# 需求：
#  输入两个数字，输出两个数字的大小关系
# 例：
# > 请输入数字1：7     (8           (6
# > 请输入数字2：8     (8           (3
# >   7 < 8          (8 = 8       ( 6 > 3

a = int(input("请输入数字1："))
b = int(input("请输入数字2："))

if a > b:
    print(f"{a} > {b}")
elif a < b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")

# if a == b:
#     print(f"{a} = {b}")
# else:
#     if a > b:
#         print(f"{a} > {b}")
#     else:
#         print(f"{a} < {b}")
