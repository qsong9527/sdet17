year= int(input("请输一个年份："))
if year > 0:
    if (year % 400 == 0) and (year % 4 != 0):
        print(f"{year}是一个普通闰年")
    elif (year % 400 == 0) and (year % 100 == 0):
        print(f"{year}是一个世纪闰年")
    else:
        print(f"{year}不是闰年")
else:
    print(f"{year}小于零，错误！！！")
