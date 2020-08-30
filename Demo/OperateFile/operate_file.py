def canshu5(name, age, hight, sex='男'):
    with open('test1.txt', encoding='utf-8', mode='a') as f1:
        f1.write('{}|{}|{}|{}\n'.format(name, age, hight, sex))


while 1:
    name = input('请输入姓名：')
    if name.upper() == 'Q':
        break
    age = input('请输入年龄：')
    hight = input('请输入身高：')
    sex = input('请输入性别：')
    if sex == '':
        canshu5(name, age, hight)
    else:
        canshu5(name, age, hight, sex)



