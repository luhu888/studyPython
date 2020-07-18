# from testpath.xx.y import yy
# 相对导入会报错，可以使用顶级目录导入
# from ..y import yy
from ..y.yy import *

# import testpath.xx.y.yy
'''
相对导入同项目下的模块，.相当于当前路径，..相当于所在路径的父路径
'''
z_age = 666


def z_f():
    print('z_f')


if __name__ == '__main__':
    y_f()
