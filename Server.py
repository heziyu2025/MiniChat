import socket

server = socket.socket()
host = socket.gethostname()
port = 0
server.bind((host, port))
print('连接已开启：', host, ':', port)
server.listen(5)

while True:
    c,addr = server.accept()
    print('连接地址：', addr)
    socket.commloopß
    print(c.recv(1024))
    c.close()