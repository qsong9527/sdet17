year= int(input("请输一个年份："))
if year > 0:
    if year % 400 != 0:
        if year % 100 != 0:
            if year % 4 == 0:
                print(f"{year}是一个闰年")
            else:
                print(f"{year}不是一个闰年")
        else:
            print(f"{year}不是一个闰年")
    else:
        print(f"{year}是世纪闰年")
else:
    print(f"{year}小于零，错误！！！")
