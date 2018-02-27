#Auther : Mustbe
import socket

# def connect_server():
#
#     info = input('Please input Server adress and port:')
#     if not info:
#         print('必须输入地址信息')
#     try:
#         address = info.split(' ')[0]
#         port = int(info.split(' ')[1])
#         return client.connect((address,port))
#     except IndexError as e:
#         print('格式不对，如：\'192.162.1.1 2222\'')
#         return 0
def connect_server():

    return client.connect(('127.0.0.1',22222))

def user_auth():
    username = input('输入用户名：')
    passwd = input('输入密码：')
    user_info = username + ' ' + passwd
    client.send(user_info.encode())
    res = client.recv(1024)
    if res.decode('utf-8') == '1':
        print('登陆成功')
    else:
        print ('登陆失败')

if __name__ == '__main__':
    client = socket.socket()
    res = connect_server()
    if res != 0:
        while True:

            print('''
                1.申请用户
                2.登陆
            ''')
            choice = input('输入选项代码：')
            if choice == '1':
                client.send(choice.encode())
                ack = client.recv(1024).decode()
                print(ack)
                print('输入用户名以及密码')
                username = input('输入用户名：')
                passwd = input('请输入密码：')
                repasswd = input('请重复输入密码：')
                if passwd == repasswd and username:
                    #user_stats 0 未登陆  1 已经登陆 2 封号
                    client.send((username + ' ' + passwd).encode())
                    res = client.recv(1024).decode()#用户建立成功
                    print(res)
                    continue
                else :
                    print('格式不对')
                    continue
            if choice == '2':
                client.send(choice.encode())
                ack = client.recv(1024).decode()
                user_auth()
                cmd = input('>>>').strip()
                client.send(cmd.encode())

                #print(client.recv(1024).decode('utf-8'))





