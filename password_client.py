import time
import os.path
import socket
client = socket.socket()
if os.path.exists('address.txt') == False:
    host = input('目标ip:')
    save_ip = input('是否记录IP?(y/n)')
    if save_ip == 'y':
        with open('address.txt', 'w') as f:
            f.write(host)
            f.close()
    elif os.path.exists('address.txt') == True:
        pass
    elif save_ip == 'n':
        pass
    else:
        print('选项错误，跳过此阶段')
else:
    pass

with open('address.txt', 'r') as f:
    host = f.read()
    f.close()
port = 8848
client.connect((host, port))
username = input('请输入数据库用户名:')
userpassword = input('请输入数据库密码:')
client.send(username.encode())
client.send(userpassword.encode())
print(client.recv(1024).decode())
print(client.recv(1024).decode())
choice = input('选择1.添加2.查询:')
client.send(choice.encode())
if choice == '1':
    app = input("应用:")
    account = input('账号:')
    password = input('密码:')
    client.send(app.encode())
    time.sleep(0.1)
    client.send(account.encode())
    time.sleep(0.1)
    client.send(password.encode())
if choice == '2':
    match = input('请输入应用:')
    client.send(match.encode())
    error = client.recv(1024).decode()
    if error == '1':
        print('错误')
    App_user = client.recv(1024).decode()
    App_password = client.recv(1024).decode()
    App_name = client.recv(1024).decode()
    print('应用:' + App_name + '账号:' + App_user + '密码:' + App_password)
    input()
