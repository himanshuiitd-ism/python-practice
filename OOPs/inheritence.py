class Animal:
  def __init__(self,name):
    self.name = name
    self.is_alive = True #ye sb ke lea same rhega
  
  def eat(self):
    print(f"{self.name} is eating!")
  def sleep(self):
    print(f"{self.name} is sleeping")
  def running(self):
    print(f"{self.name} is sleeping")

class Dog(Animal):
  def speak(self):
    print("Woof!")
class Cat(Animal):
  pass

dog1 = Dog("Scooby")
cat1 = Cat("Jefry")
# print(dog1.name)
# dog1.speak()
# dog1.sleep()
# print(cat1.name)

#multilevel inheritence
class Prey(Animal):
  def flee(self):
    print(f"{self.name} flees")

class Predator(Animal):
  def hunt(self):
    print(f"{self.name} hunts")

class Rabbit(Prey):
  pass
class Hawk(Predator):
  pass
class Fish(Prey,Predator):
  pass

rabbit = Rabbit("Snow")
hawk = Hawk("Tony")
fish= Fish("Nemo")

# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()
# fish.eat()
