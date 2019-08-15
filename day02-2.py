import random
"""num1 = random.randint(1,100)
num2 = random.randint(1,100)
print(num1,num2)
num = int(input("请输入俩数之和"))
if num == (num1 + num2):
    print("结果为真")
else:
    print("结果为假")
"""
def zs(num):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    if num == (num1 + num2):
        print("结果为真")
    else:
        print("结果为假")   
def start():
    num = int(input("请输入俩数之和"))
    zs(num)
start()