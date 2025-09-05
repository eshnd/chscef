if "1" not in input("step 1 or 2"):
    import os; os.system("pyenv global 3.7.17 && python3.7 -m pip install cefpython3 && python3.7 ~/browser.py")
else:
    import os; os.system("sh prep.sh &")
    import tkinter as tk
    import sys
    
    def say_alive():
        print("i am alive")
    
    def kill_me():
        sys.exit()
    
    root = tk.Tk()
    root.title("alive button")
    
    btn = tk.Button(root, text="click me", command=say_alive)
    btn.pack(pady=20)
    
    btn2 = tk.Button(root, text="wait", command=kill_me)
    btn2.pack(pady=20)
    
    root.mainloop()