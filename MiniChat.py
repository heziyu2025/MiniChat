import tkinter as tk
import socket
from time import ctime
import json
import tkinter.messagebox as messagebox

class MiniChat():
    def prints(self, text):
        print('[{}]{}'.format(ctime(), text))

    def signin(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '192.168.1.14'
        port = 8000

        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        
        s.connect((host, port))
        self.prints('连接成功')

        sendData = json.dumps((0, self.account.get(), self.password.get())) 
        s.send(sendData.encode('utf-8'))
        self.prints('成功发送登录请求')

        if (s.recv(1024).decode('utf-8') == '0'):
            self.prints('登录成功')
        else:
            self.prints('登录失败，用户名或密码错误')
            messagebox.showerror('错误', '用户名或密码错误')

        s.close()

    def sign_main(self):
        root = tk.Tk()
        root.title('Mini Chat')

        tk.Label(root, text="账户：").grid(row=0)
        tk.Label(root, text="密码：").grid(row=1)

        self.account = tk.Entry(root, width=20)
        self.account.grid(row=0, column=1)

        self.password = tk.Entry(root, width=20, show='*')
        self.password.grid(row=1, column=1)

        signin_button = tk.Button(root, text='登录', command=self.signin)
        signin_button.grid(row=2, column=0)

        signup_button = tk.Button(root, text='注册', state='active')
        signup_button.grid(row=2, column=1, sticky=tk.W)

        root.mainloop()

    def __init__(self):
        self.sign_main()

MiniChat()