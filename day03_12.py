
he = 0
zero = 0
mean = 0
dev = 0
sum1 = 0
for i in range(10):
    zero = eval(input("输入10个数"))
    he += zero
    mean = he / 10
    sum1 += (zero - mean)**2
    dev = (sum1 / 9)**0.5
print("The mean is ",'%.2f'%mean)
print("The standard deviation is ",dev)