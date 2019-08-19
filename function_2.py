def sumDigits(n):
    sum = 0
    m = str(n)
    for i in range(len(m)):
        num = n//10**i%10
        sum += num    
    print(sum)
def start():
    n = int(input("输入一个整数:"))
    sumDigits(n)
start()