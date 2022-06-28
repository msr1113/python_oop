class Animal():

    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print('eating')

class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print("DOG CREATED")

    def bark(self):
        print('woof')

    def eat(self):
        print('dog eating')

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()