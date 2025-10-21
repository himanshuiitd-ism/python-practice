class Student:
  count = 0
  total_gpa = 0

  def __init__(self,name,gpa):
    self.name = name
    self.gpa = gpa
    Student.count += 1
    Student.total_gpa += gpa

  #Instance method
  def get_info(self):
    return f"{self.name} {self.gpa}"
  
  @classmethod
  def get_count(cls):
    return f"Total number of students : {cls.count}"
  
  @classmethod
  def get_avg_gpa(cls):
    if cls.count == 0:
      return 0 
    else:
      return f"Average gpa of class is : {cls.total_gpa/cls.count:.2f}"
    

student1 = Student("Himanshu",8.5)
student2 = Student("Himani",10)
student3 = Student("Ram",8)

print(Student.get_count())
print(Student.get_avg_gpa())
print(student1.get_info())