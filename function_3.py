def displaySortedNumbers(num1,num2,num3):
    list = [num1,num2,num3]
    a = sorted(list)
    print(a)
def start():
    num1,num2,num3 = eval(input("Enter three numbers:"))
    displaySortedNumbers(num1,num2,num3)
start()