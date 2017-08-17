#coding:utf-8
import os,sys
import paramiko
class Client(object):
    '''
    客户端
    '''
    def __init__(self,hostname="10.200.12.8",port=22,username='root',password='yishandb'):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password



    def cmd_handle(self,cmd):
        '''
        ssh cmd
        :param cmd:
        :return:
        '''
        myssh = paramiko.SSHClient()
        myssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接ssh
        myssh.connect(self.hostname, self.port, self.username, self.password)
        # 执行命令
        stin, stout, sterro = myssh.exec_command(cmd)
        # 获取名
        result = stout.read()
        print(result.decode())
        # 关闭
        myssh.close()


    def get_file(self,filename):
        '''
        put file or get file
        :param file_cmd:
        :return:
        '''
        tansport = paramiko.Transport(self.hostname,self.port)
        tansport.connect(username=self.username, password=self.password)
        # 创建sftp
        sftp = paramiko.SFTPClient.from_transport(tansport)
        # 将文件从服务器下载到本地
        try:
            sftp.get(filename, 'test_from_linux')
            tansport.close()
            return {'status':0,'info':'success'}
        except FileNotFoundError as e:
            print("erro,the reason is %s"%str(e))
            return {'status': 1, 'info': 'fail'}


    def put_file(self,filename):
        '''
        put file or get file
        :param file_cmd:
        :return:
        '''
        tansport = paramiko.Transport((self.hostname,self.port))
        tansport.connect(self.username, self.password)
        # 创建sftp
        sftp = paramiko.SFTPClient.from_transport(tansport)
        # 将文件上传至服务器
        try:
            sftp.put('test', '/opt/test_from_window')
            tansport.close()
            return {'status':0,'info':'success'}
        except FileNotFoundError as e:
            print("erro,the reason is %s"%str(e))
            return {'status': 1, 'info': 'file not find'}




if __name__ == "__main__":
    myclient = Client()
    myclient.get_file('/opt/test_ffdsa')