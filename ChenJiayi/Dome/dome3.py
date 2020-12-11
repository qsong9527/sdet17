number = input("请输入您要查询的年份：")
if number % 4 == 0 and number % 100 != 0:
    print("{0}是润年")
elif number % 100 == 0 and number % 400 == 0:
    print("{0}是世纪润年")
else:
    print("{0}不是润年")






















