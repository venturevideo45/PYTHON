class parrot:
  
  species = "bird"
  def __init__(self, name, age):
    self.name = name
    self.age = age

Crackers = parrot("Crackers", 10)
oxford = parrot("Oxford", 15)

print(Crackers.name, "is a", Crackers.species, "and is", Crackers.age, "years old.")

print(oxford.name, "is a", oxford.species, "and is", oxford.age, "years old.")