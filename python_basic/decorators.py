
# def hello(name="Jose"):
#     return "hello "+name
#
# print(hello())
#
# mynewgreet = hello
#
# print(mynewgreet())




# def hello(name="jose"):
#     print("the hello() function has been run!")
#
#     def greet():
#         return "this string is inside greet()"
#
#     def welcome():
#         return "this string is inside welcome"
#
#     if name == "jose":
#         return greet
#     else:
#         return welcome
#
# x = hello()
#
# print(x())



# def hello():
#     return "Hi Jose!"
#
# def other(func):
#     print("hello")
#     print(func())
#
# other(hello)


def new_decorator(func):
    def wrap_func():
        print("code here before executing func")
        func()
        print("func() has been called")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("this function is in need of decorator")

# func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()

