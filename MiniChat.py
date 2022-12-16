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

        sendData = json.dumps((0, self.account_entry.get(), self.password_entry.get())) 
        s.send(sendData.encode('utf-8'))
        self.prints('成功发送登录请求')

        if (s.recv(1024).decode('utf-8') == '0'):
            self.prints('登录成功')
            self.account = self.account_entry.get()
            self.password = self.password_entry.get()
            messagebox.showinfo('信息', '登录成功！')
        else:
            self.prints('登录失败，用户名或密码错误')
            messagebox.showerror('错误', '用户名或密码错误')

        s.close()

    def signup(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '192.168.1.14'
        port = 8000

        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        
        s.connect((host, port))
        self.prints('连接成功')

        sendData = json.dumps((1, self.account_entry.get(), self.password_entry.get())) 
        s.send(sendData.encode('utf-8'))
        self.prints('成功发送登录请求')

        give_back = s.recv(1024).decode('utf-8')
        if give_back == '0':
            self.prints('注册成功')
            self.account = self.account_entry.get()
            self.password = self.password_entry.get()
            messagebox.showinfo('信息', '注册成功！')
        elif give_back == '1':
            self.prints('注册失败，该用户名已经被注册')
            messagebox.showerror('错误', '该用户名已经被注册')

    def sign_main(self):
        root = tk.Tk()
        root.title('Mini Chat')

        tk.Label(root, text="账户：").grid(row=0)
        tk.Label(root, text="密码：").grid(row=1)

        self.account_entry = tk.Entry(root, width=20)
        self.account_entry.grid(row=0, column=1)

        self.password_entry = tk.Entry(root, width=20, show='*')
        self.password_entry.grid(row=1, column=1)

        signin_button = tk.Button(root, text='登录', command=self.signin)
        signin_button.grid(row=2, column=0)

        signup_button = tk.Button(root, text='注册', state='active', command=self.signup)
        signup_button.grid(row=2, column=1, sticky=tk.W)

        root.mainloop()

    def __init__(self):
        self.sign_main()

MiniChat()