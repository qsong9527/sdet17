# 闰年：
# 公历年份为4的倍数，且不是100的倍数，为普通闰年
#  （如2004年、2020年就是闰年）
# 世纪闰年：公历年份是整百数的，必须是400的倍数才是闰年
#   （如1900年不是世纪闰年，2000年是世纪闰年）

# 闰年判断器
year = int(input("请输入年份:"))
if year > 0:
   if year % 400 == 0:
      print(f"{year} 是一个世纪闰年")
   else:
      if year % 100 == 0:
         print(f"{year} 是一个平年")
      else:
         if year % 4 == 0:
            print(f"{year} 是一个普通闰年")
         else:
            print(f"{year} 是一个平年")
else:
     print("公历以前的事情，俺也不知道")

# 补充，如果使用 and 的情况下：
#if(year % 100 == 0) and (year % 400 == 0):
#   print(f"{year} 是普通闰年")
#elif(year % 100 == 0) and (year % 400 == 0):
#   print(f"{year} 是世纪闰年")
#else:
#   print(f"f{year} 不是闰年)