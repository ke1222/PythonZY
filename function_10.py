import random
a1 = random.randint(1,6)
a2 = random.randint(1,6)
a3 = a1+a2
if a3==2 or a3==3 or a3==12:
    print("你输了")
elif a3==7 or a3==11:
    print("你赢了")
else:
    for i in range(1,1000):
        a4 = random.randint(1,6)
        a5 = random.randint(1,6)
        a6 = a5+a4
        if a6 == 7:
            print("你输了")
            break
        elif a6 == a3:
            print("你赢了")
