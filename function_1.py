    
def getPentagonalNumber(n):
    count = 0
    for n in range(1,101):
        n = n*(3*n-1)/2
        count += 1 
        print(n,end = " ")
        if count % 10 == 0 :
            print('\n')       
def start():
    n = 1
    getPentagonalNumber(n)    
start()
