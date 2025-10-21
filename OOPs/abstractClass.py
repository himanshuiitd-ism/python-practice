#Abstract class: class that can't be instantiated on it's own . meant to be subclass

#contain methods that are declared but are not implemented 
#Abstract class benefits:
#1. Prevents instantiation of the class itself 
#2. Requires children to use inherited abstract method
#In programming, instantiation refers to the process of creating  a specific object from a class. Think of a class as a blueprint (like for a car), and instantiation as building an actual car based on that blueprint.

# means they themselves can't use their methods but their children can

# to declare abstract method we need to use a decorator (@)

#we need to finish defining abstract methods in children

from abc import ABC,abstractmethod  # abc means abstact based class

class Vehicle(ABC):

  @abstractmethod
  def run(self):
    pass

  @abstractmethod
  def stop(self):
    pass

class Car(Vehicle):
  def run(self):
    print("You drive the car")
  
  def stop(self):
    print("You stop the car")

  def go(self):
    print("Go")

car = Car()
car.run()
car.stop()
car.go()

# atleast those method which are present in parent(abstract) must also present in children

#for using methods of parent 