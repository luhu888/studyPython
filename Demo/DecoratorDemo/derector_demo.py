def logger(log):
    def wrapper(f):
        def inner(*args, **kwargs):
            f(*args)
            ret1 = '函数%s已经记录到日志%s中,传入了%s参数' % (f.__name__, log, args[0])
            print(ret1)
            return f(*args)
        return inner
    return wrapper


@logger('log')
def func(name):
    ret = '实现了%s功能' % name
    return ret


print(func('login'))