
class Dog():

    # CLASS OBJECT ATTRIBUTES

    species = "mammal"

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog('lab','sammy')

print(mydog.breed)
print(mydog.name)
print(mydog.species)
