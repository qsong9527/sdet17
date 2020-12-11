#  数字大小比较器

num1 = int(input("请输入第一个数字"))
num2 = int(input("请输入第二个数字"))

if num1 == num2:
    print(f"{num1}与{num2}相等")
# elif______:  可以插入需要“另外如果的情况”
# 通过使用if、elif与else的搭配即可完成三者之间的比价
# 而不用去做两个if、else的嵌套
else:
    if num1 > num2:
      print(f"{num1}比{num2}要大")
    else:
      print(f"{num1}比{num2}要小")