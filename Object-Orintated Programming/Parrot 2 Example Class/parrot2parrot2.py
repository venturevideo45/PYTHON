class parrot:
  species = "bird"
  def __init__(self, name, age):
      self.name = name
      self.age = age

  def sing(self, song):
      return "{} sings {}".format(self.name, song)
    
  def dance(self, style):
        return "{} dances {}".format(self.name, style)
    
Crackers = parrot("Crackers", 10)

print(Crackers.sing("Happy Birthday"))
print(Crackers.dance("Pop"))