#################################################
#-------------------Decorators------------------#
#################################################

def myDecorator(func): # Decorator
    def nestedFunc(): 
        print("Before Decoration")
        func()
        print("After Decoration")
    return nestedFunc


@myDecorator
def sayHello():
    print("Hello")

sayHello()

#---------------------------------------------------------------------------------------------------------------------------------------------#


