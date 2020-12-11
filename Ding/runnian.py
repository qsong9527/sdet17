# 判断一个数字是否为基数
#      基数: 不能被2整除的数字
# 闰年
year = int(input("请输入一个年份："))
if year > 0:
    if (year % 4) == 0:
        if (year % 100)== 0:
            if (year % 400) == 0:
                print("{0} 是闰年")
            else:
                print("{0} 不是闰年")
        else:
            print("{0} 是闰年")
    else:
        print("{o} 不是闰年")
else:
    print(f"{year}小于0，错误！！！")
