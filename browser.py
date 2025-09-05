from cefpython3 import cefpython as cef
import tkinter as tk
import sys
import threading

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("testing123")
        self.master.geometry("800x512")

        self.browser_frame = tk.Frame(master)
        self.browser_frame.pack(fill=tk.BOTH, expand=1)

        self.browser_frame.bind("<Configure>", self.on_configure)

        self.browser = None
        self.master.after(100, self.embed_browser)
        self.master.after(10, self.cef_loop)

    def embed_browser(self):
        self.master.update_idletasks()
        window_info = cef.WindowInfo()

        rect = [0, 0, self.browser_frame.winfo_width(), self.browser_frame.winfo_height()]
        window_info.SetAsChild(self.browser_frame.winfo_id(), rect)

        self.browser = cef.CreateBrowserSync(
            window_info,
            url="https://showmyip.com"
        )

    def on_configure(self, event):
        if self.browser:
            self.browser.SetBounds(0, 0, event.width, event.height)
            self.browser.NotifyMoveOrResizeStarted()

    def cef_loop(self):
        cef.MessageLoopWork()
        self.master.after(10, self.cef_loop)

    def load_url(self, url):
        if self.browser:
            self.browser.LoadUrl(url)

def url_input_loop(app):
    while True:
        url = input("url: ").strip()
        app.load_url(url)

sys.excepthook = cef.ExceptHook

switches = {
    "disable-gpu": "",
    "disable-gpu-compositing": "",
    "enable-begin-frame-scheduling": ""
}

cef.Initialize(switches=switches)

root = tk.Tk()
app = MainApp(root)

threading.Thread(target=url_input_loop, args=(app,), daemon=True).start()

root.protocol("WM_DELETE_WINDOW", lambda: (cef.Shutdown(), root.destroy()))
root.mainloop()