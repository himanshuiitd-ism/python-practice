# "Duck Typing" = Another way to achieve polymorphism besides inheritence.
# Object must have the minimum necessary attributes/methods 
# "If it looks like a duck and quacks like a duck , It must be a duck ."

class Animal:
  alive = True

class Dog(Animal):
  def speak(self):
    print("Woof")

class Cat(Animal):
  def speak(self):
    print("Meow")

class Car:
  alive = False

  def speak(self):
    print("Bhroom")

animal = [Dog(),Cat(),Car()]
for i in animal:
  i.speak()
  print(i.alive)