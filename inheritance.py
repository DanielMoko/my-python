class people:
    age = ""
    name = ""
    def __init__(self,name,age):
        self.name = name
        self.age= age

    def printpeople(self):
        print("the  people details are :",self.name,self.age)

    #child class

class Student(people):
    uniform= ""

    def __init__(self,name,age,uniform):
        super().__init__(name, age)
        self.uniform= uniform
    def printstudent(self):
        print("the student details are :",self.name,self.age,self.uniform)

student1=Student("cheb",30,"blue")
student1.printstudent()
student1.printpeople()
