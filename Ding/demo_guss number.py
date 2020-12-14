


import random

r = random.randint(1,100)

while True:
    num= int(input("请猜一个100以内的整数数字并输入"))
    if(num>r):
        print("大了")
    elif(num<r):
        print("小了")
    else:
        print("你猜对了")
        break
    



