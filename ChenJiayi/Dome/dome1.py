import datetime
name = input("请输入您的名字：")
x = 0;
while x == 0:
    try:
        age = int(input("请输入您的年龄："))
        x = 1
    except ValueError:
        print("您的输入不正确请重新输入！")
curr_time = datetime.datetime.now()
if 8 <= curr_time.hour < 12:
    print("我叫{0}，今年{1}岁了，大家早上好！".format(name, age))
elif 12 <= curr_time.hour < 14:
    print("我叫{0}，今年{1}岁了，大家中午好！".format(name, age))
elif 14 <= curr_time.hour < 20:
    print("我叫{0}，今年{1}岁了，大家下午好！".format(name, age))
else:
    print("我叫{0}，今年{1}岁了，大家晚上好！".format(name, age))




























