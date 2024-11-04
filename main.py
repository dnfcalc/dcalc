import subprocess
import sys
import psutil
import webview

# pyinstaller .\main.py --exclude-module PyQt5

global BASE_URL

def kill(proc_pid):
    try:
        if proc_pid is not None and proc_pid > 0:
            process = psutil.Process(proc_pid)
            for proc in process.children(recursive=True):
                proc.kill()
                process.kill()
    except Exception:
        pass

def get_pid_by_port(port):
    for conn in psutil.net_connections():
        if conn.laddr.port == port:
            return conn.pid
    return None

class WIN:
    def __init__(self,url="",width=800,height=600):
        self.window = webview.create_window("DNF计算器",url=BASE_URL + url,frameless=True,easy_drag=False,width=width,height=height)
        self.window.expose(self.invoke)

    # def onShow(self):
    #     print("show")

    def invoke(self,commond = "",arg = None):
        if commond == "close-win":
            self.window.destroy()
        if commond == "minimize-win":
            self.window.minimize()
        if commond == "open-win":
            WIN(arg.get("url",""),width=arg.get("width"),height=arg.get("height"))


if __name__ == "__main__":
    # 启动服务
    # 创建webview窗口
    # 启动webview事件循环

    env = "release"
    for i in sys.argv:
        if i.startswith("--dev"):
            env = "dev"
            break
    p = 0
    q = 0
    if env == "dev":
        # print(get_pid_by_port(17173),get_pid_by_port(25252))
        kill(get_pid_by_port(17173))
        p = subprocess.Popen(f'python ./api/main.py',shell=True).pid
        kill(get_pid_by_port(25252))
        q = subprocess.Popen(f'vite ./packages/renderer',shell=True).pid
        BASE_URL = "http://127.0.0.1:25252"
    else:
        kill(get_pid_by_port(17173))
        p = subprocess.Popen(f'.\\resources\\dnfcalc-api.exe',shell=True).pid
        BASE_URL = "http://127.0.0.1:17173"
    view = WIN()
    view.window.events.closing += lambda : kill(p)
    view.window.events.closing += lambda : kill(q)
    webview.start(debug=env=='dev')
