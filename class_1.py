class Rectangle():
    def __init__(self):
        self.width = 4
        self.height = 40
        self.width1 = 3.5
        self.height1 = 35.7
    def getArea(self):
        mianji = self.width * self.height
        mianji1 = self.width1 * self.height1
        print("第一个矩形的面积为:",mianji)
        print("第二个矩形的面积为:",'%.2f'%mianji1)
    def getPerimeter(self):
        zhouchang = (self.width + self.height)*2
        zhouchang1 = (self.width1 + self.height1)*2
        print("第一个矩形的周长为:",zhouchang)
        print("第二个矩形的周长为:",zhouchang1)
if __name__ == "__main__":
    a = Rectangle()
    a.getArea()
    a.getPerimeter()



