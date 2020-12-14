
def add(a, b):

    print("我是一个加法函数，我可以计算传入的a,b两个数字的和")
    result = a + b
    print(f"{a} + {b} = {result}")

def compare(a, b):
    print("我是一个比较大小的函数，我可以判断传入的a,b两个数字的大小关系")
    if a > b:
        print(f"{a} > {b}")
    elif a < b:
        print(f"{a} < {b}")
    else:
        print(f"{a} = {b}")




add(2, 3)



