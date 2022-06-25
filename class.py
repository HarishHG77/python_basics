class Student:
    def init(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def display(self):
        print(str(self.rollno))
        print(self.name)
s=Student()
s.init(123,"hari")
s.display()
