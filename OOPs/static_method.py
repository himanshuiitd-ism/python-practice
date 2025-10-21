# Static method = A method that belongs to a class rather than any object from that class (instance). Usually used for general utility functions 

# Instance method = Best for operations on instance of the class(object)
# Ex: def get_info(self):
#         return f"{self.name} = {self.position}"

# Static method = Best for utility functions that do not need access to class data

#jo bhi fxn ka start self se hota hai wo obj hota hai . ex: def fxn(self):

class Employee:
  def __init__(self,name,position):
    self.name = name
    self.position = position

  def get_info(self):
    return f"{self.name} {self.position}"
  
  @staticmethod
  def is_valid_position(position):
    valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
    return position in valid_positions
  
employee = Employee.is_valid_position("Scientist")
print(employee)
employee = Employee.is_valid_position("Cook")
print(employee)

employee1 = Employee("Himanshu","Founder Ceo Market Expert")
employee2 = Employee("Himani","Janator")
print(employee2.get_info())