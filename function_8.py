def sushu():
    i = 2
    c = []
    d = []
    while i <=31:
        j = 2
        while j <= i:
            if i % j ==0:
                if i == j:
                    c.append(i)
                break
            j += 1
        i += 1
    print(c) 
    for p in c:
        d.append(2**p-1) 
    print(d)    
sushu()
