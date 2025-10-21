# class Car: #Car object
#   #attributes defining
#   def __init__(self, model, year, color, for_sale):  
#     self.model = model
#     self.year = year
#     self.color = color
#     self.for_sale = for_sale

#   #methods are action that an object can perform .like car object can perform following action
#   #methods are fxn that belong to an object
#   def drive(self):
#     print(f"You drive the {self.color} {self.model}")
#   def stop(self):
#     print(f"You stop the {self.color} {self.model}")
#   def describe(self):
#     print(f"{self.model} {self.color} {self.year}")


class Student:
  class_year = 2024 #this is class variable (defined outside constructo and remain same for every student)
  no_of_student = 0

  def __init__(self,name,age): #name and age are instance variable (diff for every obj)
    self.name = name
    self.age = age
    Student.no_of_student+=1

student1 = Student("Himanshu",21)
student2 = Student("Himani",15)
# print(student1.name)
# print(student2.class_year)
# print(Student.class_year)
print(f"My graduating class of {Student.class_year} has {Student.no_of_student} students")  #this is way for using class variable 