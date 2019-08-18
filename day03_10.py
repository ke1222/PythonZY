for i in range(1,10000):
    res = 0
    for j in range(1,i):
        if i % j == 0:
            res += j
    if i == res:
        print(i)