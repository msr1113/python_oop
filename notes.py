#lcoal

# lambda x : x**2

#enclosing function lcoals

name = 'this is a global name!'

def greet():
    name = "Sammy"
    print(name)

    def hello():
        print("hello " + name)

    hello()

print(greet())

print(name)