import random
def yb(num2):
    list = [0,1]
    num1 = random.choice(list)
    if num2 == num1:
        print("猜测正确")
    else:
        print("猜测错误")   
def start():
    num2 = int(input("请输入0或1"))
    yb(num2)
start()