#coding:utf-8
from core import user
from core import checklogin
from core.checklogin import checklogin_re
from client import client
class Views(object):
    '''
    界面交互
    '''


    def __init__(self):
        pass


    def login_view(self):
        '''
        login views
        :return:
        '''

        print("欢迎进入系统登录页面")
        while True:
            username = input("请输入登录账号:").strip()
            password = input("请输入登录密码:").strip()
            if username == "" or password == "":
                print("用户名或者密码不能为空")
                continue
            elif not username.isalnum() and not password.isalnum():
                print("用户名或者密码格式不正确")
                continue
            else:
                re_user = user.User(username, password)
                result = re_user.login(username,password)
                if result['status'] == 0:
                    self.sys_view(username)

    def regist_view(self):
        '''
        regist view
        :return:
        '''
        print("欢迎进入系统注册页面")
        while True:
            username = input("请输入账号:").strip()
            password = input("请输入密码:").strip()
            if username == "" or password == "":
                print("用户名或者密码不能为空")
                continue
            elif not username.isalnum() and not password.isalnum():
                print("用户名或者密码格式不正确")
                continue
            else:
                re_user = user.User(username,password)
                result = re_user.regist()
                if result:
                    self.sys_view(username)

    @checklogin_re
    def sys_view(self,username):
        '''
        sys view
        :return:
        '''
        print("欢迎进入系统")
        while True:
            cmd = input("%s==>"%username)
            cmd_arry = cmd.split()
            if len(cmd_arry)>1:
                myclient = client.Client()
                if cmd_arry[0] == 'get':
                    file_name = '/opt/' + cmd_arry[1]
                    result = myclient.get_file(file_name)
                    if result['status'] == 0:
                        print("ok")
                    else:
                        print(result['info'])
                elif cmd_arry[0] == 'put':
                    file_name = '/opt/' + cmd_arry[1]
                    result = myclient.put_file(file_name)
                    if result['status'] == 0:
                        print("ok")
                    else:
                        print(result['info'])
                else:
                    print("not the cmd")
            else:
                myclient = client.Client()
                myclient.cmd_handle(cmd)







    def interview(self):
        '''
        总的界面入口
        :return:
        '''
        user_opion = {
            '1':self.login_view,
            '2':self.regist_view,
            '3':self.sys_view,
            '4':exit
        }

        while True:
            user_choice = input('''
                    请选择功能菜单：
                    1、登录
                    2、注册
                    3、进入系统
                    4、退出
                    ====》''').strip()
            if str(user_choice) == '4':
                user_opion[str(user_choice)]("退出成功")
            if str(user_choice) == '3':
                user_opion[str(user_choice)](checklogin.USERSTATUS['username'])
            if str(user_choice) in user_opion:
                user_opion[str(user_choice)]()

            else:
                print("选择错误，请重新选择")
                continue


