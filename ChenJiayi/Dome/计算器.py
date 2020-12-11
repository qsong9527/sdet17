import re
print("欢迎使用计算器v1.0(v1.0版本仅支持两个整数之间的加减乘除运算)\n", "_"*45)
print("(加号用+)(减号用-)(乘号用*)(除号用/)")
while True:
    string = input("请输入您需要的计算：")
    sz = re.compile(r"\d+")
    jc = re.compile(r"^\d+(\+|\-|\*|\/){1}\d+$")
    t = sz.findall(string)
    jg = jc.findall(string)
    if len(jg) == 1:
        pass
    else:
        print("您的输入有误导致系统崩溃,请重新输入！")
        continue
    try:
        x = int(t[0])
        y = int(t[1])
    except Exception as result:
        print("您的输入有误导致系统崩溃,请重新输入！")
        continue
    if "+" in string:
        print(x, "+", y, "=", x+y)
    elif "-" in string:
        print(x, "-", y, "=", x-y)
    elif "*" in string:
        print(x, "×", y, "=", x*y)
    elif "/" in string:
        print(x, "÷", y, "=", "%f.2"%(x/y))
    else:
        print("未检测出您有使用运算符！")