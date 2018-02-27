#Auther : Mustbe

import os,sys,socketserver

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from core import main
# print(BASE_DIR)
from conf import config

if __name__ == '__main__':

    HOST,port = '0.0.0.0',22222

    server = socketserver.ThreadingTCPServer((HOST,port),main.FTP_SERVER_MAIN)

    server.serve_forever()




