#Auther : Mustbe

import socketserver,hashlib,json,os,sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)
from conf import config

# config_file = BASE_PATH + '''\\conf\\config.ini'''

def get_config():
    config_file = 'config.ini'
    info = config.config_gen(config_file)
    info.dump_cfg()
    dir_name = info.get_ftp_dir()
    print(dir_name)
    return dir_name

def auth_user(username,passwd):
    def wapper():

        if username == '1' and passwd == '1':

            return 1

        else: return  0

    return wapper()


class log(object):
    pass


class User_user(object):
    # def __init__(self,username,passwd):
    #
    #     self.username = username
    #     self.passwd = passwd

    def use_md5(self):
        pass

    def makeuser(self,username,passwd):
        self.username = username
        self.passwd = passwd
        info = {'username': self.username, 'password': self.passwd, 'space_size': 100,
                'user_status': '0'}
        self.filename = username + '.json'
        f = open(self.filename,'w')
        json.dump(info,f)
        dir_name = get_config()
        os.mkdir(dir_name + '\\' +self.username)
        f.flush()
        f.close()
        return 1
    def deluser(self):
        pass

    def modifyuser(self):
        pass

    def authuser(self,username,passwd):

        self.username = username
        self.passwd = passwd
        if os.path.isfile('%s.json' % self.username):
            f = open('%s.json' % self.username,'r+')
            self.info = json.load(f)
            print(self.info['username'],self.info['password'])
            if self.username == self.info['username'] and self.passwd == self.info['password']:
                self.info['user_status'] = 1
                print(self.info)
                f.seek(0)
                json.dump(self.info,f)
                return 1
            else:
                return 0
        else:
            print('用户名不存在')

class Ftp_action(object):
    '''FTP的相关文件操作'''
    def ls_dir(self,command):
        '''列出目录里的文件'''
        os.popen('dir')
        pass


class FTP_SERVER_MAIN(socketserver.BaseRequestHandler):
    def handle(self):
        user = User_user() #实例化User对象
        fac = Ftp_action()
        while True:
            try :
                self.choice = self.request.recv(1024).decode('utf-8')

                if self.choice == '1':
                    self.request.send('开始建立用户吧~'.encode())
                    self.info = self.request.recv(1024).decode()
                    self.username = self.info.split(' ')[0]
                    self.passwd = self.info.split(' ')[1]
                    mkuser = user.makeuser(self.username,self.passwd )
                    if mkuser == 1:
                        self.request.send((self.username + '建立成功').encode())
                        print('建立成功')
                        continue
                    else:
                        self.request.send((self.username + '建立失败').encode())
                        continue

                #print('当前用户链接：%s' % self.client_address)
                #log()
                elif self.choice == '2':
                    self.request.send('开始登陆吧'.encode())
                    self.info = self.request.recv(1024).decode()
                    self.username = self.info.split(' ')[0]
                    self.passwd = self.info.split(' ')[1]
                    res = user.authuser(self.username,self.passwd)
                    if res == 1:
                        self.request.send('1'.encode())
                        self.cmd = self.request.recv(1024).encode()
                        if self.cmd.startswith('get'):
                            pass
                        elif self.cmd.startswith('put'):
                            pass
                        elif self.cmd.startswith('ls'):
                            self.cmd = self.cmd.split(' ')[1]
                            res = fac.ls_dir(self.cmd)#列出目录文件
                            self.request.send(res)
                        elif self.cmd.startswith('cd'):
                            pass



                    else:
                        self.request.send('login vaild'.encode())
            except ConnectionError as e:
                self.request.send(b'0')
                print('%s 链接失败 reason: %s' % (self.client_address,e))




if __name__ == '__main__':
    get_config()

