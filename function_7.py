def distance(x1,y1,x2,y2):
    juli = ((x1-x2)**2+(y1-y2)**2)**0.5
    print("两点间距离为:",'%.2f'%juli)
def start():
    x1,y1 = eval(input("x1,y1:"))
    x2,y2 = eval(input("x2,y2:"))
    distance(x1,y1,x2,y2)
start()