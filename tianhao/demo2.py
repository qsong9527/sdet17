a=int(input("请输入一个年份"))
if a%4==0 and a%100!=0:
    print(f"{a}是闰年")
elif a%400==0:
    print(f"{a}是世纪闰年")
else:
    print(f"{a}是平年")