#coding:utf-8

#全局使用，标记用户是否登录，保存登录后的用户名
USERSTATUS = {
    'islogin':False,
    'username':''
}
#ISLOGIN = False

def checklogin_re(func):
    '''
    login decorator
    :param func:
    :return:
    '''

    def wrapper(*args,**kwargs):
        if USERSTATUS['islogin']:
            return func(*args,**kwargs)

        else:
            exit("not login")

    return wrapper

