import random
x = 1
while x <=10:
    r = random.randint(1,100)
    print(f"{x}随机数:{r}")
    x += 1
print("打印完毕")