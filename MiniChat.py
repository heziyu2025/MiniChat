import tkinter as tk
import socket

def signin():
    server = socket.socket()
    host = '192.168.1.14'
    port = 8001
    
    server.connect((host, port))
    print('连接成功')
    inData = '1283789478'
    server.send(inData.encode('utf-8'))
    print('发送成功！', inData)
    server.close()

root = tk.Tk()
root.title('Mini Chat')

tk.Label(root, text="账户：").grid(row=0)
tk.Label(root, text="密码：").grid(row=1)

account = tk.Entry(root, width=20)
account.grid(row=0, column=1)

password = tk.Entry(root, width=20, show='*')
password.grid(row=1, column=1)

signin_button = tk.Button(root, text='登录', command=signin)
signin_button.grid(row=2, column=0)

signup_button = tk.Button(root, text='注册', state='active')
signup_button.grid(row=2, column=1, sticky=tk.W)

root.mainloop()