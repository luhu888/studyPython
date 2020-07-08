import copy

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
        elif i%2 == 0:
           sum = sum - i
        else:
            sum = sum + i
    print(sum)


def is_palindrome():
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

        else:print(li[i])


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
        for i, j in enumerate(goods):
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
    reverse 将列表翻转过来
    列表相加相乘  + *
    :return:
    """
    li = [1, 2, 6, 7, 4, 9, 11]
    li2 = [2, 4, 3, 1, 10, 9]
    li.sort()
    print(li)


def list_delete():
    li = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    del li[1::2]
    print(li)



list_delete()
