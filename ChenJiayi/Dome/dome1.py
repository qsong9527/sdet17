name = input("请输入您的名字：")
x = 0;
while x == 0:
    try:
        age = int(input("请输入您的年龄："))
        x = 1
    except ValueError:
        print("您的输入不正确请重新输入！")
print("我叫{0}，今年{1}岁了，大家早上好！".format(name, age))
print("我叫{0}，今年{1}岁了，大家中午好！".format(name, age))
print("我叫{0}，今年{1}岁了，大家晚上好！".format(name, age))





























