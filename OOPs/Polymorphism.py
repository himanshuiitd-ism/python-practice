# Polymorphism = Greek word that means to "have many forms or faces"
#               Poly=Many
#               Morphe = Form

# Two ways to achieve polymorphism
# 1. Inheritence = An obj couuld be treated of the same type as a parent class
# 2. "Duck Typing" = obj must have necessary attributes/methods

from abc import ABC,abstractmethod

class Shapes(ABC):
  @abstractmethod
  def area(self):
    pass

class Circle(Shapes):
  def __init__(self,radius):
    self.radius = radius

  def area(self):
    return 3.14*self.radius*self.radius

class Square(Shapes):
  def __init__(self,side):
    self.side = side
  
  def area(self):
    return self.side**2
  
class Triangle(Shapes):
  def __init__(self,base,height):
    self.base = base
    self.height = height

  def area(self):
    return 0.5*self.base*self.height
  
class Pizza(Circle):
  def __init__(self,topping,radius):
    super().__init__(radius)
    self.topping = topping

  def area(self):
    return 3.14*self.radius*self.radius
  


shapes = [Circle(4),Square(5),Triangle(6,7),Pizza("chicken",8)]
for shape in shapes:
  print(f"{shape.area()}cm^2")