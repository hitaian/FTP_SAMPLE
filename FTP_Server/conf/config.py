#Auther : Mustbe
import sys
import os
import configparser

class config_gen(object):
    def __init__(self,file):
        self.file = os.path.abspath(file)
        self.cfg = configparser.ConfigParser()

    def add_config(self,se):
        self.cfg.add_section(se)

    def add_item(self,se,key,value):
        self.cfg.set(se,key,value)

    def write_cfg(self):
        f = open(self.file,'w')
        self.cfg.write(f)
        f.close()

    def get_ftp_dir(self):
        info = self.cfg.get('BASE_DIR','ftpdir')
        print(info)
        return info

    def get_cfg(self):
        info = self.cfg.read(self.file)
        print(info)

    def dump_cfg(self):
        se_list = self.cfg.sections()  # cfg.sections()显示文件中的所有 section
        print('==================>')
        for se in se_list:
            print(se)
            print(self.cfg.items(se))
        print('==================>')



if __name__ == '__main__':

    info = config_gen('config.ini')
    info.add_config('BASE_DIR')
    info.add_item('BASE_DIR','ftpdir','''E:\\py_study_new\\day7\\FTP_SERVER\\data\\''')
    info.write_cfg()
    info.get_ftp_dir()
    info.get_cfg()
    info.dump_cfg()