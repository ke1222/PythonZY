class Fan(object):
    def __init__(self,speed = 1,on = False,radius = 5,color = "blue"):
        self._speed = speed
        self._on = on
        self._radius = radius
        self._color = color

    @property #装饰器
    def speed(self):
        return self._speed  
    @speed.setter #修改器
    def speed(self,speed1):
        self._speed = speed1
    
    @property #装饰器
    def on(self):
        return self._on  
    @on.setter #修改器
    def on(self,on1):
        self._on = on1
    @property #装饰器
    def radius(self):
        return self._radius 
    @radius.setter #修改器
    def radius(self,radius1):
        self._radius = radius1
    @property #装饰器
    def color(self):
        return self._color 
    @color.setter #修改器
    def color(self,color1):
        self._color = color1

if __name__ == "__main__":
    fan = Fan(3,True,10,"yellow")
    print("风速:",fan._speed,"\n","是否打开:",fan._on,"\n","半径:",fan._radius,"\n","颜色:",fan._color)
    fan1 = Fan(2,False,5,"blue")
    print("风速:",fan1._speed,"\n","是否打开:",fan1._on,"\n","半径:",fan1._radius,"\n","颜色:",fan1._color)
