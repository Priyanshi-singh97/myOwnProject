#def decorators(func):
#    def wrapper():
#        print("before")
#        func()
#        print("after")
#    return wrapper

#def say_hello():
#    print("execution")

#say_hello=decorators(say_hello)

#say_hello()



def decorators(func):
    def warapper():
        print("before")
        func()
        print("after")
    return warapper

@decorators
def say_hello():
    print("exection")

say_hello()
