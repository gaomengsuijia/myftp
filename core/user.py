#coding:utf-8
import os,sys
import json
import hashlib
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = "%s\data"%BASE_DIR
print(DATA_DIR)
sys.path.append(BASE_DIR)
from conf import conf
from core import checklogin
class User(object):
    '''
    用户模型
    '''

    def __init__(self,username,password):
        self.username = username
        self.password = password


    def login(self,username,password):
        '''
        login
        :param username:
        :param password:
        :return:
        '''
        if username == '' or password == '':
            print("parameter erro")
            return {'userinfo':'','status':1001,'info':'parameter erro'}
        hash = hashlib.md5()
        hash.update(bytes(username, encoding="utf-8"))
        user_hash = hash.hexdigest()
        print(user_hash)
        file_path = os.path.join(DATA_DIR,user_hash)
        if os.path.isfile(file_path):
            try:
                with open(file_path,'r') as f:
                    userinfo = json.load(f)
                    print(userinfo)
                    if username == userinfo['username']:
                        if password == userinfo['password']:
                            print("login sucess")
                            #修改登录标志
                            checklogin.USERSTATUS['islogin'] = True
                            checklogin.USERSTATUS['username'] = self.username
                            return {'userinfo':{'username':userinfo['username']},'status':0,'info':'login sucess'}
                        else:
                            print("password erro")
                            return {'userinfo':'','status':1002,'info':'password erro'}
                    else:
                        print('username erro')
                        return {'userinfo':'','status':1003,'info':'username erro'}
            except OSError as e:
                print("not open file,resean is %s"%str(e))
                return {'userinfo':'','status':1004,'info':'not open file'}

        else:
            print('file not exits')
            return {'userinfo':'','status':1005,'info':'file not exits'}




    def regist(self):
        '''
        regist
        :return:
        '''
        #查询是否重复
        if self.isre():
            print("该用户已经注册")
            return False
        if self.username.isalnum() and self.password.isalnum():
            userinfo = {'username':self.username,'password':self.password}
            hash = hashlib.md5()
            hash.update(bytes(self.username,encoding="utf-8"))
            user_hash = hash.hexdigest()
            print(user_hash)
            file_path = os.path.join(DATA_DIR,user_hash)
            print(file_path)
            try:
                with open(file_path,'w') as f:
                    json.dump(userinfo,f)
                    print("regist success")
                    # 修改登录标志
                    checklogin.USERSTATUS['islogin'] = True
                    checklogin.USERSTATUS['username'] = self.username
                    return True
            except OSError as e:
                print('can not open file,the resorn is %s'%str(e))


        else:
            print("param is erro")
            return False



    def isre(self):
        '''
        用户是否已经注册
        :return:
        '''
        hash = hashlib.md5()
        hash.update(bytes(self.username,encoding="utf-8"))
        user_hash = hash.hexdigest()
        print(user_hash)
        if os.path.isfile(os.path.join(DATA_DIR,user_hash)):
            return True
        else:
            return False







if __name__ == "__main__":
    user = User('xiaotu','123456')
    user.login('xiaotu','123456')
    print(checklogin.USERSTATUS['islogin'])