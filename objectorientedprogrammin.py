class student:
    student_name=""
    student_age=0
    student_marks=0

    def __init__(self):#1st function  is a constructor
        print("constructor called")


    def set_student_name(self,name):#second function takes the parameter name and sets it to the
        self.student_name=name

    def display_student_name(self):#third function displays the student name
        print("student:",self.student_name)

student1=student()
student1.set_student_name("dan")
student1.display_student_name()

class student:
    student_name=""
    student_age=0
    student_marks=0


    def __init__(self,name,age,marks):
        self.student_name=name
        self.student_age=age
        self.student_marks=marks
        print("constructor called")

    def display_student_details(self):
        print("std name",self .student_name,"age:",self.student_age,"marks:",self.student_marks)

student1=student(name="dan",age="50",marks="80")
student1.display_student_details()






