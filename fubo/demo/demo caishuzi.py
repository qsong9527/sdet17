import random
r = random.randint(1,100)
while True :
    p = input (f"请输入一个数字")
if r > p  :
    print("数字小了")
elif r < p  :
    print("数字大了")
else: r = p
print ("恭喜你，答对了")

