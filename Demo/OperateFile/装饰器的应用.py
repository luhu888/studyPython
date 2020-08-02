user_status = {'username': None, 'status': False}


def user_info():
    info = {}
    with open('register') as f1:
        li = []
        for line in f1:
            li = line.strip().split('|')
            info[li[0]] = li[1]
    return info


def login():
    info = user_info()
    count = 1
    while count < 4:
        username = input('请输入用户名：')
        password = input('请输入密码：')
        if username in info and password == info[username]:
            user_status['username'] = username
            user_status['status'] = True
            print('登录成功')
            return True
        else:
            print('账号密码错误')
            count += 1
    # return False


def auth(f):

    def inner(*args, **kwargs):
        if user_status['status'] is True:
            ret = f(*args, **kwargs)
            return ret
        elif login():
            ret = f(*args, **kwargs)
            return ret
        else:
            print('登录失败，无法访问该页面，请稍后重试！！！！！')
    return inner


@auth
def article():  # inner()
    print('欢迎访问文章页面')


@auth
def content():
    print('欢迎访问内容页面')



article()
content()


