"""a,b,c = eval(input("Enter a,b,c"))
p = (b**2 - 4*a*c)
r1 = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a)
r2 = (-b - ((b**2 - 4*a*c)**0.5)) / (2*a)
if p > 0:
    print("The roots are",'%.2f'%r1,"and",'%.2f'%r2)
elif p == 0:
    print("The root is ",'%.2f'%r1)
else:
    print("The equation has no real roots")
"""

def shu():
    a,b,c = eval(input("Enter a,b,c"))
    p = (b**2 - 4*a*c)
    r1 = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a)
    r2 = (-b - ((b**2 - 4*a*c)**0.5)) / (2*a)
    if p > 0:
        print("The roots are",'%.2f'%r1,"and",'%.2f'%r2)
    elif p == 0:
        print("The root is ",'%.2f'%r1)
    else:
        print("The equation has no real roots")
def start():
    shu()
    
start()
