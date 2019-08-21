class LinearEquation(object):
    def __init__(self,a=0,b=0,c=0,d=0,e=0,f=0):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f
    @property
    def geta(self):
        return self._a
    @property
    def getb(self):
        return self._b

    @property
    def getc(self):
        return self._c

    @property
    def getd(self):
        return self._d

    @property
    def gete(self):
        return self._e
    @property
    def getf(self):
        return self._f    
    def getX(self,a,b,c,d,e,f):
        x = (e * d - b * f) / (a * d - b * c)
        return x
    def getY(self,a,b,c,d,e,f):
        y = (self._a * self._f - self._e * self._c) / (self._a * self._d - self._b * self._c)
        return y
if __name__ == "__main__":
    le = LinearEquation()
    le.a,le.b,le.c,le.d,le.e,le.f = eval(input("输入6个值:"))
    if le.a * le.d - le.b * le.c != 0:
        print(le.getX(),le.getY()) 
    else:
        print("这个方程式无解")