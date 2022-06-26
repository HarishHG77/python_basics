class Circle:
    def init(self,radius):
        self.radius=radius
    def calc(self):
        area=3.142*self.radius*self.radius
        print("area of circle="+str(area))
c=Circle()
c.init(5)
c.calc
#or
x=input("enter radius of a circle")    
radius=int(x)                         
c=Circle()
c.init(radius)
c.calc()