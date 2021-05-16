#################################################
#-------------------Decorators------------------#
#################################################

# def myDecorator(func): # Decorator
#     def nestedFunc(): 
#         print("Before Decoration")
#         func()
#         print("After Decoration")
#     return nestedFunc


# @myDecorator
# def sayHello():
#     print("Hello")

# sayHello()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# def myDecorator(func):
#     def nestedFunc(*numbers):
#         for number in numbers:            
#             if number < 0:
#                 print("One of the Numbers is less than Zero")
#         func(*numbers)
#     return nestedFunc

# @myDecorator
# def calculate(n1, n2, n3):
#     print(n1 + n2 + n3)

# calculate(-5,10,50)

#---------------------------------------------------------------------------------------------------------------------------------------------#

from time import time

def speedTest(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Function runtime is: {end - start}")
    return wrapper

@speedTest
def bigLoop():
    for number in range(1,40001):
        print(number)

bigLoop()