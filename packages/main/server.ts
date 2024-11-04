import child_process from "node:child_process"
import { join } from "node:path"
import { app } from "electron"

const port: number = 17173

let instance: child_process.ChildProcess

/**
 * 开启python的api服务
 * @returns
 */
export function startServer() {
  judgeServerOpen(port).then(async res => {
    if (res) {
      console.log(`${port} is in used"`)
      await stopServer()
    }
    if (app.isPackaged) {
      // exec不会报错 spawn会抛错
      instance = child_process.exec("\"./resources/dnfcalc-api.exe\"", (_, stdout: any) => {
        console.log(stdout)
      })
      console.log("server started.")
      return
    }

    const execCommand = process.platform === "win32" ? "python" : "python3"

    instance = child_process.spawn(execCommand, [join(__dirname, "../../../api/main.py"), `${port}`])

    if (instance) {
      console.log("server started.")
      instance.stdout?.pipe(process.stdout)
      instance.stderr?.pipe(process.stderr)
      instance.stdin?.pipe(process.stdin)
    }
  })
}

/**
 * 判断端口是否被占用
 * @param port 端口号
 * @returns 该端口是否被占用
 */
function judgeServerOpen(port: number): Promise<boolean> {
  const order = `netstat -ano|findstr "${port}"`
  return new Promise<boolean>(resolve => {
    child_process.exec(order, (_: any, stdout: any) => {
      if (stdout === "") {
        resolve(false)
      } else {
        resolve(true)
      }
    })
  })
}

/**
 * 关闭python的api服务
 * @returns
 */
export function stopServer(): Promise<string> {
  const order = process.platform == "win32" ? "taskkill /f /im dnfcalc-api.exe" : "taskkill /f /im python.exe"

  return new Promise(resolve => {
    if (instance) {
      if (instance.kill(0) && instance.kill()) {
        console.log("server stoped.")
      }
      resolve("server stoped.")
    }
    child_process.exec(order, (_, stdout: string) => {
      // TODO 关闭python api
      resolve(stdout)
    })
  })
}
