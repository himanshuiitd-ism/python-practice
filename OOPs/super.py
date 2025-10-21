# super() = fxn used in a class to call methods from parent class

class Shape:
  def __init__(self,color,is_filled):
    self.color = color
    self.is_filled = is_filled

  def describe(self):
    print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
  def __init__(self, color, is_filled,radius):
    super().__init__(color,is_filled)
    self.radius = radius
  
  def describe(self):
    print(f"Circle is {self.color} in color and {'filled' if self.is_filled else 'not filled'} and area is {3.14*self.radius*self.radius}cm^2")  #this describe method will be used bcoz this is method overRighting (child> parent)

    #now if I want to use parent's escribe method as well then I will use super method ,we are extending the functionality
    super().describe()

class Square(Shape):
  def __init__(self, color, is_filled,width):
    super().__init__(color,is_filled)
    self.width = width
  
  def describe(self):
    print(f"Circle is {self.color} in color and {'filled' if self.is_filled else 'not filled'} and area is {self.width*self.width}cm^2")
    super().describe()

circle = Circle("Red", True , 5)
square = Square("Green",False , 6)

# circle.describe()
square.describe()

#Allows you to extend the functionality of inherited methods
#basically constructor use krne ke lea parent ka (bina define kea)