import time
import socket
server = socket.socket()
host = '127.0.0.1'
port = 8848
server.bind((host, port))
server.listen(5)


def find_data(match):
    print('你要查询的应用是:' + match)
    match = match+'\n'
    print(len(match))
    f = open('password.txt', 'r+')
    data = f.readlines()
    line = len(data)
    print('开始遍历查找')
    for i in range(line):
        for i in range(line):
            if match == data[i]:
                print('已找到')
                print('应用:'+data[i],
                    '账号:'+data[i+1],
                    '密码:'+data[i+2])
                time.sleep(0.1)
                s.send(data[i].encode())
                time.sleep(0.1)
                s.send(data[i+1].encode())
                time.sleep(0.2)
                s.send(data[i+2].encode())
                print('用户信息已发送到客户端')
                break
        else:
            print('没有找到')
            s.send('1'.encode())
            break
    f.close()

def add_password(app, account, password):
    with open('password.txt', 'a') as f:
        f.write(app + '\n')
        print(len(app))
        f.write(account + '\n')
        print(len(account))
        f.write(password + '\n')
        print(len(password))
        f.close()


while True:
    s, addr = server.accept()
    username = s.recv(1024).decode()
    userpassword = s.recv(1024).decode()
    s.send('服务器接受到账号密码,正在验证'.encode())
    print(username, userpassword)
    if username == 'admin' and userpassword == 'hello':
        print('账号密码验证成功')
        s.send('账号密码验证成功'.encode())
        choice = s.recv(1024).decode()
        print(choice)
        if choice == '1':
            app = s.recv(1024).decode()
            account = s.recv(1024).decode()
            password = s.recv(1024).decode()
            add_password(app=app, account=account, password=password)
        if choice == '2':
            match = s.recv(1024).decode()
            find_data(match=match)

    else:
        print('账号或密码有误')
        s.send('账号或密码有误'.encode())
