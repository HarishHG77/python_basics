class Student:
    def __init__(self,r,n):
        self.rollno=r
        self.name=n
    def display(self):
        print("rollno of student="+str(self.rollno))
        print("name of student="+self.name)
s=Student(417,"harish")
s.display()