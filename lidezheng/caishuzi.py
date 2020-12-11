import random
r = random.randint(1,100)
whlie true:
    user_input=int(input("请输入一个数："))
    if user_input > r:
        print("你输入的数大了")
    elif user_input < r:
        print("你输入的数小了")
    else:
        print("你答对了")
break
