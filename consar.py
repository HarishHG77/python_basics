#finding area of circle using constructor
class Circle():
    def __init__(self,rad):
        self.r=rad
    def calc(self):
        area=3.142*self.r*self.r
        print("area of circle="+str(area))
c=Circle(6)
c.calc()