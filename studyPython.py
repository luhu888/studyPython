import copy
import datetime
import hashlib
import json
import logging
import os
import pickle
import random
import re
import shutil
import time
from collections import namedtuple, defaultdict, Counter
from functools import reduce
from logging import handlers
from math import pi
from multiprocessing import Process, Lock, Queue

import requests

flag = True
"""
    无限循环加终止条件
"""


def xunhuan1():
    flag = True
    while flag:
        print('1')
        print('2')
        print('3')
        flag = False
        print('4')
        print('5')


def xunhuan2():
    i = 1
    while i < 101:
        print(i)
        i += 1


def xunhuan3():
    i = 0
    while i or i == 0:
        i += 1
        if i % 2 == 0:
            print(i)
        elif i > 100:
            break
        else:
            print('i=', i)


def xunhuan4():
    """
    continue相当于while循环的底部，后面不再执行
    break打断不执行else
    :return: string
    """

    i = True
    while i:
        print('1')
        print('2')
        print('3')
        i = False
        break
        print('4')

    else:
        print('end')


def geshihua():
    info = input('请输入信息：')
    name = input('请输入姓名：')
    sex = input('请输入性别：')
    str = """
    ------------info of %s-------------
    name : %s
    sex : %s
    -----------------------------------
    """ % (info, name, sex)

    print(str)


def shujuleixing_int():
    """
        进制的转化2进制和10进制
    :return:  int
    """
    i = 10
    print(i.bit_length())    # 获取二进制的有效长度


def qiepian():
    str = 'python超牛逼啊'
    print(str[0])
    print(str[:])
    print(str[::1])
    print(str[:6])  # 切片，从0开始，左闭右开
    print(str[6:])
    print(str[:5:2])  # 步长，隔1位取值
    print(str[-5:-1])   # 反向取
    print(str[-1:-6:-2])   # 倒序取需要反向步长
    print(str[-1::-1])


def upper_lower():
    user = input('请输入用户名：')
    password = input('请输入密码：')
    v_code = input('请输入验证码')
    code = 'ASdf'
    if user == 'luhu' and password == '123456' and v_code.lower() == code.lower():
        print('登录成功！！！')
    elif v_code.lower() != code.lower():
        print("验证码错误！！！")
    elif user != 'luhu' or password == '123456':
        print('用户名或密码错误！！！')


def str_operate():
    str = 'wqeASFsfdsa'
    print(str.startswith('A', 3, 6))
    print(str.startswith('w', 3, 6))    # 切片判断后面一段是否以我开头
    print(str.startswith('wqe'))
    str2 = '哈哈    路虎 哈哈哈哈，路虎 惹我定时发送，路虎' \
           '而且我去问，路虎ww且惹我qqqfdsfsfs \n  ss'
    print(str2)
    print(str2.replace('路虎', '卢虎', 2))   # 默认全部替换,定义之后从左到右修改指定个数
    print(str2.strip())   # 去除首尾空格和换行符,制表符 \n  \t
    print(str2.strip('ss'))   # 去除首尾指定字符


def my_split():
    """
    分隔操作
    :return:
    """
    str = ':haha:xiaomin:jane:hulu'
    print(str.split(':', 2))  # 将前两个分隔开，默认全部分开，str  ----> list


def my_str_join():
    """
    连结操作
    :return:
    """
    str = 'hulu'   # 可迭代的对象才可以使用join
    str2 = '+'.join(str)
    print(str2)
    str3 = ['hulu', 'haha', 'xiaoming']    # list -----> str
    str4 = ':'.join(str3)
    print(str4)


def my_count():
    str = 'adsfdasdqerqwadasfs243afafdsa'
    count = str.count('a')
    print(count)


def my_format():
    str = '我叫{},今年{}岁，性别{},明年依然叫{}'.format('路虎', 21, '男', '路虎')
    str2 = '我叫{0},今年{1}岁，性别{2},明年依然叫{0}'.format('路虎', 21, '男')  # 可以使用后面字符对应的索引
    str3 = '我叫{name},今年{age}岁，性别{sex},明年依然叫{name}'.format(name='路虎', sex='男', age=21)  # 也可以在前面指定变量

    print(str3)


def my_is():
    str = 'wewrqe'
    str1 = '123qwq w'
    print(str1.isalnum())   # 是否全为字母或数字或两者的组合
    print(str1.isalpha())   # 是否全为字母
    print(str1.isdecimal())  # 是否为十进制，数字


def my_for():
    """
    for有限循环，for else用法同while，使用break不执行else
    :return:
    """
    str = 'hahwe好rwrwr'
    for i in str:
        if i == '好':
            break
        print(i)
    print('zhi:', i)

    # j = 0
    # while j < len(str):
    #     print(str[j])
    #     j += 1


def str_to_list():
    """
    list的增删查改
    append在列表末尾添加对象，无返回值
    extend在列表末尾一次性追加另一个序列的多个值（组成对象的最小元素）,如果是字符串就迭代着添加单个字符，无返回值
    insert在列表指定位置插入数据，同样无返回值
    pop在列表指定位置删除数据，默认最后一位，支持倒序删除，返回值为被删除的元素
    remove删除指定元素，如果重名就删左起第一个,无返回值
    del按索引删，按切片删(支持步长)
    :return:
    """
    # str1 = list('242343242342342')
    # print(str1)
    str1 = ['aa', 'bb', 'cc']
    # str2 = str1.append('ee')   这种写法是错的
    str1.append('ee')
    str1.extend(['ff', 'kk'])
    str1.extend(['ll'])
    str1.extend('ll')
    str1.insert(2, 'luhu')   # 按索引插入数据
    str1.insert(23, 'luhu4')
    s = str1.pop(-1)
    s = str1.pop(5)
    str1.remove('aa')   # 删除指定元素，如果重名就删左起第一个
    # str1.clear()    # 清空列表，无返回值
    print(str1)
    # del str1[2]
    # del str1[:2]   # 从第0位往后隔一位删除
    # del str1[-1:-5:-2]
    # str1[::2] = 'abcd'   # 将str1中不显示的位置迭代换成右边对象的最小元素,位置要一一对应
    str1[1:4] = 'absfdsf'  # 不加步长，就将str1中的1-3位换成右边对象的最小元素，
    print(str1)


def list_nesting():
    str1 = [1, 2, 'asd', 'ee', [1, 2, 'luhu']]
    str1[4][2] = str1[4][2].upper()
    print(str1)


def my_tuple():
    """
    元组，只读列表，切片（加步长），索引，存储大量数据,单列表中的对象的最小单位可以修改，但不能被删除
    :return:
    """
    t = (1, 2, 'qwq', [1, 2, 'err'])
    print(t[2])
    print(t[::2])
    print(len(t))
    t[3][2] = t[3][2].upper()
    # del t[2]
    del t[3][1]
    print(t)
    a, b, c, d = t    # 元组的拆包
    print(a, b, c, d)


def my_range():
    """
    类似于列表，数字范围的列表
    :return:
    """
    r = range(4, 10, 2)
    r = range(10)
    r = range(100, 10, -1)
    print(r)
    # print(r[2])     # range支持索引，r中的第3个元素
    for i in r:
        print(i)


def my_range2():
    l1 = [1, 2, 'ww', 'er', 9]
    for i in range(len(l1)):
        print(i)


def my_range3():
    r = range(0, 5)
    print(r[1:3])


def my_range4():
    r = range(5, 1, -1)
    for i in r:
        print(i)


def my_split1():
    str = input('请输入两个数相加：')
    r = str.split('+')
    result = 0
    for i in r:
        result = int(i) + result
    print(result)


def my_str():
    str = input('请输入字符串：')
    dict1 = []
    j = 0
    for i in str:
        if i.isdecimal():
            j += 1
            dict1.append(i)
    print(dict1, j)


def my_for1():
    str = range(1, 100)
    sum = 0
    for i in str:
        if i == 88:
            continue
        elif i % 2 == 0:
           sum = sum - i
        else:
            sum = sum + i
    print(sum)


def is_palindrome():   # 判断是不是水仙花数
    str = '1上海自来水来自海上1'
    str1 = str[-1::-1]
    if str == str1:
        print('it is palindrome')
    else:
        print(str1)
        print('it is not palindrome')


def my_join():
    list1 = ['haha', 'is', 'true', 2]
    # str1 = '_'.join(list1)
    # print(str1)
    re = list1[0]
    for i in range(1, len(list1)):
        re = re + '_' + str(list1[i])
    print(re)


def my_list1():
    list1 = []
    for i in range(100, 10, -1):
        if i % 4 == 0:
            list1.append(i)
    print(list1)


def minganci():
    list1 = ['hi', 'dog', 'is']
    str = 'hi,i am lilei, it is my dog！！！'
    for i in list1:
        print(i)
        if i in str:    # i为敏感词
            x = str.rfind(i)   # 寻找敏感词索引
            print(x, i)
            list1 = list(str)
            for j in range(x, x+len(i)):     # 遍历敏感词替换
                list1[j] = '*'
            str = ''.join(list1)
    print(str)


def minganci2():
    list1 = ['hi', 'dog', 'is']
    str = 'hi,i am lilei, it is my dog!!!'
    for i in list1:
        temp = ''
        str = str.replace(i, "*"*len(i))
    print(str)


def list_xunhuan():
    li = ["Taibai", 'alexC ', ' ABcdFC ', 'luHu ', "wuSir", ' Akikc']
    li1 = []
    for i in li:
        i = i.strip()
        if i.lower().startswith('a') and i.lower().endswith('c'):
            li1.append(i)
    print(li1)
    print(li)


def xunhuan_dayin():
    li = [1, 2, 3, [2, 'we', 45], 3]
    for i in range(len(li)):
        if type(li[i]) == list:
            for j in range(len(li[i])):
                print(li[i][j])

        else: print(li[i])


def my_dict():
    """
    数据类型的分类（可变与不可变）：
    可变不可哈希：list dict set
    不可变可哈希：str bool int tuple
    键值对，键必须为不可变数据类型，值可以为任意数据类型或对象
    字典在3.5版本之前时无序的，3.6之后按初次建立字典的顺序排列，3.7之后是有序的
    字典的缺点是以空间换时间，字典查询数据很快
    :return:
    字典的创建方式及增删查改
    dict1 = dict([(1,'ww'),(2,'ee')])
    dict1 = dict(key1=1,key2=2)
    dict1 = dict.fromkeys(iterable,value)
    dict1 = dict1.update()
    字典推导式
    """
    dict1 = dict((('ee', 4), ('dff', 2), ('po', 65), ('wew', 2)))    # 元组的拆包
    dict2 = dict(a=1, b=4, c=7)
    dict3 = dict({'a': 2, 'b': 9, 'c': [1, 2, 3, 'trtr']})
    dict4 = {'a': 2, 'b': 9}
    dict4['haha'] = 5     # 有则改无则加
    dict4.setdefault('hahf', 555)  # 有则不动，无则加，默认加None
    dict4.pop('a')     # 按照键删除键值对
    dict4.pop('c', '没有此键')   # 没有此键返回后面信息
    # dict4.clear()    # 内容清空
    # del dict4['b']
    d = dict3.get('y', '没有此键')     # 按键查值，没有返回后面的信息，默认None
    # print(list(dict3.keys()))      # 获取字典所有的键，类型为dict_keys
    # print(list(dict3.values()))    # 获取字典所有的值，类型为dict_value，可迭代，可转换数据类型
    for key, value in dict3.items():
        print('key=', key, 'value=', value)   # 元组的拆包


def dict_demo():
    dict1 = {
        'xiaoming': {
            'aaa': ['我', 'is', 'hi'],
            'bbb': ['was', 'hello', 'pic']
        },
        'lilei': {
            'zhang': ['li', 'lu', 'wang'],
            'java': ['we', 'ella', 'piao']
        }
    }

    dict1.setdefault('luhu', {"go": ['ll', 'kk']})
    dict1['xiaoming'] = {
            'aaa': ['我888', 'is', 'hi'],
            'bbb': ['was', 'hello', 'pic'],
            'ccc': [1, 2, 3]
        }
    print(dict1['xiaoming']['aaa'].insert(0, 'insert'))
    print(dict1)


def dict_demo2():
    dict2 = {}
    str = ' k:0|k1 :1|k2 :2|k3 :3|k4:4|k5:5|k6:6'
    for i in str.split('|'):
        key, value = i.split(':')
        dict2[key.strip()] = int(value)
    print(dict2)


def dengyu_is_demo():
    """
    id相同值一定相同，值相同，id不一定相同
    :return:
    """
    l1 = [1, 2, 3, 4]
    l2 = [1, 2, 3, 4]
    l3 = l1
    print(l1 == l2)    # 比较变量的数值是否相同
    print(l1 is l3)    # 比较变量的地址是否相同
    print(id(l1))      # 获取变量的地址



str1 = '1000'
str2 = '1000'
"""
同一代码块缓存机制：同一代码块下，申明变量先检查内存中是否创建该数据
优点：节省内存，提升性能
适用变量：str bool int
适用细则：几乎所用的str 所有的bool，所有的int
"""
# print(str is str1)
# print(id(str), id(str1))


"""
不同代码块的缓存机制：不同代码块下，申明变量先检查内存中是否创建该数据，不过数据范围变小了
适用变量：str bool int
适用细则：一定规则的str 所有的bool，-5~256的int
"""
str1 = 257
str2 = 257
# print(str1 is str2)     # 在交互式命令行中执行，结果为false


def my_set():
    """
    set 集合，集合是无序的，一个集合中不会出现重复的元素，集合中的元素不可变，可哈希
    集合的增删改,交并差集，反交集，子集，超集
    增：add, update 迭代着增加
    删：remove 删除指定元素，pop 随机删除
    改：变相改，先删后改
    交集& 并集|
    :return:
    """
    set1 = set({1, 2, 'aa', False, 'vv', '12'})
    # print(set1)
    set2 = {1, 4, 8, 'gg', 2}
    set3 = {'1', '1', 12, 'ewe'}    # set的正确性校验，里面不可放可变数据类型
    set4 = {1, 2}
    # print(set3)
    print(set1 & set2)   # 交集
    print(set1 | set2)   # 并集
    print(set1 - set2)   # 差集，set1中有set2中没有的
    print(set1 ^ set2)   # 除了两个共有的其他元素
    print(set4 < set1)   # 判断set4是不是set1的子集
    print(set1 > set4)   # 判断set1是不是set4的超集


def list_quchong():
    """
    通过集合的特性给列表去重
    :return:
    """
    li = [1, 1, 2, 3, 3, 4, 4, 'aa', 'aa']
    set1 = set(li)
    li = list(set1)
    print(li)


def copy_demo():
    """
    浅拷贝：只拷贝外壳，不拷贝里面的东西，在内存中开辟新空间去存放copy的对象（列表，字典），里面所有的元素和copy的对象共用同一个
    深拷贝：将可变的数据类型在内存中重新创建一份，不可变的数据类就沿用之前的
    :return:
    """
    li = [1, 2, '33', 'adf', [1, 2, 'aa']]
    li2 = li.copy()
    li3 = copy.deepcopy(li)
    li[4].append('oppo')
    li[0] = 9
    print(li)
    print('浅拷贝', li2)
    print('深拷贝', li3)
    li[0] = 90


def copy_demo2():
    """
    说明切片是浅拷贝，可变数据类型共用一个
    :return:
    """
    li = [1, 2, 3, [1, 2, 'ee', 3]]
    li2 = li[:]
    li[-1].append('aa')
    print(li)
    print(li2)


def gouwu_demo():
    goods = [
        {"name": "主机", "price": 1999},
        {"name": "鼠标", "price": 30},
        {"name": "键盘", "price": 20},
        {"name": "显示器", "price": 300}
    ]

    while 1:
        for i, j in enumerate(goods):   # enumerate 返回有列表索引和索引对应的值组成的元组（（0，{"name": "主机", "price": 1999}），（1，{"name": "主机", "price": 1999}））
            print('{}\t{}\t{}'.format(i + 1, j["name"], j["price"]))
        input1 = input('请输入编号:')
        if input1.isdecimal():
            if 0 < int(input1) < len(goods)+1:
                print(goods[int(input1)-1]["name"], goods[int(input1)-1]["price"])
                break
            else:
                print("输入编号超出范围，请重新输入！！！")
        elif input1.upper() == "Q":
            print("退出程序！")
            break
        else:
            print('输入有误,请重新输入')


def mima_demo():
    li = []
    while 1:
        name = input('请输入用户名>>>')
        if name.lower() == 'n': break
        password = input('请输入密码>>>')
        dic1 = {"name": name, "password": password}
        li.append(dic1)
    print(li)


def lianxi1():
    # info = [1, 2, 3]
    info = 'aa'
    userinfo = [info, info, info]
    # info[0] = 'dd'
    info = 'vv'
    print(userinfo)


def lianxi2():
    """
    data创建在循环外，会出现重复的i，因为每次循环都将i的地址指向最新的i
    :return:
    """
    # data = {}
    data_list = []
    for i in range(10):
        data = {}
        data['user'] = i
        data_list.append(data)
    print(data_list)


def lianxi3():
    for i in range(10):
        if i % 2 == 1:
            print(i*'*')


def qiao7():
    li = []
    for i in range(1, 100):
        if i % 7 == 0:
            li.append('咣')

        else:
            li.append(i)
    print(li)


def str_kuochong():
    """
    str方法的扩充
    capitalize   首字母大写其余变小写
    swapcase     大小写翻转
    center       居中对齐，总长度为int填充默认空格
    find         根据元素找第一个索引,找不到返回-1
    index        根据元素找第一个索引,找不到报错
    :return:
    """
    str1 = 'heLLoLuhu'
    print(str1.capitalize())
    print(str1.swapcase())
    print(str1.center(50, '*'))
    print(str1.find('u'))


def tuple_kuozhan():
    """
    tuple的扩展
    count 计数某一元素出现的次数
    index 根据元素返回第一个的位置，没有就报错
    :return:
    """
    tu1 = (1, 1, 2, 3, 4, 4, 4, 6, 7)
    print(tu1.count(2))
    print(tu1.index(4))


def list_kuozhan():
    """
    list的扩展
    index
    count
    sort 默认从小到大排，字母按首字母asc码从小到大排,不返回值
    sort(reverse=True)  从大到小排
    reverse 将列表翻转过来
    列表相加相乘  + *
    :return:
    """
    li = [1, 2, 6, 7, 4, 9, 11]
    li2 = [2, 4, 3, 1, 10, 9]
    li.sort()
    print(li)
    print(li2*2)
    print(li+li2)


def list_delete():
    """
    删除索引为奇数对应的值,不要再列表循环的时候删除元素，否则会影响结果
    :return:
    """
    li = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    # del li[1::2]
    # for i in range(len(li)-1, -1, -1):    # 倒叙删除，删除之后不会影响前面的索引
    #     if i % 2 ==1:
    #         li.pop(i)
    li2 = []
    for i in range(len(li)):
        if i % 2 == 0:
            print(li[i])
            li2.append(li[i])
    print(li2)


def dict_kuozhan():
    """
    dict 的扩展
    update()     有则改无则新增  update(key=value),update(dict)
    get(key,default)  获取键对应的值，没有就创建该键并将default的值赋给该键
    dict.fromkeys(iterable,value)   创建一个新的字典，将同一个值赋值给keys这个可迭代对象，缺点不同的键指向同一个对象，对象值改变，dict所有的值一起改变
    字典在循环的时候不可删除，否则会报错
    :return:
    """
    dict1 = {'key': 1213, 'key1': 'ert', 'key2': 999, 'aa': 'lll', 'key4': '1212'}
    for i in list(dict1.keys()):
        if 'k' in i:
            dict1.pop(i)
    print(dict1)


def dict_update():
    dict1 = {'a': 12}
    dict2 = {'ee': 98, 'uu': 90}
    dict1.update((('ww', 2), ('qq', 4)))
    dict1.update(hobby='play')
    dict1.update(dict2)
    print(dict1.fromkeys(['e', 'v', 'l'], 'haha'))   # fromkeys会创建一个新的字典，操作完之后记得将新字典指给原来的变量
    print(dict.fromkeys(['e', 'v', 'l'], 'haha'))    # 这种方式更易于理解
    print(dict1)


def dict_kuozhan2():
    dict1 = {'key': 1213, 'key1': 'ert', 'key2': 999, 'aa': 'lll', 'key4': '1212'}
    li = []
    for i in dict1.keys():
        li.append(i)
    print(li)
    for k in li:
        if 'k' in k:
            dict1.pop(k)
    print(dict1)
    # print(type(dict1.keys()))


def my_bytes():
    """
    str 文字文本，  bytes 字节文本
    数据在内存中全部是以Unicode编码的
    但是当数据用于网络传输或存到硬盘中，必须是以非Unicode编码（utf-8，gbk）
    数据类型：bytes   与字符串很像，在内存中非Unicode编码
    bytes数据类型可以直接用于网络的传输
    :return:
    """
    by = b'ff'
    str = '你好'   # str在内存中是Unicode编码
    by1 = b'\xc4\xe3\xba\xc3'
    by2 = by1.decode('gbk')
    by3 = by2.encode('utf-8')   # 用啥编码就用啥解码,变成Unicode的
    by33 = by.decode('utf-8')
    print(str.encode('gbk'))
    print(by2)
    print(by3)
    print(by33)


def dict_list_lianxi():
    v2 = {}
    v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for item in v1:
        if item < 6:
            print(item)
            continue
        if 'k1' in v2:
            v2['k1'].append(item)
        else:
            v2['k1'] = [item, ]
    print(v2)


def copy_lianxi():
    s1 = 'fdfdf'
    s4 = 'fdfdf'
    s2 = copy.copy(s1)
    s3 = copy.deepcopy(s1)
    l1 = [1, 2, 3, [1, 4], 6]
    l4 = [1, 2, 3, 4, 6]
    l2 = copy.copy(l1)
    l3 = copy.deepcopy(l1)
    l1[3][1] = 'e'
    l1[1] = 'e'
    print(l2)
    print(s1 is s4)
    print(s1 is s3)
    print(l1[3] is l2[3])
    print(l1 is l2)
    print(l1 is l3)


def copy_lianxi2():
    v1 = [1, 2, 3, {'name': 'jane', 'number': [7, 77, 88]}, 4, 5]
    v2 = copy.copy(v1)
    # print(v1[3] is v2[3])
    print(v1[3]['number']is v2[3]['number'])


def open_file():
    """
    file_handler约定俗成名称叫文件句柄，对文件的操作都要通过文件句柄
    encoding 可以不写，默认操作系统的默认编码
    mode 默认只读模式打开 rt
    t --> text   单位t, b
    b --> binary
    a --> append 追加
    w --> write   读写方向 w,r
    r --> read
    r 只读文本
    r+ 先读光标到结尾并追加写
    rb 非文本      r+b
    w 写,没有该文件会自动创建文件
    wb 非文本写
    w+ 写读   w+b
    windows: gbk
    linux mac: utf-8
    flush   强制刷新，保存
    :return:
    """
    # file_handler = open('D:\Downloads\\test.txt', encoding='utf-8', mode='r')
    file_handler = open('/Users/hulu/Desktop/test/test.txt', mode='r+')
    file_handler.read()
    file_handler.write('luhu,xaioming，零零落落')
    file_handler.flush()
    print(file_handler.read())
    # file_handler = open('/Users/hulu/Desktop/test/test2.txt', mode='w')

    # file_handler2 = open('D:\Downloads\\test1.txt', encoding='gbk')
    # content = file_handler.read()
    # content = file_handler.read(5)   # 读取前5个字符
    # content = file_handler.readline(2)   # 读取第一行的前2个字符
    # content = file_handler.readlines()   # 读取多行，返回的是每行的列表
    # print(content)
    # 但这几种读取文件方式不好，一次加载所有数据到内存，数据多的话会撑爆内存
    # for line in file_handler:   # 这种读取方式最合理，每次只加载一行到内存，用一次丢一次
    #     print(line)

    # file_handler.write('luhu,hahah')
    file_handler.close()    # 关闭文件，否则一直打开占用内存


def tell_file():
    file_handler = open('/Users/hulu/Desktop/test/test3.txt', encoding='utf-8', mode='r')
    file_handler.read()
    print(file_handler.tell())    # 先读光标定位到最后，告诉这个文本有多少个字节
    file_handler.close()


def seek_file():
    file_handler = open('/Users/hulu/Desktop/test/test3.txt')
    print(file_handler.seek(1))  # 先读光标定位到指定位置，然后读取的是光标之后的内容
    print(file_handler.read())
    file_handler.close()


def open_file2():
    """
    文件的另一种打开方式：
    优点 不需要手动关闭文件，可以同时打开多个文件
    :return:
    """
    with open('/Users/hulu/Desktop/test/test3.txt', encoding='utf-8') as f1,\
            open('/Users/hulu/Desktop/test/test2.txt')as f2:
        print(f1.read())
        print(f2.read())


def file_demo():
    with open('test.txt') as f1, open('test.bak', mode='w') as f2:
        for line in f1:
            new_content = line.replace('luhu', 'LUHU')
            f2.write(new_content)
        # content = f1.read()     # 使用read不好，数据多会爆内存
        # new_content = content.replace('luhu', 'LUHU')
        # f2.write(new_content)
        os.remove('test.txt')
        os.rename('test.bak', 'test.txt')


def shuixianhua():
    while 1:
        str1 = input('请输入一个数字：')
        if str1.isdecimal():
            # tem = str(str1)
            print(len(str1))
            res = 0
            for i in str1:
                res += int(i)**3
                print(res)
            if res == int(str1):
                print('是水仙花数')
                break
            else:
                print('不是水仙花数')

        else:
            print('输入的不是数字')


def chepai_dic_list():
    cars = ['鲁A34545', '沪B43445', '黑C32333', '沪A2323323', '鲁A3423434', '沪N343543434', '京A23224', '沪A1243242', '皖M434e3423']
    locals = {'鲁': '山东', '皖': '安徽', '沪': '上海', '黑': '黑龙江', '京': '北京', '湘': '湖南'}
    # car_num = {}
    # for local in locals.keys():
    #     count = 0
    #     for car in cars:
    #         if local in car:
    #             count += 1
    #     car_num[local] = count
    # car_local = {}
    # for key in car_num.keys():
    #     # print(key)
    #     car_local[locals[key]] = car_num[key]
    # print(car_local)
    # dict1 = {}
    # for car in cars:
    #     if locals[car[0]] not in dict1:
    #         dict1[locals[car[0]]] = 1
    #     else:
    #         dict1[locals[car[0]]] += 1
    # print(dict1)
    dict2 = {}
    for car in cars:
        dict2[locals[car[0]]] = dict2.get(locals[car[0]], 0) + 1  # 将值赋值给键，没有就赋值为0
    print(dict2)


def file_dict():
    li1 = []
    li3 = ['name', 'price', 'amount']
    with open('test.txt') as f1:
        for line in f1:
            li2 = line.strip().split(' ')
            dict1 = {}
            for i in range(len(li3)):
                dict1[li3[i]] = li2[i]
            li1.append(dict1)
        f1.close()
    print(li1)


def file_dict1():
    with open('test.txt') as f1:
        li1 = []
        for line in f1:
            dict1 = {}
            dict1['name'], dict1['price'], dict1['amount'] = line.strip().split(' ')
            li1.append(dict1)
        f1.close()
    print(li1)


def my_hanshu():
    """
    函数返回多个值时，会被处理成元组tuple返回
    :return:
    """
    print('test')
    return 'kk', [1, 2, 3], 3


def canshu(a, b):
    """
    形参，实参
    实参：
    1. 位置参数，从左到右一一对应
    2. 关键字参数，调用方法时使用形参，传错顺序也没关系   canshu(a=1, b=1),但是一定要放在位置参数之后
    3. 混合参数，关键字参数一定要在位置参数后面，否则会报错
    4. 默认参数，在方法名中指定默认值，默认参数可以不传，也可以按位置参数使用，使用关键字参数时，一定要放在位置参数之后
    形参：
    1. 位置参数，从左到右一一对应
    2. 默认参数，可以不传使用默认值，如果修改必须使用default_key=key这种形式,且放在位置参数之后
    :return:
    """
    c = (a if a > b else b)     # 三元运算符对if else的简写,括号不用写，方便阅读理解
    print(c)


def canshu2(age, sex, hight, weight):
    """
    canshu2(21, '女',hight=172, weight=55)    混合参数，关键字参数一定要在位置参数后面，否则会报错
    :param age:
    :param sex:
    :param hight:
    :param weight:
    :return:
    """
    return '筛选结果：年龄%s，性别%s，身高%s，体重%s' % (age, sex, hight, weight)


def canshu3(l):
    c = l[:2] if len(l) > 2 else l
    return c


def canshu4(age, hight, weight, sex='男'):
    return '筛选结果：年龄%s，性别%s，身高%s，体重%s' % (age, sex, hight, weight)


def canshu5(*args):
    """
    形参：
    动态接收位置参数 *args,约定俗成叫args
    * 代表聚合，它将所有位置参数聚合成一个元组赋值给args
    动态接收关键字参数 **kwargs，它将所有的关键字参数聚合成一个字典赋值给kwargs
    :param args:
    :return:
    """
    print('请你吃， %s %s %s' % args)


def wannengcanshu(*args):
    count = 0
    for i in args:
        count = count + i
    print(count)


def wannengcanshu2(name, age, *args, sex='male'):
    """
    当函数中出现位置参数，默认参数，动态接收位置参数（万能形参）时，将默认参数指定在最后，通过关键字参数调用传参
    :param name:
    :param age:
    :param args:
    :param sex:
    :return:
    """
    print(args)
    print(sex)
    # wannengcanshu2(1, 3, 6, 9, 11, sex='nv')


def wannengcanshu3(name, age, *args, c, sex='nan', **kwargs):
    """
    当函数中出现位置参数，动态接收位置参数，动态接收关键字参数，默认参数时，默认参数放在动态接收位置参数和动态接收关键字参数之间，
    动态接收关键字参数放最后，放在动态接收位置参数和动态接收关键字参数之间的位置参数叫仅限关键字参数，该参数必须通过关键字参数调用，必传默认参数和仅限
    关键字参数在调用时位置可以随便放，不会被动态接收关键字参数聚合到字典里
    :param name:
    :param age:
    :param args:
    :param sex:
    :param kwargs:
    :return:
    """
    print(sex)
    print(c)
    print(args, kwargs)
    # wannengcanshu3(1, 3, 6, 9, 11, sex1='nv', c='a', dic1=1, sex='9', dic2=2, dic3=3)


def wannengcanshu4(*args, **kwargs):
    """
    * 或**相当于打散
    :param args:
    :return:
    """
    print(args)
    print(kwargs)
# wannengcanshu4({1, 3, 2}, [1, 2],**{'k1':'ff'})


input = '路虎'   # hanshu5的全局变量
count = 0       # hanshu5的全局变量


def hanshu5():
    """
    取值顺序，就近原则，局部方法就从局部使用，然后取全局的，最后去内置的找
    LEGB原则：local enclosed(嵌套函数，父级) global build_in
    作用域：
    内置名称命空间：存放的是内置函数
    全局名称空间：py文件，存放的是py文件（除去函数，类内部的）的变量，函数名与函数在内存中地址的关系
    局部名称空间：存放的函数内部的变量与值的对应关系
    全局作用域：内置名称命名空间，全局名称命名空间
    局部作用域：局部名称命名空间
    局部作用域可以引用全局作用域的变量，不可以改变全局作用域的变量
    :return:
    """
    input = 'luhu'  # enclosed 父级的局部变量

    def func():
        print(input)
    # count += 1    # 当python解释器读取到局部作用域时，发现你对一个变量进行修改，
                    # 解释器会认为你已经创建了一个局部变量，它就从局部找这个局部变量，就报错了
    func()
    print(input)


# print(input)    # hanshu5的全局变量无法获取局部变量input的值

# wannengcanshu4(*[1, 2, 3], *[4, 5, 6])   # 相当于[1, 2, 3, 4, 5, 6]
# wannengcanshu4(**{'name': 'luhu'})
# wannengcanshu4({'name': 'luhu'}, {'age': '23'})
# wannengcanshu4(**{'name': 'luhu'}, **{'age': '23'})


def zuoyongyu():
    name = 'luhu'
    age = 12
    print(globals())      # 返回的是全局作用域的所有内容地址组成的字典
    print(locals())       # 返回的是局部作用域的所有内容地址组成的字典


# a = 10
# b = 20


# def test3(a, b):
#     print(a, b)
#
#
# c = test3(b, a)
# print(c)

# a = 10
# b = 20
#
#
# def test4(a, b):
#     a = 3
#     b = 5
#     print(a, b)
#
#
# c = test4(b, a)
# print(c)


def morencanshu(a, list=[]):
    """
    默认参数的坑，当默认参数指向的是可变参数类型时，那么无论你调多少次这个默认参数，它的地址都指向同一个
    当调用完函数后，函数的在内存中被清空，但可变参数不被清空，且地址不变
    :param a:
    :param list:
    :return:
    """
    list.append(a)
    return list


# print(morencanshu('ll'))    #['ll',]
# print(morencanshu('123', []))     # ['123',]
# print(morencanshu('hh'))    #   ['ll', ''hh']

# ret1 = morencanshu('ll')
# ret2 = morencanshu('123', [])
# ret3 = morencanshu('hh')    # 执行完再打印ret1,ret3指向的是同一个列表,通过id函数可以看出两个指向的是同一个地址
# print(ret1, id(ret1))   # ['ll', ''hh']
# print(ret2)   # ['123',]
# print(ret3, id(ret3))   # ['ll', ''hh']


# a = 2
# def jububianliang_keng():
#     """
#     局部变量的坑，会报错，在引用前未定义局部变量
#     :return:
#     """
#     print(a)
#     a = 4

# name = 'fff'
# def jubu_quanju():
#     """
#     将局部变量声明为全局变量，只有在该函数被调用时，全局变量才生效
#     :return:
#     """
#     global name
#     name = 'luhu'
#     print(name)
#
# # print(name)   # 会报错
# jubu_quanju()
# print(name)   # 不会报错，调用函数后，全局变量生效，就近原则打印luhu


# count = 1
# def quanju_yinyong():
#     """
#     global应用，修改全局变量
#     :return:
#     """
#     global count
#     count += 1
# print(count)
# quanju_yinyong()
# print(count)


def my_nonlocal():
    """
    nonlocal
    1. 不能操作全局变量，
    2. 局部作用域：用于操作内层函数对外层函数中局部变量的修改（高阶函数）
    :return:
    """
    count = 1

    def inner():
        nonlocal count
        count += 1
        print('inner', count)
    print('outer', count)   # 还没调用内层函数
    inner()
    print('outer_after', count)


def func():
    """
    函数名其实也是一个变量
    函数名可以作为容器类数据类型的元素
    函数名可以作为函数的参数
    :return:
    """
    print('in func')


def func1():
    print('in func1')


def func3(x):
    x()
    print('in func3')


def func4(x):
    print('in func4')
    return x

# func1 = func
# func1()   # 会打印in func而不是func1
# ff  = [func, func1]    # 函数名可以作为容器类数据类型的元素
# for i in ff:
#     i()
# func3(func)   # 函数名可以作为函数的参数
# f = func4(func)    # 结果就是return了func，f=func
# f()


def geshihua():
    """
    新特性，格式化输出
    相对于之前的format，%s 结构更简化，可以结合表达式，函数使用，效率更高
    f'{}'括号里可以放字符串，字典，列表,表达式,函数
    :return:
    """
    name = 'luhu'
    age = 23
    dict1 = {"name": "路虎", "age": 22}
    li1 = ['陆虎', 23]
    msg = f'我叫{name}, 今年{age}岁'
    msg1 = f'我叫{dict1["name"]}，今年{dict1["age"]}岁'
    msg2 = f'我叫{li1[0].upper()}，今年{li1[1]}岁'
    print(msg)
    print(msg1)
    print(msg2)


def my_iterable():
    """
    可迭代的：更新迭代，可以重复循环的一个过程，更新迭代每次都有新的内容，可以循环更新的实实在在的一个值
            内部含有__iter__方法的对象就是可迭代对象
    可迭代的对象常见： str,list,tuple,set,dict,range，文件句柄
    可迭代对象的优点：储存的数据直接显示，直观，拥有的方法多，操作方便
             缺点：占用内存，不能直接通过for循环直接取值（索引，key），要通过迭代器，（list是通过for循环加自有操作方法取值）
    dir()获取这个对象的方法，返回一个列表
    :return:
    """
    li1 = [1, 2, 3]
    print(dir(li1))


def my_iterator():
    """
    迭代器，可更新迭代的工具，内部含有__iter__和__next__方法的就是迭代器
    文件句柄就是迭代器
    使用iter和next方法将可迭代对象转化成迭代器
    优点:节约内存；惰性机制，next一次取一个值，绝不多取
    缺点；速度慢；查看数据不直观；取值不走回头路，只能一直向下走
    :return:
    """
    str = 'dfsaf242342fsafdsa'
    obj = iter(str)    # 或使用obj.__iter__()'
    print(next(obj))   # 或使用print(obj.__next__())
    print(next(obj))


def my_iterator2():
    """
    用while实现for循环
    :return:
    """
    l2 = [1, 2, 3, 5, 6, 7, 8, 9]
    l3 = iter(l2)
    while 1:
        try:
            print(l3.__next__())
        except StopIteration:
            break


def func11():
    print('in func11')
def func22(x):
    print('in func22')
    return x
def func33(y):
    print('in func33')
    return y
# ret = func22(func11)    # 调用func22方法打印in func22，返回'func11'
# ret()                   # func11（），打印in func11
# ret2 = func33(func22)    # 调用func33方法打印in func33，返回'func22'
# ret3 = ret2(func11)      # func22(func11)，打印in func22，返回'func11'
# ret3()                   # 打印in func11


def test3():
    for i in range(10):
        pass
    print(i)

ll = []


def test4(args):
    ll.append(args)
    return ll  # 将全局变量的值修改了
# print(test4(1))
# print(test4(2))
# print(test4(3))


def cal(str):
    count = 1
    # for i in range(1, str+1):
    for i in range(str, 0, -1):
        count = i*count
    print(count)


def chenfa():
    for i in range(1, 10):
        for j in range(1, i+1):
            print(str(j)+'*'+str(i)+'=' + str(i * j), end=' ')
        print('\n')


def my_yield():
    """
    生成器，本质就是迭代器，区别在于，生成器是自己用python代码构建的数据结构，迭代器是python提供的，或者转化得来的
    获取生成器的方法：生成器函数;生成器表达式;python内部提供的
    return 函数只存在一个return 结束函数，并且给函数的执行者返回值
    yield 只要函数中有yield那么他就是生成器函数，不会返回值，不是函数了，生成器函数中可以存在多个yield，yield不会结束生成器函数，一个yield对应一个next
    生成器相当于自己构建的一个数据集
    :return:
    """
    print('11')
    yield 4
    yield 5
# my = my_yield()
# print(next(my))
# print(next(my))


def my_yeild2():
    for i in range(1, 201):
        yield f'第{i}个包子好了！！'
# ret = my_yeild2()
# for i in range(1, 11):   # 惰性机制，没有结束生成器函数
#     print(next(ret))
# for i in range(1, 11):
#     print(next(ret))


def my_yield_from():
    ll = [1, 2, 3, 5, 6, 7]
    ll2 = [8, 9, 10, 11, 12, 13, 14]
    yield from ll     # 将ll变成一个迭代器，依次取里面的元素
    yield from ll2
# my = my_yield_from()
# for i in range(13):
#     print(next(my))   # 先将ll循环完，再循环ll2


def liebiaotuidaoshi():
    """
    列表推导式：用一行代码构建一个比较复杂有规律的列表
    循环模式： [变量（加工后的变量） for 变量 in iterable]
    筛选模式：[变量（加工之后的变量） for 变量 in iterable if 条件]
    :return:
    """
    li = [i for i in range(1, 11)]
    li2 = [i for i in range(1, 101) if i % 2 == 0]
    li3 = [i**2 for i in range(1, 11)]
    li4 = [f'python{i}期' for i in range(1, 101)]
    names = [['ddd', 'luhu', 'luhu1', 'luhu2', 'lele', 'lee'], ['jenney', 'elle', 'fdf', 'klk']]
    li5 = [name for i in names for name in i if name.count('e') == 2]
    dict1 = ['jay', 'jj', 'meet']
    dict2 = ['周杰伦', '林俊杰', '元宝']
    dict12 = {dict1[i]: dict2[i] for i in range(len(dict1))}   # 同理，字典推导式
    print(dict12)


def shengchengqi():
    """
    生成器表达式，思想同列表推导式一模一样，只不过不方括号改成小括号，
    优点，节约内存
    与列表推导式本质上的区别：列表推导式是可迭代对象，生成器表达式是迭代器
    :return:
    """
    names = [['ddd', 'luhu', 'luhu1', 'luhu2', 'lele', 'lee'], ['jenney', 'elle', 'fdf', 'klk']]
    li5 = (name for i in names for name in i if name.count('e') == 2)
    print(next(li5))
    print(next(li5))


def neizhihanshu():
    """
    内置函数
    eval        剥去字符串的外衣，运算里面的代码,会有中毒的风险，在网络传输中会被黑客截取替换成病毒，执行eval会中毒
    exec        与eval相似，代码流，执行代码
    hash        不可变数据类型才有此方法，获取该值的哈希值
    help        获取该函数的帮助用法
    callable    判断一个函数是否可被调用
    int         将字符串转化成整数，将小数转化成整数(不是四舍五入，直接去除小数)，将二进制转化成10进制
    complex(x,j) 将传入的值转化成复数
    float       将数值转化成小数
    bin         将十进制转化成二进制
    oct         将十进制转化成八进制
    hex         将十进制转化成十六进制
    divmod      计算除数与被除数的结果，返回一个包含商和余数的元组
    round       保留浮点数的小数位数，默认保留整数
    pow         求x**y次幂（三个参数为x**y的结果对z取余）
    bytes       用于不同编码之间的转化
    ord         输入字符找该字符编码的位置
    chr         输入位置数字找出其对应的字符
    repr        返回一个对象的string形式
    all         判断一个可迭代对象里面全都是真，返回true
    any         判断一个可迭代对象里面又一个是真，就返回true
    abs         返回绝对值
    sum         求和
    reversed    将一个序列翻转,转化成一个迭代器
    zip         拉链方法，两边同步，以最短的为准, 返回一个可迭代对象，以元组存放数据
    min(ll,key) 最小值,凡是可以加key的，他会自动将可迭代对象中的每个元素按照顺序传入key对应的函数中,
                如果传入的是字典，默认比较键的大小，返回该键值
    max         最大值
    sorted      排序，不是对原列表排序，生成一个新列表，也可以加key,默认从低到高排，reverse=true，是高到低排
    filter      类似列表推导式的筛选模式，返回的是一个迭代器
    map         类似于列表推导式的循环模式，返回的是一个迭代器
    reduce      累加

    :return:
    """
    str1 = '1+3'
    # print(eval(str1))
    str2 = '''
for i in range(10):
    print(i)'''
    str3 = 'wer'
    # print(hash(str3))
    # exec(str2)
    str_to_int = '12'
    xiaoshu_to_int = 12.99
    erjinzhi_to_in = '0100'
    print(int(str_to_int))
    print(int(xiaoshu_to_int))
    print(int(erjinzhi_to_in, base=2))
    print(float(3.3334))
    print(round(3.2222, 2))
    print(divmod(10, 3))
    print(pow(2, 3, 3))
    str1 = '你好'
    es = str1.encode('utf-8')
    print(es)
    ds = es.decode('utf-8')
    print(ds)
    bes = bytes(str1, encoding='utf-8')
    bes2 = bytes(str1, encoding='gbk')
    print(bes)
    print(bes2)
    print(ord('a'))    # 如果是asc码中的就返回asc码对应的位置，超出就用unicode的位置
    print(ord('中'))
    print(chr(97))
    print(repr(str1))
    print('我叫%s' % str1)
    print('我叫%r' % str1)
    str2 = [1, 2, 0, 'e']
    print(all(str2))
    print(any(str2))
    iter = reversed(str2)
    print(next(iter))
    tup1 = (1, 3, 5)
    obj = zip(str2, tup1)
    for i in obj:
        print(i)
    # li1 = [1, 4, 9, 16, 25]
    li2 = [i**2 for i in range(1, 6)]
    li3 = map(lambda i: i**2, range(1, 6))


def abss(a):
    return abs(a)   # 模拟自己创建的绝对值函数
"""
凡是可以加key的，他会自动将可迭代对象中的每个元素按照顺序传入key对应的函数中
"""
# ll = [1, 2, 6, 77, 8, 99, -8, 77]
# # print(min(ll, key=abss))   # 返回绝对值最小的数
# print(list(filter(lambda i: i > 3, ll)))  # 返回的是迭代器
# print(list(map(lambda i: i**2, ll)))
dict3 = {'a': 2, 'b': 4, 'c': 1}


def my_min(a):     # 返回值最小的对应的键
    return dict3[a]
# print(min(dict3,key=my_min))   # 将dict3的每个元素传给my_min，比较my_min返回值中最小的元素
# print(min(dict3, key=lambda i: dict3[i]))   # 或者简写成匿名函数
# li2 = [('aa', 3), ('bb', 5), ('cc', 1), ('dd', 9), ('ee', 2)]
# print(min(li2, key=lambda i: i[1]))
# print(sorted(li2, key=lambda i: i[1], reverse=True))


def test5():
    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    li = [key for i in M for key in i if key == i[2]]
    li2 = [[i-2, i-1, i] for i in range(3, 10, 3)]
    li3 = [(i-1, i) for i in range(1, 7)]
    li4 = ['alex', 'luhu', 'haha']
    li5 = [li4[i]+str(i) for i in range(len(li4))]
    dict1 = {'name': 'luhu',
             'values': [{"timestamp": 1517996427.94, "value": 100},
                        {"timestamp": 1517996327.94, "value": 101},
                        {"timestamp": 1517993337.94, "value": 111}]}
    li6 = [[k["timestamp"], k["value"]] for k in dict1['values']]
    color = ['black', 'white']
    size = ['s', 'm', 'l']
    li7 = [(i, j) for i in color for j in size]
    li8 = (i for i in range(5))
    print(li8)   # 不使用next不会执行，只会打印地址
    return li8
# g = test5()
# print(next(g))
# print(next(g))


def chain(*args):
    for it in args:
        # for i in it:
        #     yield i
        yield from it   # 可以用yield from优化一层循环，提高效率
# g = chain('abc', (0, 1, 2))
# print(next(g))
# print(next(g))


def lambda_demo(a, b):
    """
    匿名函数，一句话函数，不用声明函数名，冒号前为形参，后为返回值
    :param a:
    :param b:
    :return:
    """
    # return a+b
    my_lambda = lambda a, b: a+b   # 构建匿名函数
    print(my_lambda(1, 2))
    my_lambda2 = lambda i: (i[0], i[2])    # 接受可切片的数据，返回索引为0和2的值
    print(my_lambda2([1, 2, 3, 4]))
    my_lambda3 = lambda i, j: i if i > j else j  # 返回两个数中较大的数
    print(my_lambda3(9, 6))


def reduce_demo(x, y):
    """
    reduce 之前的内置函数，累加，第一次传入，1，2   第二次传入1+2  3
    :param x:
    :param y:
    :return:
    """
    return 10*x+y

# print(reduce(reduce_demo, [1, 2, 3, 4, 5]))


def bibao_demo():
    """
    闭包  保证数据的安全性
    内层函数 对外层非全局变量的使用，就会形成闭包
    被引用的非全局变量也叫做自由变量，这个变量会和内层函数产生一个绑定关系
    自由变量不会在内存中消失
    闭包只存在嵌套(高阶)函数中
    通过代码判断有没有自由变量，确定是不是闭包
    :return:
    """
    li = []

    def average(avg):
        li.append(avg)
        return sum(li)/len(li)
    return average


# bi = bibao_demo()
# print(bi.__code__.co_freevars)
# print(bi(1000))
# print(bi(2000))
# print(bi(3000))


def zhuangshiqi():
    """
    装饰器就是一个函数，本质是闭包
    装饰器：完全遵循开放封闭原则，在不改变原函数的代码以及调用方式的前提下，为其增加新功能
    开放：对代码的拓展是开放的，修改功能（函数）
    封闭：对源码的修改是封闭的(被装饰函数)
    :return:
    """
    print('打开了一个很复杂的功能')


def index(f):
    """
    最简单的装饰器，对zhuangshiqi函数的扩展，不改变调用方法及原函数的代码
    :param f:
    :return:
    """
    def inner():
        start_time = time.time()
        print(time.time())
        f()
        time.sleep(2)
        end_time = time.time()-start_time
        print(end_time)
    return inner
# zhuangshiqi = index(zhuangshiqi)
# zhuangshiqi()


def index1(f):
    def inner():
        start_time = time.time()
        time.sleep(2)
        f()
        end_time = time.time()-start_time
        print(end_time)
    return inner


@index1     # 装饰器的语法糖,相当于先执行zhuangshiqi1=index1(zhuangsiqi1)，然后在执行zhuangshiqi1()
def zhuangshiqi1():
    print('打开了一个很复杂的功能。。。')
# zhuangshiqi1()


def index2(f):
    def inner():
        r = f()
        start_time = time.time()
        time.sleep(1)
        end_time = time.time()-start_time
        print(f'耗时:{end_time}')
        return r
    return inner


@ index2
def zhuangshiqi2():
    """
    被装饰函数是一个带有返回值的函数
    :return:
    """
    print('打开了一个很复杂且有返回值的功能！！！')
    return 666
# print(zhuangshiqi2())    # 相当于先zhuangshiqi2=index(zhuangshiqi2),然后zhuangshiqi2()


def index3(f):
    def inner(*args, **kwargs):
        start_time = time.time()
        r = f(*args, *kwargs)
        time.sleep(0.4)
        end_time = time.time()-start_time
        print(end_time)
        return r
    return inner


@index3
def zhuangshiqi3(name, age):
    """
    标准版的装饰器，有返回值，有参数的被装饰函数
    :param name:
    :param age:
    :return:
    """
    print(f'欢迎{age}岁的{name}打开了一个超复杂的功能')
    return 666
# print(zhuangshiqi3('luhu', 12))


# -------------------------------------------------------------------------------------------#
import sys
# sys.path.append(r'/Users/hulu/PycharmProjects/studyPython/TestPath')  # 添加绝对路径
sys.path.append(os.path.dirname(__file__)+'/TestPath')
"""
通过相对路径添加自定义模块路径,目的是隐藏文件结构
"""
# import b
# from my_package import *


def mokuai():
    """
    自定义模块：
    模块，本质就是py文件，封装语句的最小单位
    自定义模块，就是定义py文件：变量定义，可执行语句，for循环，函数定义等
    模块的运行方式：脚本运行（解释器直接运行）
                 模块方式：被其他的模块导入，为导入的模块提供资源（变量，函数定义，类函数等）
    自定义模块被导入（import）时，其中的可执行语句会立即执行
    python中提供了一种可以判断自定义模块是属于开发阶段还是使用阶段的方法__name__,如果直接出现在模块中，
    以脚本方式运行时，会返回__main__,以导入方式运行时，会返回模块名
    sys.path 查看模块所在的路径
    __file__当前的绝对路径
    os.path.dirname(__file__)获取一个路径的父路径
    import xx 和 from xx import *的区别：
    import xx必须使用模块名xx前缀调用其中的成员
    from xx import * 可以直接使用成员名来调用，但容易产生命名冲突
    可以使用别名alias来解决冲突 from xx import xx as xx1
    import xx as x 给模块起别名，简化
    可以通过__all__控制from xx import *允许调用的成员,详见my_package.py


    :return:
    """
    pass
    # print(sys.path)
    # print(b.test_func())
    # print(age1, pac_func2())

# # 将项目所在的父目录导入即可,xx项目的父目录是testpath
# sys.path.append(os.path.dirname(__file__)+'/TestPath')
# from xx.z import zz
# print(zz.z_f())
# # print(zz.yy.y_f())   # 不想对外界暴露文件结构(yy模块)在zz.py引用时可以使用from ..y.yy import *，通过zz.y_f()调用
# print(zz.y_f())
# -------------------------------------------------------------------------------------------#


def my_random():
    """
    random模块，提供了和随机数获取相关的方法
    random.random()获取[0.0,1.0)范围内的浮点数
    random.randomint(a,b)获取[a,b]范围内的一个整数
    random.uniform(a,b)获取[a,b)范围的=内的浮点数
    random.shuffle(x)把参数指定的数据中的元素打乱，参数必须是一个可变的数据类型
    random.sample(x,k)从x中随机抽取k个数据，返回一个列表
    :return:
    """
    li = list(range(10))
    random.shuffle(li)
    print(li)
    li2 = random.sample(li, 5)
    print(li2)


def my_time():
    """
    时间模块，封装了时间戳以及与字符串转换的相关功能
    time.time() 获取时间戳，现在据计算机元年(1970.01.01 00:00:00)的秒数
    time.gmtime(secs) 获取格式化时间对象，GMT:格林尼治时间,传入一个时间戳，不传就默认当前时间
    国外的tm_wday第一天从0开始，tm_yday一年的第多少天，tm_isdst是否是夏令时
    time.localtime(secs)  获取当地时间对象
    time.strftime(format(str),secs)   # 将时间对象格式化成可读时间
    time.strptime(str,format(str))   # 将可读时间解析成时间对象
    time.mktime(format(str))   # 将时间对象转化成时间戳
    :return:
    """
    print(time.gmtime())
    print(time.localtime())
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    print(time.strptime('2020-07-19 01:00:54', '%Y-%m-%d %H:%M:%S'))
    print(time.strptime('2020', '%Y'))   # 不传月日，时间，时间默认给0，日期默认给1
    print(time.mktime(time.localtime()))


def my_datetime():
    """
    datetime 模块封装了一些和日期，时间相关的类 date time timedelta,多用于数学计算
    timedelta 时间的变化量
    :return:
    """
    # date类：获取时间对象的各个属性
    dt = datetime.datetime(2020, 3, 1, 12, 23, 33)
    d = datetime.date(2010, 10, 10)
    t = datetime.time(12, 13, 14)
    print(dt)
    print(d.month)
    print(t.hour)
    print(dt.month)
    print(dt.hour)
    td = datetime.timedelta(days=1, hours=1, minutes=12)
    td2 = datetime.timedelta(hours=3, minutes=23, seconds=34)
    t1 = td - td2   # 时间运算
    t2 = dt + td
    print(t2)


def my_os():
    """
    os 和操作系统相关的操作
    文件的重命名，删除
    os.remove(path)
    os.rename(old,new)
    os.removedirs()   # 文件夹必须是空的才能删除
    os.path.dirname(path)  # 返回path的父目录
    os.path.basename(path) # 返回path中最后一级的名称（文件夹名，或文件名）
    os.path.split(path)    # 把path中的路径和文件名切分开，返回一个元组
    os.path.join(path,paths) # 将多个路径拼接起来
    os.path.abspath(path)   # 获取当前项目路径拼接path返回
    os.path.isdir(path)    # 判断是不是文件夹
    os.path.exists()       # 判断文件，路径是否存在
    :return:
    """
    path = os.path.join(r'd:', 'aaa', 'ggg')
    path1 = os.path.abspath('ff')
    print(path1)


def my_sys():
    """
    和python解释器相关的操作
    sys.argv[0]  # 脚本名
    sys.argv[1]  # 第二个参数
    sys.path    # 解释器寻找模块的路径
    sys.modules # 返回系统已经加载的模块，以字典形式返回

    :return:
    """
    # return int(sys.argv[1]) + int(sys.argv[2])
    # python studyPython.py 1 3  命令行执行
    print(sys.modules)


def my_json():
    """
    json(javaScript Object Notation):把所有的东西变成字符串，用于存储或网络传输
    json的序列化是不完全的序列化过程
    序列化过程（serialization）将内存中的数据转换成字节串，用以保存文件或网络传输，称为序列化过程
    反序列化过程（deserialization）从文件，网络中获取的数据，转换成内存中原来的数据类型，称为反序列化过程
    dumps 序列化成json字符串，存在内存中
    dump  将字符串写入文件中
    loads 从内存中反序列化成json字符串
    load  从文件中反序列化成json字符串
    json文件通常都是一次性写，一次性读
    :return:
    """
    s = json.dumps([1, 2, 3, 6, 8])
    s1 = json.dumps((1, 2, 3, 6, 8))   # 元组序列化后变成列表，无法序列化集合
    # print(type(s))
    print(s)
    with open('serialization.txt', mode='at', encoding='utf-8') as f1:
        json.dump(s1, f1)

    load = json.loads(s1)
    print(load)
    # print(type(load))
    with open('serialization.txt', mode='rt', encoding='utf-8') as f2:
        print(type(f2))
        ret = json.load(f2)
        print(ret)
    os.remove('serialization.txt')
    with open('json.txt', mode='at', encoding='utf-8') as f3:
        f3.write(json.dumps([1, 4, 6, 8, 99, 0])+'\n')
        f3.write(json.dumps([1, 3, 6, 11, 99, 22])+'\n')

    with open('/Users/hulu/PycharmProjects/studyPython/tmp/json.txt', mode='rt', encoding='utf-8') as f4:
        for line in f4:
            print(json.loads(line.strip()))


def my_pickle():
    """
    pickle将python中所有的数据类型转换成字节串，序列化过程
          将字节串转化成python中的数据类型，反序列化过程
    pickle多次读写容易出错，常用场景一次读一次写，不能跨语言
    与json对比：
    json：1.不是所有的数据类型都可以序列化
          2.不能多次对同一个文件序列化
          3.json数据可以跨语言
    :return:
    """
    bys = pickle.dumps([1, 2, 3, 'tt'])
    bys1 = pickle.dumps((1, 4, 5, 7))
    bys3 = pickle.loads(bys1)
    # print(bys3)
    # print(type(bys3))
    with open('pickle.txt', mode='wb') as f1:   # 这里的模式要使用b模式，操作字节
        pickle.dump((1, 2, 3, 5, 'ss'), f1)    # 一次性写入文件中

    with open('pickle.txt', mode='ab') as f2:   # 这里的模式要使用ab模式，追加操作字节
        pickle.dump((1, 2, 3, 5, 'ss'), f2)
        pickle.dump((8, 2, 3, 4, 'ff'), f2)

    with open('pickle.txt', mode='rb') as f3:
        for i in range(3):   # pickle多次读写容易出错
            print(pickle.load(f3))


def my_collections():
    """
    collections模块
    namedtuple()：命名元组
    defaultdict():默认值字典
    Counter()：计数器

    :return:
    """
    Rectangle = namedtuple('这是矩形的类Rectangle的说明', ['length', 'width'])
    r = Rectangle(10, 5)
    # print(r.length)  # 通过属性访问元组的元素

    dict1 = defaultdict(int, name='luhu', age=12)   # int为工厂函数
    dict2 = defaultdict(lambda: 4, name='luhu', age=12)   # int为工厂函数

    # print(dict2['adress'])
    # print(dict(dict2))
    c = Counter('ewrwetedfagjjdgh哈哈哈你好')

    print(dict(c))  # 返回一个计数对象
    print(c.most_common())  # 返回一个列表，字母和对应出现次数以元组形式存放


def my_hashlib():
    """
    hashlib 封装一些用于加密的类
    目的：用来判断和验证，并非解密
    特点：把一个大的数据切分成不同块，分别对不同的块进行加密，再汇总的结果，和直接对整体数据加密的结果是一致的
         单向加密，不可逆
         原始数据的一点小变化，将导致结果雪崩式差异
    :return:
    """
    m = hashlib.md5()   # 获取一个加密对象
    m.update(b'hello')  # 使用加密对象的update，进行加密，只接收字节类型
    m.update('abc你好'.encode('utf-8'))  # 多次调用会累加加密
    res = m.hexdigest()    # 通过hexdigest获取结果
    print(res)


def my_module1():
    """
    不同的数据库模块有同样的连接方法
    模块别名统一接口，归一化思想
    :return:
    """
    res = input('请输入')
    if res == 'mysql':
        import mysql1 as sm
    elif res == 'oracle':
        import oracle1 as sm

    sm.conect()


def my_re():
    """
    正则表达式
    元字符
    []  一个中括号只表示一个字符位置
    [abc] 匹配a或b或c
    [0-9a-zA-z]  按照asc码表进行的范围比对，匹配一个字符在0-9，a-z，A-Z之中的一个字符
    在正则表达式中能帮助我们表示匹配的内容的符号都是正则中的元字符
    \d  [0-9] digit
    \w  [0-9a-zA-z_]   表示匹配数字字母下划线  word
    \s可以匹配所有的空白     |\t|\n  空格，tab，换行(enter),换行不容易看出来
    \D   不是数字都匹配
    \W   不是数字字母下划线就可以匹配
    \S   匹配非空白字符
    [\d\D] [\s\S][\w|w]    匹配所有
    .    匹配除换行符以外的所有(一个字符)
    [^\d]   [^1]    匹配所有的非数字
    ^    匹配一个字符串的开始
    $    匹配一个字符串的结尾
    ｜    或  a表达式|b表达式 匹配a或b表达式，如果a匹配成功，不会匹b，如果两个规则有重叠的部分，总是把长的放在左边
             abc|ab  匹配abc或ab
    ()   分组   约束或描述的范围             www\.(baidu|jd|taobao)\.com
    \b      匹配边界border                hello world  o\b  只匹配第一个在单词尾的o
    量词
    {n}     表示匹配n次
    {n,}    表示至少匹配n次
    {n,m}   表示至少匹配n次，至多匹配m次
    ?       表示匹配0次或1次
    +       表示匹配1次或多次
    *       表示匹配0次或多次
    \d+(\.\d+)?  匹配小数或整数
    贪婪匹配 : 在量词范围允许的情况下，尽可能多的匹配内容   \d{3,}6    123456657896 整个都会被匹配上
    惰性匹配：在量词范围允许的情况下，尽可能少的匹配内容     \d{3,}?6   (量词后加？)        123456657896 123456会被匹配上
    .*?x  表示匹配任意字符任意次数，遇到x就停下来（惰性匹配）
    转义符：原本有特殊意义的字符放到字符组里[],可以取消它的意义，-在字符组里表示范围，不希望表示范围可以放在最前面
    [().*+?] 在字符组中会取消它的特殊意义，或者加\取消特殊意义
    findall  只显示括号里匹配到的内容，优先显示分组中的
    search 还是按照完整的正则进行匹配，显示也显示第一个匹配到的内容，但是可以给group方法传参获取具体文组的内容
    加括号是为了对真正需要的内容进行提取
    split((re),str)  切割，返回被切开的字典，也可以使用括号对提取规则匹配的内容进行提取
    sub((re),res，str，index)    替换   将res按照re规则替换索引位置为res
    subn((re),new,str)  替换，将str按照规则re匹配内容，并将匹配到的内容替换成new，返回元组，里面存放替换的str和替换次数
    match((re),str)    匹配以re规则开头的内容，其他和search方法一致，match一般用来规定字符串必须是这样的
    compile()  一个正则表达式如果要用多次，可以先用compile编译一下，节省时间
    finditer()   节省空间，将匹配的内容作为迭代器返回,结果集特别多时用
    分组命名   给分组命名，方便取值，详见ret5,分组命名的引用，匹配开头结尾相同规则的内容
               也可以通过分组的索引取规则   '<(\w+)>.*?</\\1>'  \1在Python中有转义，要使用\阻止转义
    '<(?P<tag>\w+)>.*?</(?P=tag)>'
    :return:
    """
    ret0 = re.findall('4\d\d', '3244242t435242')
    ret = re.findall('4(\d)(?:\d)', '3244242t435242')   # 取消优先显示分组2 ?:
    ret1 = re.search('4(\d)(\d)', '3244242t435242324324322')   # search只匹配一个，匹配不上返回会报错
    print(ret0)
    print(ret)
    if ret1:
        print(ret1.group())
        print(ret1.group(1))    # 匹配第1个分组中的
        print(ret1.group(2))

    ret3 = re.compile('4\\d(\\d)')
    ret3.search('dafas2341332qdfasdfdsa')
    ret4 = re.finditer('\d', '342ewrw2342432')
    # for i in ret4:
    #     print(i.group())
    # ret5 = re.search('\\d\\d\\d[1](\\d)(\w*)(?P<name>\\d+)(\\d?)\\d', 'dsafsd234234dfsfsdf23423423asdrwr234211werwer11123423')
    # print(ret5.group('name'))
    # ret6 = re.search('<(?P<tag>\w+)>.*?</(?P=tag)>', '<ab>2342erwer</abc>24424</abvbn>')
    # print(ret6)
    ret7 = re.search('<(\w+)>.*?</\\1>', '<ab>2342erwer</ab>24424</abvbn>')
    print(ret7)
    # print(ret0)
    # print(ret)
    # if ret1:
    #     print(ret1.group())
    #     print(ret1.group(1))    # 匹配第1个分组中的
    #     print(ret1.group(2))


def filter_int():
    reg = '1-23+34*56+(56-5.09)+4.55'
    ret = re.findall('\d+\.\d+|(\d+)', reg)
    ret = filter(lambda n: n, ret)
    print(list(ret))


sys.setrecursionlimit(100000)   # 可以手动修改最大递归深度
count = 0


def digui():
    """
    递归函数（Recursion），python的递归函数默认递归最大深度是1000层
    return返回给上一级调用digui()，层层递归，return到第一级
    并不是函数中有return，return的结果就一定能被调用函数的外层接收到
    :return:
    """
    global count
    count += 1
    if count == 4:
        return
    print(count)
    digui()
    print('666')


def digui2():
    global count
    count += 1
    print(count)
    if divmod(count, 10) == (5, 1):
        return
    digui2()

# ----------------------------------------------------------------------------------------------------- #
def digui3(count):
    count += 1
    print(count)
    if count == 5:
        return 5

    return digui3(count)

# def digui3(1):
#     count += 1
#     print(2)
#     if 2 == 5:
#         return 5
#     digui3(2)
# def digui3(2):
#     count += 1
#     print(3)
#     if 3 == 5:
#         return 5
#     digui3(3)
# def digui3(3):
#     count += 1
#     print(4)
#     if 4 == 5:
#         return 5
#     digui3(4)
# def digui3(4):
#     4 += 1
#     print(5)
#     if count == 5:
#         return 5     -->返回给digui(4)，digui3()没有return，所以拿到的是None
#     digui3(count)
# ----------------------------------------------------------------------------------------------------- #


res = 1
def jiecheng(number):
    global res
    res = number*res
    print(res)
    number -= 1
    if number == 1:
        return res
    return jiecheng(number)

count = 0
def fibonacci_sequence(a=0, b=1):   # 斐波那契数列，后一个数等于前两个之和
    global count
    count += 1
    if count == 100:
        print(a)
    c = a + b
    a = b
    b = c
    fibonacci_sequence(a, b)
# print('-->', digui3(1))
# fibonacci_sequence()
# print('-->',jiecheng(5))


def logger(*args):
    """
    带参数的装饰器
    :param path:
    :return:
    """
    def log(f):
        def inner(*args1, **kwargs):
            print(args[0])
            print('%s执行了函数%s' % (time.strftime('%Y-%m-%d %H:%M:%S'), f.__name__), '写入'+args[0])
            ret = f(*args1, **kwargs)
            return ret
        return inner
    return log


@logger('login.log')    # ret = logger(login.log) login = ret(login)
def login():
    print('执行了登录功能')


@logger('add_goods.log')
def add_goods():
    print('执行了添加商品功能')


def digui_file(path):  # 获取一个文件夹下所有文件的大小
    size = 0
    dir_list = os.listdir(path)  # 列出该路径下的所有文件夹，返回一个list
    # print(dir_list)
    for i in dir_list:
        abs_path = os.path.join(path, i)
        if os.path.isfile(abs_path):  # 该路径拼接遍历到的文件(夹)名，判断其是否是一个文件
            print(i, os.path.getsize(abs_path))  # 获取文件的大小
            file_size = os.path.getsize(abs_path)
            size = size + file_size
            # print(size)

        else:  # 不是文件，递归返回
            digui_file(abs_path)
    return size


# print(digui_file(r'D:\Users\hulu\PycharmProjects\badmintonRobot\tmp'))


def my_shutil():
    # shutil.copytree('tmp', 'tmp2',ignore=shutil.ignore_patterns('*.py'))
    # 移动文件/目录
    shutil.move("move", "tmp", copy_function=shutil.copy2)

    # 获取磁盘使用空间
    total, used, free = shutil.disk_usage(".")
    print("当前磁盘共: %iGB, 已使用: %iGB, 剩余: %iGB" % (total / 1073741824, used / 1073741824, free / 1073741824))

    # 压缩文件
    # shutil.make_archive('压缩文件夹的名字', 'zip','待压缩的文件夹路径')
    # shutil.make_archive('logging2', 'zip','/Users/jingliyang/PycharmProjects/面试题/常用模块/随机数')
    #
    # # 解压文件
    # shutil.unpack_archive('zip文件的路径.zip','解压到目的文件夹路径')
    # shutil.unpack_archive('/Users/jingliyang/PycharmProjects/面试题/常用模块/shutil模块/logging2.zip','/Users/jingliyang/PycharmProjects/面试题/常用模块/shutil模块/tmp')


def my_logging(a, b):
    """
    日志模块，用于调试和定位问题
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.error('error message')
    logging.critical('critical message')

    logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有：
    filename：用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中。
    filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
    format：指定handler使用的日志显示格式。
    datefmt：指定日期时间格式。
    level：设置rootlogger（后边会讲解具体概念）的日志级别
    stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件(f=open(‘test.log’,’w’))，默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。
    format参数中可能用到的格式化串：
    %(name)s Logger的名字
    %(levelno)s 数字形式的日志级别
    %(levelname)s 文本形式的日志级别
    %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
    %(filename)s 调用日志输出函数的模块的文件名
    %(module)s 调用日志输出函数的模块名
    %(funcName)s 调用日志输出函数的函数名
    %(lineno)d 调用日志输出函数的语句所在的代码行
    %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
    %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
    %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
    %(thread)d 线程ID。可能没有
    %(threadName)s 线程名。可能没有
    %(process)d 进程ID。可能没有
    %(message)s用户输出的消息
    :return:
    """
    # 日志输出到屏幕
    logging.basicConfig(level=logging.DEBUG,
                        format='当前时间%(asctime)s - %(name)s - %(module)s - %(levelname)s: %(message)s',
                        filename='test.log',
                        )

    logging.debug('a+b=%s' % (a + b))
    return a + b


def my_getLogger(a, b):
    """
    logging库提供了多个组件：Logger、Handler、Filter、Formatter。
    Logger对象提供应用程序可直接使用的接口，
    Handler发送日志到适当的目的地，
    Filter提供了过滤日志信息的方法，
    Formatter指定日志显示格式。
    另外，可以通过：logger.setLevel(logging.Debug)设置级别,
    也可以通过fh.setLevel(logging.Debug)单对文件流设置某个级别
    :param a:
    :param b:
    :return:
    """
    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler('test.log', encoding='utf-8')
    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    logging.basicConfig(level=logging.DEBUG,
                        format='当前时间%(asctime)s - %(name)s - %(module)s - %(levelname)s: %(message)s',
                        handlers=[fh, ch])

    logging.debug('a+b=%s' % (a + b))
    return a + b


def my_split_logging():
    """
    StreamHandler:不使用配置文件的方式
    FileHandler:logging模块自带的三个handler之一。继承自StreamHandler。将日志信息输出到磁盘文件上。
    RotatingFileHandler:位于logging.handlers支持循环日志文件
    TimedRotatingFileHandler:定时循环日志handler，位于logging.handlers，支持定时生成新日志文件,when=‘D’，interval=2，就是指两天的时间间隔，
    backupCount决定了能留几个日志文件。超过数量就会丢弃掉老的日志文件。
    :return:
    """
    sh = logging.StreamHandler()
    rh = handlers.RotatingFileHandler('myapp.log', maxBytes=1024, backupCount=5)
    fh = handlers.TimedRotatingFileHandler(filename='x2.log', when='s', interval=5, encoding='utf-8')
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p',
        handlers=[fh, sh, rh],
        level=logging.ERROR
    )

    for i in range(1, 100000):
        time.sleep(1)
        logging.error('KeyboardInterrupt error %s' % str(i))


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 16, 20, 21, 22, 23, 25, 26]


def erfen(x, mid=(len(li)-1)//2):
    if li[mid] == x:
        return mid
    elif li[mid] > x:
        mid = (mid-1)//2
    elif li[mid] < x:
        mid = (mid+len(li)-1)//2

    return erfen(x, mid)
# print(erfen(16))


class Person:  # 定义一个人类
    """
    面向对象：定义一个模子，用来描述一类事物，具有相同的属性和方法
    类是一个大范围，约束了事物的属性，但不能约束具体的值
    对象是一个具体的内容，是类的产物，遵循类的约束，同时给属性赋值
    类下面的静态变量，属性，绑定方法都储存在该类的命名空间中

    特殊的类属性
    类名.__name__# 类的名字(字符串)
    类名.__doc__# 类的文档字符串
    类名.__base__# 类的第一个父类(在讲继承时会讲)
    类名.__bases__# 类所有父类构成的元组(在讲继承时会讲)
    类名.__dict__# 类的字典属性
    类名.__module__# 类定义所在的模块
    类名.__class__# 实例对应的类(仅新式类中)
    """
    role = 'person'

    def __init__(self, name, aggressivity, life_value):   # 必须叫这个名字，创建对象时会自动调用这个初始化方法
        self.name = name
        self.aggressivity = aggressivity
        self.life_value = life_value

    def attack(self, dog):
        dog.life_value -= self.aggressivity
        return dog.life_value


class Dog:
    def __init__(self, aggressivity, life_value, name='dog'):   # 必须叫这个名字，创建对象时会自动调用这个初始化方法
        self.name = name  # 为类创建属性，所有的这一个对象需要使用的属性都需要与self关联起来
        self.aggressivity = aggressivity   # 执行完init中的逻辑之后，self变量会自动的被返回到调用处
        self.life_value = life_value

    def bark(self, person):   # 为类创建方法
        person.life_value -= self.aggressivity
        return person.life_value
# per = Person('ll', 23, 400)    # 实例化，会自动传到__init__中，调用__init__把空间的内存地址作为self参数传递到函数内部
# # print(dir(per))
# # print(per.__dict__)
# # print(per.__doc__)
# dog = Dog(2, 100)
# per.attack(dog)
# dog.bark(per)
# per.sex = 'male'  # 对象属性的新增
# print(per.__dict__)
# del per.name  # 对象属性的删除
# print(per.__dict__)


class MyCircle:
    def __init__(self, semicircle):
        self.semicircle = semicircle

    def get_square(self, pi):
        square = self.semicircle**2*pi
        return square
# my_circle = MyCircle(7)
# print(my_circle.get_square(math.pi))


exp = '1+2-3+2*8/9+6-3*3/5*(1+2)'


def jisuanqi(exp):
    ret = re.search('(\d+(\.\d+)?)[*/](\d+(\.\d+)?)', exp)
    if ret:
        if '*'in ret.group():
            s = ret.group().split('*')
            ret1 = float(s[0])*float(s[1])
            exp = exp.replace(str(ret.group()), str(ret1))
            print(exp)
            jisuanqi(exp)
        elif '/' in ret.group():
            s = ret.group().split('/')
            ret1 = float(s[0]) / float(s[1])
            exp = exp.replace(str(ret.group()), str(ret1))
            print(exp)
            jisuanqi(exp)
    ret2 = re.search('(\d+(\.\d+)?)[-+](\d+(\.\d+)?)', exp)
    if ret2:
        if '+'in ret2.group():
            s = ret2.group().split('+')
            res = float(s[0])+float(s[1])
            exp = exp.replace(str(ret2.group()), str(res))
            print(exp)
            jisuanqi(exp)
        elif '-'in ret2.group():
            s = ret2.group().split('-')
            res = float(s[0])-float(s[1])
            exp = exp.replace(str(ret2.group()), str(res))
            print(exp)
            jisuanqi(exp)
    else:
        print(exp)
        return exp


class MyCount:
    """
    类的静态变量
    如果一个变量是所有对象共享的值，那么这个变量应该被定义成静态变量，所有和静态变量相关的增删改查都应该使用类名来处理
    """
    count = 0

    def __init__(self):
        MyCount.count += 1     # 记录实例化的次数
# my = MyCount()
# my2 = MyCount()
# print(my2.count)


class Student:
    """
    类的组合:在一个类中以另外一个类的对象作为数据属性，称为类的组合
    初始化对象的时候把要引用的类对象作为参数放进要调用的类对象中，通过对象名.变量名.属性名，来查看组合类中的属性值
    通过对象名.变量名.方法名()调用组合类中的方法
    """
    def __init__(self, name, sex, phone_number):
        self.name = name
        self.sex = sex
        self.phone_number = phone_number

    def tingke(self):
        print('学生在听课')


class ClassRoom:
    def __init__(self, amount, student):
        self.student = student
        self.amount = amount
# cla = ClassRoom(11, Student('luhu', 'male', '15856691310'))
# print(cla.student.name)
# cla.student.tingke()


class Project:
    """
    类组合的好处，关联的类的属性值修改，所有绑定该类的对象中的属性值都会被修改
    """
    def __init__(self, course, time, teacher):
        self.course = course
        self.time = time
        self.teacher = teacher


class Course:
    def __init__(self, name, price):
        self.name = name
        self.price = price
# linux = Course('linux', '13400')
# python = Course('python', '12900')
# lin_pro = Project(linux, '6mouth', 'wusir')
# print(lin_pro.course.price)
# py_pro = Project(python, '3mouth', 'jane')
# lin_pro2 = Project(linux, '7mouth', 'xiaoming')
# linux.price = '20000'
# print(lin_pro2.course.price)
# print(lin_pro.course.price)


class Circle:
    def __init__(self, r):
        self.r = r

    def square(self):
        s = pi*self.r**2
        return s


class RingCircle:
    def __init__(self, r1, r2):
        r1, r2 = (r1, r2) if r1 > r2 else (r2, r1)     # 三元运算符
        self.outside_circle = Circle(r1)
        self.inside_circle = Circle(r2)

    def ring_square(self):
        return self.outside_circle.square() - self.inside_circle.square()
# rc = RingCircle(7, 4)
# print(rc.ring_square())


class Animal:
    """
    继承：Cat继承Animal类
          Animal  父类（超类，基类）
          Cat     子类（派生类）
          子类可以使用父类的方法和静态变量
    """
    def __init__(self, name):
        self.name = name
        self.blood = 100
        self.waise = 200

    def run(self):
        print(self.name, '动物会跑')

    def drink(self):
        print(self.name, '会喝水')

    def breath(self):
        print(self.name+'会呼吸')


class Cat(Animal):
    def miaomiao(self):
        print('喵喵叫')

    def run(self):
        Animal.run(self)
        print(self.name, '喵喵会跑')

    def drink(self):
        self.waise += 300
        Animal.drink(self)   # 使用父类类名，调用父类的同名方法
        print(self.name+'喝水会加智慧')


class Fish(Animal):
    """
    父类和子类方法的选择：
        子类的对象如果调用方法，永远优先调用自己的，如果自己没有才会用父类的
        如果自己有还想用父类的，直接在子类方法中调用父类的方法
        如果调用父类的方法名与子类的方法名同名，需要在子类方法中使用父类名.方法名，来调用父类方法
        如果调用子类自己的其他方法，需要在子类方法中使用self.方法名，来调用子类中其他的方法
    """
    def drink(self):
        self.blood += 100
        # Animal.drink(self)
        print(self.name+'喝水会加血')

    def breath(self):
        print(self.name+'有自己的呼吸方式')
        # Fish.drink(self)
        self.drink()   # 调用子类自己的其他方法
        Animal.drink(self)
        print('呼吸的时候会喝水')
# cat = Cat('猫')  # 调用init，对象在自己的空间中没找到init，然后会找父类的init
# fish = Fish('鱼')
# # cat.drink()
# # fish.drink()
# fish.breath()
# print(cat.__dict__, fish.__dict__)


class Foo:
    def __init__(self):
        self.func()   # 在每一个self调用func的时候，我们不看这句话在哪里执行，只看self是谁，这里self是Son，son.func()

    def func(self):
        print('in Foo')


class Son(Foo):
    def func(self):
        print('in Son')
# s = Son()


class Cat2(Animal):
    """
    子类也有初始化方法，这时候要使用父类名.__init__(self,args)
    """
    def __init__(self, name, eye_color):
        Animal.__init__(self, name)   # 调用了父类的初始化，去完成一些通用属性的初始化
        self.eye_color = eye_color    # 派生属性
# cat2 = Cat2('小白', 'blue')
# print(cat2.eye_color)


class A:
    """
    新式类，python3中的类，python2中继承obj的类就叫新式类
    经典类，python2中没有继承obj的类
    多层的单继承，如果子类对象中没有需要调用的方法，如果父类也没有，就去爷级中寻找，知道找到为止
    当B，C类继承A类时，D继承B，C，D(B,C)初始化D调用D中的方法，如果没有，会从父类中找，优先近的B，如果B中没有，找C类中就叫往广度
    找，找A类中就叫往深度找，新式类总是优先广度寻找，经典类会优先深度寻找
    优先广度算法，C3算法
    """
    def func1(self):
        print('in A')
class B(A):pass
class C(B):pass
class D:
    def func1(self):
        print('in D')
class F(A, D):
    """如果多继承的父类中都有子类要调用的方法，那么F(A,D)先继承谁就优先调用其中的方法
    Python3中的类都继承object类，object是个类祖宗@
    """
    pass
# C().func1()
# F().func1()    # in A
# print(A.__bases__)   # 打印该类的上一级父类
# print(F.__base__)
# print(F.__bases__)
f = F()
# print(type(f) is F)    # 判断F类是不是f的类型，但是无法判断F的父类A是不是f的类型
# print(isinstance(f, A))    # 判断F类是不是f的类型，也可以判断F的父类A是不是f的类型

# a =A()
# print(A.func1)    # 函数<function A.func1 at 0x0000019D969557B8>
# print(a.func1)    # 方法<bound method A.func1 of <__main__.A object at 0x0000019D96948A90>>
# print(A.__module__)


def my_data():
    """
    数据结构
    {}    字典      key-value 通过key找value的值特别快
    []    序列      通过index找值特别快
    ()    元组
    {1,}  集合
    'str' 字符串

    队列Queue：先进先出FIFO（first in first out）put(1) put(2) put(5) put(3) put(7),第一次get取值1，第二次2，第三次取5
    栈Stack：  后进先出LIFO（last in first out）
    :return:
    """
    pass


class Queue1:
    """
    实现一个简单的先进先出队列
    """
    def __init__(self):
        self.l = []

    def put(self, num):
        self.l.append(num)

    def get(self):
        return self.l.pop(0)


class Stack(Queue1):
    """继承队列实现栈"""
    def get(self):
        return self.l.pop()

# queue = Queue()
# queue.put(1)
# queue.put(2)
# queue.put(3)
# queue.put(5)
# queue.put(4)
# print(queue.l)
# print(queue.get())
# print(queue.get())
# print(queue.get())
# stack = Stack()
# stack.put(1)
# stack.put(2)
# stack.put(3)
# print(stack.get())
# print(stack.get())


class MyPickle:
    """
    面向对象实现pickle的dump，load
    """
    def __init__(self, path):
        self.path = path
        self.bytes = my_bytes

    def pickle_dump(self, my_bytes):
        with open(self.path, mode='ab') as f1:
            pickle.dump(my_bytes, f1)

    def pickle_load(self):
        with open(self.path, mode='rb') as f1:
            while 1:
                try:
                    i = pickle.load(f1)
                    yield i
                except EOFError:
                    break
# my = MyPickle('/Users/hulu/PycharmProjects/studyPython/pickle.txt')
# my.pickle_dump(b'23wrwwqrwq2412')
# for i in my.pickle_load():
#     print(i)


class AObj:
    list = []

    def __init__(self):
        self.list = []

    def func(self):
        self.list.append(1)


class BObj(AObj):
    def __init__(self):
        self.list = []

    def func(self):
        self.list.append(2)
# a = AObj()
# b = BObj()
# a.func()
# b.func()
# print(a.list)
# print(b.list)
# print(AObj.list)
# print(BObj.list)


class A2:
    """
    F（D(B(A)),E(C(A))）,如果F继承D，E，D继承B，E继承C， B，C继承A，那么F在新式类的继承顺序按广度优先，满足c3算法
    在其他线路上有就不会走，提高效率
    merge规则；
    如果一个类出现在从左到右所有顺序的最左侧，并且没有在其他位置出现，那么先提出来作为继承顺序中的一个
    或一个类出现在从左到右顺序的最左侧，并且没有在其他顺序中出现，那么先提出来作为继承顺序中的一个
    如果从左到右第一个顺序中的第一个类出现在后面且不是第一个，那么不能提取，顺序向后继续找其他顺序中符合上述条件的类
    A(O) = [AO]    A继承Obj
    B(A) = [BAO]   B继承A
    C(A) = [CAO]
    D(B) = [DBAO]
    E(C) = [ECAO]
    F(D,E)=c3(D(B)+E(C))
          = F[+]
         F=[DBAO] + [ECAO]
        FD=[BAO] + [ECAO]
       FDB=[AO]  + [ECAO]   A出现在后面，会走重复的操作，所以提E
      FDBE=[AO]  + [CAO]
     FDBEC=[AO]  + [AO]
    FDBECA=[O]   +[O]
    FDBECAO   可以使用此方法D2.mro()核对


    """
    def func(self):
        print('in a')

class B2(A2):
    def func(self):
        print('in B')

class C2(A2):
    pass

class D2(B2, C2):
    pass

# -------------------------------------------------------
# print(D2.mro())  # 查看D继承的顺序


# class Payment:
#     """
#     抽象类
#     raise 主动抛出异常，如果子类没有重写pay方法就主动抛出异常
#     这个类也叫规范类，不实现功能，只为规范之后的同类型方法
#     """
#     def pay(self, price):
#         raise NotImplementedError('请重写pay的同名方法')
# -------------------------------------------------------


from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    """
    实现抽象类的另一种方式，只要不重写pay方法，实例化就会失败报错
    """
    @abstractmethod
    def pay(self, price):
        print('请重写该同名方法')


class weChat(Payment):
    def __init__(self, name):
        self.name = name

    def pay(self, price):
        dic = {'name': self.name, 'price': price}
        # 调用微信支付的链接
        print('%s通过微信支付了¥%s' % (self.name, price))


class AliPay(Payment):
    def __init__(self, name):
        self.name = name

    def fuqian(self, num):
        dic = {'name': self.name, 'price': num}
        # 调用ali支付链接
        print('%s通过AliPay支付了¥%s' % (self.name, num))


def pay(name, price, kind):
    """
    归一化处理，方便对接的同事调用
    或者通过反射优化代码，使得每次不用修改代码，即可完成其他支付类型的归一化处理
    :param name:
    :param price:
    :param kind:
    :return:
    """
    # if kind == 'weChat':
    #     wx = weChat(name)
    #     wx.pay(price)
    # elif kind == 'AliPay':
    #     ali = AliPay(name)
    #     ali.pay(price)
    class_name = getattr(sys.modules['__main__'], kind)
    obj = class_name(name)
    obj.pay(price)
# pay('luhu', 200, 'weChat')
# pay('haha', 300, 'AliPay')


def len(obj=range(1, 11)):
    """
    多态： 一个类型表现出来的多种状态，比如支付中表现出的苹果支付和微信支付两种状态
    在Java中：一个参数必须指定类型
    所以如果想让两个类型的对象都可以传，那么必须让两个类继承自一个父类，在指定类型的时候用父类来指定 def pay(Payment a, int b)
    但在python中不需要指定类型，所以python中处处是多态，
    鸭子类型： 长得像鸭子的就叫鸭子类型
    所有实现了__len__ 方法的类，在调用len函数的时候，obj都说是鸭子类型
    比如 类里面__dir__中只要有__iter__,__next__ 的就是迭代器

    """
    return obj.__len__()


class A3:
    """
    多继承中super()按照广度mro来寻找func方法
    在单继承中，super()就是调用父类中的方法
    """
    def func(self):
        print("A")


class B3(A3):
    def func(self):
        super().func()
        print('B')


class C3(A3):
    def func(self):
        super().func()
        print('C')


class D3(B3, C3):
    def func(self):
        super().func()
        print('D')
# d = D3()
# print(D3.mro())
# d.func()


class User:
    """
    在单继承中用super()表示父类中的同名方法
    """
    def __init__(self, name):
        self.name = name


class VIPUser(User):
    def __init__(self, name, level):
        # User.__init__(self, name)   # 不推荐
        # super(VIPUser, self).__init__(name)
        super().__init__(name)  # 推荐
        self.level = level
# lu = VIPUser('luhu', 12)
# print(lu.__dict__)
# print(lu.__dir__())


class UserInfo:
    """
    封装：把属性或方法装起来
    广义上：把属性和方法装起来，外面不能直接调用，要通过类名来调用
    狭义上：把属性和方法隐藏起来，外面不能调用，只能内部使用
    """
    def __init__(self, name, password):
        self.name = name
        self.__password = password   # 加上双下划线就变成私有的

    def get_password(self):
        return self.__password
# info = UserInfo('luhu', 123456)
# print(info.get_password())   # 只能看不能改值
# print(info.password)  # 报错，看不到了


class Foo2:
    """
    私有方法和属性不能被子类使用
    """
    def __init__(self):
        self.__func()

    def __func(self):
        print('in foo')


class Son2(Foo2):
    # def __init__(self):
    #     self.__func()

    def __func(self):
        print('in son')
# Son2()


class MyProperty:
    def __init__(self, r):
        self.r = r

    @property
    def square(self):
        """
        用property装饰器将方法伪装成属性，
        :return:
        """
        return pi*self.r**2
# circle = MyProperty(4)
# print(circle.r)
# print(circle.square)


class Goods:
    discount = 0.8

    def __init__(self, name, origin_price):
        """
        装饰器进阶，属性值的修改
        :param name:
        :param origin_price:
        """
        self.name = name
        self.__origin_price = origin_price

    @property
    def price(self):
        return self.discount * self.__origin_price

    @price.setter     # 给price加参数，接收一个新的参数替换旧值
    def price(self, new_price):
        if isinstance(new_price, int):
            self.__origin_price = new_price

    @price.deleter  # 删除方法，不常用
    def price(self):
        print('zhixing ')
        del self.__origin_price
# apple = Goods('apple', 7)
# print(apple.price)
# apple.price = 5
# del apple.price
# print(apple.price)


class Person3:
    """
    反射，getattr
    反射类的静态变量/其他方法
    反射对象的实例变量/绑定方法
    反射模块中的所有变量：1被导入的模块，当前执行的py文件-脚本
    判断模块中是否能反射成功  hasattr

    """
    Role = 'role'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        print('aha')


# ll = Person3('路虎', 23)
# ret = getattr(ll, 'name')    # 反射对象的实例变量
# print(ret)
# ret2 = getattr(ll, 'func')  # 反射对象绑定的方法
# print(ret2)    # 返回的是方法对应的地址，加上()即可执行该方法
# print(getattr(Person3, 'Role'))   # 反射类的静态变量
# import fanshe
# print(getattr(fanshe, 'sww'))  # 引用模块中的任意变量
# print(getattr(fanshe, 'l1'))
# print(getattr(fanshe, 'd1'))
# print(hasattr(fanshe, 'd11'))    # 判断模块中是否能反射成功，与getattr一起使用防止报错
class File:
    l1 = ['write', 'read', 'remove']

    def write(self):
        print("in write")

    def read(self):
        print("in read")

    def remove(self):
        print("in remove")
# f = File()
# print(f.__dir__())
# i1 = input('请输入操作序号')
# if int(i1) in range(1, 4):
#     obj = getattr(f, File.l1[int(i1)-1])   # 反射对象里的方法地址
#     print(obj)
#     obj()


class Goods1:
    __discount = 0.5
    """
    @classmethod 把一个对象绑定的方法改成类方法
    在方法中仍然可以引用类中的静态变量
    可以不用实例化对象，直接用类名在外部调用这个方法
    什么时候用classmethod
    1.定义了一个方法，默认传self，但这个self没有使用
    2.并且你在这个方法里用到了当前的类名，或者准备使用这个类的内存空间中的名字的时候
    """

    def __init__(self, name, origin_price):
        self.name = name
        self.__origin_price = origin_price

    @property
    def price(self):
        return self.__origin_price*self.__discount

    @classmethod
    def change_discount(cls, new_discount):
        cls.__discount = new_discount
# Goods1.change_discount(0.3)
# goods = Goods1('apple', 20)
# print(goods.price)


class User:
    pass
    """
    @staticmethod装饰器，本身就是一个普通的函数，被挪到类的内部执行，那么直接给这个函数添加staticmethod装饰器就可以了
    什么时候用：在函数内部既不会用到self，也不会用到cls类
    """
    @staticmethod
    def login(a, b):
        print('登录的逻辑', a, b)
# User.login('a', 'b')   # 可以通过类名.方法直接调用，也可以和普通方式先实例化一个对象，再调用
# user = User()
# user.login('a', 34)


class Cls:
    """
    __callable__   对象()调用这个类中的__call__方法
    __len__        len(对象)，需要实现这个类中的__len__方法
    :return:
    """
    def __init__(self, name):
        self.name = name
        self.students = []

    def __len__(self):
        return len(self.students)
# cc = Cls('class')
# cc.students.append('luhu')
# print(len(cc))
# print(cc.students.__dir__())


class New(object):

    def __new__(cls, *args, **kwargs):  # cls表示类自己的对象，不是调用它的对象
        """
        先创建对象的空间，有一个类指针指向__new__
        调用init
        new可用于单例设计
        :param args:
        :param kwargs:
        :return:
        """
        # o = super().__new__(cls)    # 重写父类object中的new方法
        o = object.__new__(cls)
        print('in new', o)
        return o

    def __init__(self):
        print('in init', self)
# new = New()


class Baby:
    """
    利用__new__实现的单例设计模式
    这个类被调用的时候只会创建一个实例
    更简单的单例模式，把它当作模块导入，使用其中的方法都是单例
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, cloth, pants):
        self.cloth = cloth
        self.pants = pants


b1 = Baby('ff', 'tt')
b2 = Baby('qq', 'zz')

# print(b1.cloth)
# print(b2.cloth)


class MyCourse:
    """
    __str__    __repr__
    在打印一个对象的时候，调用__str__方法
    在%s拼接一个对象时候，调用__str__方法
    在str一个对象时候，调用__str__方法
    当找不到__str__时会去找__repr__,功能是一样的，但在使用%r进行字符串拼接的时候只会去找repr
    """
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

    def __str__(self):
        return self.name + '\t' + str(self.price) + '\t' + self.period
# python = MyCourse('python', 200, '6mouth')
# go = MyCourse('go', 100, '2mouth')
# linux = MyCourse('linux', 900, '9mouth')
# lst = [python, go, linux]
# print(python)
# print('以下是课程详情%r' % python)
# str(go)
# for index, c in enumerate(lst, 1):
#     print(index, c)


def my_multiprocessing(name):
    """
    进程：进行中的程序就是一个进程，占用资源，需要操作系统调度，pid：能够唯一标识一个进程，但不是永久不变的，启动后结束前是固定的
    进程是计算机中最小的资源分配单位
    并发：多个程序同时执行：只有一个cpu，多个程序在一个CPU上执行
    宏观上多个程序同时执行
    微观上多个程序轮流在一个cpu上执行，本质还是串行
    并行：多个程序同时执行，并且在多个cpu上执行
    同步：在做A事的时候发起B事件，必须等待B事件结束之后才能继续做A事
    异步：在做A事的时候发起B事件，不需要等待B事件结束就可以继续A事件
    阻塞：cpu不工作了就叫阻塞，input，sleep
    非阻塞：cpu在工作就是非阻塞
    线程：线程是进程的一个单位，不能脱离进程存在
    线程事计算机中能够被cpu调度的最小单位
    同步阻塞：input，recv，accept
    进程的调度算法：给所有的进程分配资源或者分配cpu使用权的一种方法
    短作业优先，
    先来先服务，FIFS
    多级反馈算法：
    对个任务队列，优先级从高到低
    新来的任务总是优先级最高的
    每一个新任务几乎会立即获得一个时间片时间
    执行完一个时间片之后会降到下一级队列中
    总是优先级最高的任务都执行完才执行优先级低的队列
    并且优先级越高时间片越短
    多进程间的数据是隔离的
    :return:
    """
    print('进程id:', os.getpid(), '父进程id:', os.getppid(), name)   # 进程id和父进程id
    time.sleep(random.random())
    print('执行完毕')


# if __name__ == '__main__':  # Mac上不用这句，windows必须要，否则会报错
#     my_multiprocessing('hh')   # 父进程
#     p = Process(target=my_multiprocessing, args=('luhu',))  # 子进程可以传递参数，但必须以元组的方式传递，但是不能获取子进程的返回值
#     p.start()    # 开启一个子进程
#     p.join()   # 同步阻塞，直到p这个子进程执行完毕才继续执行后面代码
#     print('程序结束')
# if __name__ == '__main__':
#     arg_lst = [('zz',), ('aa',), ('cc',)]
#     p_lst = []
#     for i in arg_lst:
#         p = Process(target=my_multiprocessing, args=i)
#         p.start()
#         p_lst.append(p)
#         for j in p_lst:
#             j.join()
# print('多进程执行完毕')


n = 0


def func():
    """
    多进程间的数据是隔离的
    :return:
    """
    global n
    n += 1
#
#
# p_lst = []
# for i in range(100):
#     p = Process(target=func)
#     p.start()
#     p_lst.append(p)
#     for p in p_lst:
#         p.join()
#         print(n)
#
# print(n)


class MyProcess(Process):
    """
    开启进程的另一种方式，面向对象的方式
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()

    def run(self):
        time.sleep(2)
        print(os.getppid(), os.getpid(), self.a, self.b, self.c)
# if __name__ == '__main__':
#     p = MyProcess(1, 2, 3)
#     p.start()
#     print(p.name)
#     print(p.is_alive())
#     p.terminate()  # 结束子进程，但不会立即结束，得等到系统响应,异步非阻塞
#     sleep(1)
#     print(p.is_alive())  # 查看进程是否活着


def shouhu_process():
    """
    主进程会等待所有的子进程结束，回收资源
    守护进程会等待主进程代码执行结束之后再结束,而不是整个主进程结束，和其他子进程结束无关
    :return:
    """
    while 1:
        print('in shouhu_process')
        time.sleep(1)


def shouhu_process2():
    for i in range(10):
        print('in shouhu_process2' + str(i))
        time.sleep(1)
# if __name__ == '__main__':
#     p1 = Process(target=shouhu_process)
#     print(p1.name)
#     p1.daemon = True   # 开启守护进程
#     p2 = Process(target=shouhu_process2)
#     print(p2.name)
#     p1.start()
#     p2.start()
#     time.sleep(5)
#     p2.join()


def lock_func(i, lock):
    # lock.acquire() # 拿钥匙
    # print('被锁起来的功能%s' % i)
    # time.sleep(1)
    # lock.release()  # 还钥匙
    with lock:   # 这样写法更简单
        print('被锁起来的功能%s' % i)
        time.sleep(1)
# if __name__ == '__main__':
#     lock = Lock()   # 互斥锁
#     for i in range(10):
#         p = Process(target=lock_func, args=(i, lock))
#         p.start()


def consumer(q, name):
    """
    生产者消费者模型：分布式操作模块celery用的就是这个，本质就是让生产者和消费者数据的效率达到平衡并且最大化的效率
    进程间的通信，可以通过multiprocess的queue获取值，先进先出
    put()   get()
    一次put，对应一次get，如果直接get，取不到值，进程会阻塞
    消费者通常取到数据之后还要进行某些操作
    同步阻塞：调用函数必须等待结果，cpu没有工作（input，sleep，connect）
    同步非阻塞：调用函数必须等待结果，cpu仍在工作，调用了一个高计算的函数strip，min，sorted
    异步阻塞：调用函数不需要立即获取结果，而是继续做其他的事情，在获取结果的时候不知先获取谁的，总之需要等（阻塞）、
    异步非阻塞：调用函数不需要获取结果也不需要等，start(),terminate()
    :return:
    """
    while 1:
        food = q.get()
        if food:
            print('%s吃了%s' % (name, food))
        else:
            break


def producer(q, name, food):
    """
    生产者通常放数据之前需要先通过某些代码来获取数据
    :param q:
    :return:
    """
    for i in range(10):
        foodi = food + str(i)
        print('%s生产了%s' % (name, foodi))
        q.put(foodi)
        time.sleep(1)


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=consumer, args=(q, 'luhu'))
    p2 = Process(target=producer, args=(q, 'dachu', 'cake'))
    p3 = Process(target=consumer, args=(q, '小明'))
    p1.start()
    p2.start()
    p3.start()
    p2.join()     # 等待生产者生产完再开始吃
    q.put(None)   # 有几个消费者就要put几次None
    q.put(None)


# ret = requests.get('https://www.baidu.com')
# print(ret.content.decode('utf-8'))





















