class Student:
    total_count = 0  ## Class Variables
    class_year = 2026

    def __init__(self,name,age):
        self.name = name       ## Instance variables
        self.age = age
        Student.total_count +=1

student1 = Student("Inaya",4)
student2 = Student("Jameel",33)
student3 = Student("Heena",30)

print(f"My class total count is : {Student.total_count} , the class year is {Student.class_year}")  ## accessing a class variable "class."