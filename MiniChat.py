import tkinter as tk
import socket
from time import ctime
import json

def signin():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8000

    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    
    s.connect((host, port))
    print('[{}]连接成功'.format(ctime()))
    sendData = json.dumps((0, account.get(), password.get())) 
    s.send(sendData.encode('utf-8'))
    print('[{}]成功发送登录请求'.format(ctime()))
    s.close()

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