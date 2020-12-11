number = int(input("请输入您要查询的年份："))
if number % 4 == 0 and number % 100 != 0:
    print(f"{number}是润年")
elif number % 100 == 0 and number % 400 == 0:
    print(f"{number}是世纪润年")
else:
    print(f"{number}不是润年")






















