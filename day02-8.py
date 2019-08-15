import random
def game(num2):
    num1 = random.randint(1,3)
    print(num1)
    if num1 == num2 :
        print ("平局")
    elif num1 == 1 and num2 == 2:
        print("电脑胜")
    elif num1 == 1 and num2 == 3:
        print("你胜")
    elif num1 == 2 and num2 == 1:
        print("你胜")
    elif num1 == 2 and num2 == 3:
        print("电脑胜")
    elif num1 == 3 and num2 == 1:
        print("电脑胜")
    else :
        print("你胜")    
def start():
    num2 = int(input("输入石头(1)剪刀(2)布(3)"))
    game(num2)   
start()