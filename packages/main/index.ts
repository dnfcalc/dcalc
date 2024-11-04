import { join } from "node:path"
import path from "path"
import { BrowserWindow, app, ipcMain, screen, shell } from "electron"
import { startServer, stopServer } from "./server"


// Disable GPU Acceleration for Windows 7
// if (release().startsWith("6.1"))
app.disableHardwareAcceleration()
// Set application name for Windows 10+ notifications
if (process.platform === "win32") {
  app.setAppUserModelId(app.getName())
}

process.env.ELECTRON_DISABLE_SECURITY_WARNINGS = "true"

if (!app.requestSingleInstanceLock()) {
  app.quit()
  process.exit(0)
}

let win: BrowserWindow | null = null

const storage:any = {}

let factor = 1.0

async function createWindow() {
  factor = Math.min(screen.getPrimaryDisplay().workAreaSize.height * 0.75 / 680, screen.getPrimaryDisplay().scaleFactor);
  win = new BrowserWindow({
    frame: false,
    width: Math.round(920 * factor),
    height: Math.round(680 * factor),
    resizable: false,
    icon: join(__dirname, "../renderer/favicon.ico"),
    webPreferences: {
      preload: join(__dirname, "../preload/index.cjs"),
      nodeIntegration: true,
      contextIsolation: false,
      webSecurity: false,
      devTools: import.meta.env.DEV,
      partition: String(+new Date()),
      zoomFactor: factor
    }
  })
  win.setMenuBarVisibility(false)

  win.webContents.session.clearCache()

  if (app.isPackaged) {
    win.loadURL(`http://localhost:17173?r=${Math.random()}`)
    // win.webContents.reloadIgnoringCache()
  } else {
    // 🚧 Use ['ENV_NAME'] avoid vite:define plugin
    const url = `http://${process.env.VITE_DEV_SERVER_HOST}:${process.env.VITE_DEV_SERVER_PORT}?r=${Math.random()}`
    win.loadURL(url)
    // win.webContents.openDevTools({ mode: "undocked", activate: true })
  }

  // Test active push message to Renderer-process
  // win.webContents.on("did-finish-load", () => {
  //   win?.webContents.send("main-process-message", new Date().toLocaleString())
  // })

  // Make all links open with the browser, not with the application
  win.webContents.setWindowOpenHandler(({ url }) => {
    const { origin } = new URL(url)
    if (origin != "localhost") {
      shell.openExternal(url)
    }
    return { action: "deny" }
  })

  win.webContents.closeDevTools()

  win.setMenuBarVisibility(false)

  // 注册自定义协议
  const agreement = 'dcalc' // 自定义协议名
  let isSet = false // 是否注册成功

  app.removeAsDefaultProtocolClient(agreement) // 每次运行都删除自定义协议 然后再重新注册
  // 开发模式下在window运行需要做兼容
  if (process.env.NODE_ENV === 'development' && process.platform === 'win32') {
    // 设置electron.exe 和 app的路径
    isSet = app.setAsDefaultProtocolClient(agreement, process.execPath, [
      path.resolve(process.argv[1]),
    ])
  } else {
    isSet = app.setAsDefaultProtocolClient(agreement)
  }
}

startServer()

setTimeout(() => {
  app.whenReady().then(createWindow)
}, 5000)

app.on("window-all-closed", () => {
  win = null
  app.quit()
})

app.on("quit", () => {
  stopServer().then(() => {
    console.log("app quit.")
    app.exit(0)
  })
})

app.on("second-instance", (event,commandLine) => {
  let uid = undefined
  const command = commandLine.find(a=>a.startsWith("dcalc://"))
  if(!!command){
    uid = command.split('uid=')?.[1] ?? ""
  }
  storage["uid"] = decodeURIComponent(uid ?? "")
  if (win) {
    // Focus on the main window if the user tried to open another
    if (win.isMinimized()) {
      win.restore()
    }
    if (!undefined){
      win.reload()
    }
    win.focus()
  }
})

app.on("activate", () => {
  const allWindows = BrowserWindow.getAllWindows()
  if (allWindows.length) {
    allWindows[0].focus()
  } else {
    createWindow()
  }
})


ipcMain.handle("open-win", (event, arg) => {
  const childWindow = new BrowserWindow({
    width: Math.round(arg.width * factor),
    height: Math.round(arg.height * factor),
    resizable: false,
    frame: false,
    icon: join(__dirname, "../renderer/favicon.ico"),
    webPreferences: {
      preload: join(__dirname, "../preload/index.cjs"),
      webSecurity: false,
      nodeIntegration: true,
      contextIsolation: false,
      partition: String(+new Date()),
      zoomFactor: factor
    }
  })

  childWindow.webContents.session.clearCache()

  if (app.isPackaged) {
    const url = `http://localhost:17173${arg.url}`
    childWindow.loadURL(url)
    // childWindow.webContents.reloadIgnoringCache()
  } else {
    // 🚧 Use ['ENV_NAME'] avoid vite:define plugin
    const url = `http://${process.env.VITE_DEV_SERVER_HOST}:${process.env.VITE_DEV_SERVER_PORT}${arg.url}`
    childWindow.loadURL(url)
    // childWindow.webContents.openDevTools({ mode: "undocked", activate: true })
  }
})

ipcMain.handle("minimize-win", event => {
  const window = BrowserWindow.fromWebContents(event.sender)
  if (window) {
    window.minimize()
  }
})

ipcMain.handle("close-win", event => {
  const window = BrowserWindow.fromWebContents(event.sender)
  if (window) {
    window.close()
  }
})

ipcMain.handle("restart", () => {
  win?.webContents.session.clearCache().then(() => {
    app.relaunch()
    app.quit()
    console.log("restart...")
  })
})

ipcMain.handle("getStorage", (event, arg) => {
  return storage[arg] ?? undefined
})

ipcMain.handle("getVersion", () => {
  return app.getVersion()
})

ipcMain.handle("setStorage", (event, arg) => {
  Object.defineProperty(storage, arg.key, {
    value: arg.value,
    writable: true,
    enumerable: true,
    configurable: true
  })
})

ipcMain.handle("open-url", (event, url) => {
  shell.openExternal(url)
})

process.on("exit", () => {
  app.quit()
})
