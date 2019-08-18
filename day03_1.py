
zhengshu = 0
fushu = 0
he = 0
zero = 1
while zero != 0:
    zero = eval(input("输入整数"))
    if zero > 0:
        zhengshu += 1
    elif zero < 0:
        fushu += 1
    else:
        break
    he += zero
print(float(he / (zhengshu + fushu)))

