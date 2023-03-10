import tkinter as tk
import socket
from time import ctime
import json
import tkinter.messagebox as messagebox
import base64
from tkinter import ttk

def prints(text):
    print('[{}]{}'.format(ctime(), text))

class Login():
    def change_dat(self):
        with open('data', 'wb') as f:
            dat_en = json.dumps(self.data).encode()
            f.write(base64.b64encode(dat_en))
            f.close()
        prints(self.data)

    def signin(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '192.168.1.14'
        port = 8000

        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        
        s.connect((host, port))
        prints('连接成功')

        sendData = json.dumps((0, self.account_entry.get(), self.password_entry.get())) 
        s.send(sendData.encode('utf-8'))
        prints('成功发送登录请求')

        if (s.recv(1024).decode('utf-8') == '0'):
            prints('登录成功')
            self.account = self.account_entry.get()
            self.password = self.password_entry.get()
            self.data['account'] = self.account
            self.data['password'] = self.password
            self.change_dat()
            prints(self.data)
            self.root.destroy()
        else:
            prints('登录失败，用户名或密码错误')
            messagebox.showerror('错误', '用户名或密码错误')

        s.close()

    def signup(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '218.89.171.135'
        port = 48193

        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        
        s.connect((host, port))
        prints('连接成功')

        sendData = json.dumps((1, self.account_entry.get(), self.password_entry.get())) 
        s.send(sendData.encode('utf-8'))
        prints('成功发送登录请求')

        give_back = s.recv(1024).decode('utf-8')
        if give_back == '0':
            prints('注册成功')
            self.account = self.account_entry.get()
            self.password = self.password_entry.get()
            self.data['account'] = self.account
            self.data['password'] = self.password
            self.change_dat()
            self.prints(self.data)
            self.root.destroy()
            self.mainApp()
        elif give_back == '1':
            prints('注册失败，该用户名已经被注册')
            messagebox.showerror('错误', '该用户名已经被注册')

    def remember_password_command(self):
        self.data['remember password'] = not self.data['remember password']
        self.change_dat()

    def auto_signin_command(self):
        if self.data['auto signin']:
            self.data['auto signin'] = False
        else:
            if not self.data['remember password']:
                self.auto_signin_checkbutton.deselect()
                messagebox.showerror('错误', '请先选择“记住密码。”')
            else:
                self.data['auto signin'] = True
        self.change_dat()

    def __init__(self):
        try:
            with open('data', 'rb') as f:
                dat = f.read()
                baseen = base64.b64decode(dat)
                base = baseen.decode()
                self.data = json.loads(base)
                f.close()
        except:
            self.data = {'remember password': True, 'auto signin': False, 'account': '', 'password': '', 'friends': []}
            self.change_dat()

        prints(self.data)

        self.root = tk.Tk()
        self.root.title('Mini Chat')

        ttk.Label(self.root, text="账户：").grid(row=0)
        ttk.Label(self.root, text="密码：").grid(row=1)


        account_en = tk.StringVar(value=self.data['account'])
        password_en = tk.StringVar(value=self.data['password'])

        if self.data['remember password']:
            self.account_entry = ttk.Entry(self.root, width=20, textvariable=account_en)
        else:
            self.account_entry = ttk.Entry(self.root, width=20)

        self.account_entry.grid(row=0, column=1)

        if self.data['remember password']:
            self.password_entry = ttk.Entry(self.root, width=20, show='*', textvariable=password_en)
        else:
            self.password_entry = ttk.Entry(self.root, width=20, show='*')

        self.password_entry.grid(row=1, column=1)

        remember_password_checkbutton = tk.Checkbutton(self.root, text='记住密码', command=self.remember_password_command)
        remember_password_checkbutton.grid(row=2, column=0)

        if (self.data['remember password']):
            remember_password_checkbutton.select()

        self.auto_signin_checkbutton = tk.Checkbutton(self.root, text='自动登录', command=self.auto_signin_command)
        self.auto_signin_checkbutton.grid(row=2, column=1, sticky=tk.W)

        if (self.data['auto signin']):
            self.auto_signin_checkbutton.select()
            self.signin()

        signin_button = ttk.Button(self.root, text='登录', command=self.signin)
        signin_button.grid(row=3, column=0)

        signup_button = ttk.Button(self.root, text='注册', command=self.signup)
        signup_button.grid(row=3, column=1, sticky=tk.W)

        self.root.mainloop()

class MiniChat():
    def __init__(self):
        login = Login()
        self.data = login.data

        self.root = tk.Tk()
        self.root.title('Mini Chat')

        top_frame = ttk.Frame(self.root)

        tk.Label(top_frame, text='请选择：').pack(side=tk.LEFT)

        friends_name = []
        self.friends = self.data['friends']
        for i in self.friends:
            friends_name.append(i['name'])

        friends_name = tuple(friends_name)

        friend_list_box = ttk.Combobox(top_frame, values=friends_name)
        friend_list_box.pack(side=tk.LEFT)

        top_frame.pack()

        self.root.mainloop()

MiniChat()