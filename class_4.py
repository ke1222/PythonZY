import math

class RegularPolygon(object):
    def __init__(self,n = 3,side = 1,x = 0,y = 0):
        self._n = n
        self._side = side
        self._x = x
        self._y = y

    @property #装饰器
    def n(self):
        return self._n  
    @n.setter #修改器
    def n(self,n1):
        self._n = n1
    
    @property #装饰器
    def side(self):
        return self._side 
    @side.setter #修改器
    def side(self,side1):
        self._side = side1
    
    @property #装饰器
    def x(self):
        return self._x 
    @x.setter #修改器
    def x(self,x1):
        self._x = x1
    
    @property #装饰器
    def y(self):
        return self._y 
    @y.setter #修改器
    def y(self,y1):
        self._y = y1
    def getPerimerter(self):
        return self.n*self.side
    def getArea(self):
        return self.n * self.side ** 2 / (4 * math.tan(math.pi / self.n))
if __name__ == "__main__":
    rp1 = RegularPolygon()
    print("周长为:",'%.2f'%rp1.getPerimerter())
    print("面积为:",'%.2f'%rp1.getArea())
    print("---------------------------------------")
    rp2 = RegularPolygon(6,4)
    print("周长为:",'%.2f'%rp2.getPerimerter())
    print("面积为:",'%.2f'%rp2.getArea())
    print("---------------------------------------")
    rp3 = RegularPolygon(10,4,5.6,7.8)
    print("周长为:",'%.2f'%rp3.getPerimerter())
    print("面积为:",'%.2f'%rp3.getArea())
    
    
    