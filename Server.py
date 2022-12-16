import socket
import tkinter as tk
from time import ctime
import threading

def prints(text):
    rootText.insert(tk.END, text)

def mainloop():
    root.mainloop()

root = tk.Tk()
root.title('Mini Chat Server')
rootText = tk.Text(root, width=30, height=5)
rootText.pack()

threading.Thread(target=mainloop)

server = socket.socket()
host = socket.gethostname()
port = 8001
server.bind((host, port))
prints('启动服务监听：{}:{}'.format(host, port))
server.listen(5)

while True:
    c,addr = server.accept()
    prints('用户：{} 接入系统'.format(addr))
    data = c.recv(1024)
    print('data=%s' % data)
    prints('[{}]接收数据：{!r}'.format(ctime(), data.decode('utf-8')))
    c.close()