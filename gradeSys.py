# You are creating a student grading system. Each student has a private attribute __grade
# representing their score. The class Student should have methods set_grade(grade) to
# update the score, get_grade() to view it, and display_info() to show the student’s name
# and grade. Students should create student objects, update grades using setters, retrieve
# them using getters, and understand how encapsulation keeps the grade secure from
# direct modification.

class Student:
    def __init__(self,name):
        self.name=name
        self.__grade=0
    def set_grade(self,grade):
        self.__grade=grade
    def get_grade(self):
        return self.__grade
    def display_info(self):
        print("Name: ",self.name)
        print("Grade: ",self.__grade)
s1=Student("Ahmed")
s1.set_grade(90)
g1=s1.get_grade()
print("Grade: ",g1)
s2=Student("Ali")
s2.set_grade(85)
s2.display_info()