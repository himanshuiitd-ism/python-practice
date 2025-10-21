class Company:
  class Employee:
    def __init__(self,name,position):
      self.name = name
      self.position = position

    def get_details(self):
      return f"{self.name} {self.position}"
    
  def __init__(self,company_name):
    self.company_name = company_name
    self.employees =[]  #left side me kuch bhi name use kr skte hai ,but right side me agr use krte hai to wo constructor variable hona chahie

  def add_employee(self,name,position):
    new_employee = self.Employee(name,position)
    self.employees.append(new_employee)

  def list_employees(self):
    return [employee.get_details() for employee in self.employees]
  
company = Company("Tata")
company2 = Company("tripiitrip")

company.add_employee("Raghav","Manager")
company.add_employee("Rahul","Chief Security")
company.add_employee("Sweta","PA")

company2.add_employee("Himanshu","Founder")
company2.add_employee("Mannan","AI_Engineer")
company2.add_employee("Aditya Jain","AI Engineer and Marketing analyst")

# for emp in company.list_employees():
#   print(emp)

for emp in company2.list_employees():
  print(emp)