class Animal:        # Creation of a super class, Animal
  def __init__(self, name):        # Initializes attributes of the parent class
    self.name = name        # Creation of a new attribute, self.name

  def feed(self):        # Creation of a new method, feed(self)
    return self.feed     # Returns the new method, self.feed

  def make_sound(self):        # Creation of a new method, make_sound(self)
    return self.make_sound        # Returns the new method, self.make_sound

class Lion(Animal):        # Creation of a new sub class, Lion(Animal)
  def make_sound(self):        # Inherits and overrides the parent method, make_sound(self)
    return f"{self.name} roars loudly!"

  def feed(self):        # Inherits and overrides the parent method, feed(self)
    return f"{self.name} eats fresh meat."

class Elephant(Animal):        # Creation of a new sub class, Elephant(Animal)
  def make_sound(self):        # Inherits and overrides the parent method, make_sound(self)
    return f"{self.name} trumpets!"

  def feed(self):        # Inherits and overrides the parent method, feed(self)
    return f"{self.name} eats grass and fruit."

class Monkey(Animal):        # Creation of a new sub class, Monkey(Animal)
  def make_sound(self):        # Inherits and overrides the parent method, make_sound(self)
    return f"{self.name} chatters!"

  def feed(self):        # Inherits and overrides the parent method, feed(self)
    return f"{self.name} eats banana."



# Creation of objects
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.feed())
print("-----")

print(elephant.make_sound())
print(elephant.feed())
print("-----")

print(monkey.make_sound())
print(monkey.feed())
print("-----")
