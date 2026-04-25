class Empyloyee :
    Species = "Human"
    def __init__(self, name, age, gender):
         self.name = name
         self.age = age
         self.gender = gender

    def __del__(self):
        print("Destructor called, Empyloyee deleted")


Empyloyee1 = Empyloyee("Jayanth", 16, "Male")

print(Empyloyee1.name)
print(Empyloyee1.age)
print(Empyloyee1.gender)
del Empyloyee1




    

