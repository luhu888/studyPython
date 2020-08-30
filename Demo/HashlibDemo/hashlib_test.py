import hashlib


register_path = 'register'    # 静态，配置项


def get_md5(username, password):
    """
    公共组件
    :param username:
    :param password:
    :return:
    """
    m = hashlib.md5()
    m.update(username.encode('utf-8'))
    m.update(password.encode('utf-8'))
    return m.hexdigest()


def register(username, password):
    """
    主逻辑函数
    :param username:
    :param password:
    :return:
    """
    ret = get_md5(username, password)
    with open(register_path, mode='a') as f1:
        f1.write(ret+'\n')


def login(username, password):
    """
    主逻辑函数
    :param username:
    :param password:
    :return:
    """
    ver = get_md5(username, password)
    with open(register_path, mode='r', encoding='utf-8') as f1:
        for i in f1:
            if i.strip() == ver:
                print('登录成功')
                return True
            else:
                print('账号密码错误')
                break


def view():
    pass


func_dict = {
    1: register,
    2: login,
    3: quit,
    4: view
}


def run():
    while 1:
        func = int(input('1.register 2.login 3.quit:'))
        name = input('请输入用户名：')
        password = input('请输入密码：')
        func_dict[func](name, password)


if __name__ == '__main__':
    run()       # 启动按钮


