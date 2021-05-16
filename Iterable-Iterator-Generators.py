#################################################
#--------------Iterable & Iterator--------------#
#################################################

# Iterable
# [1] Object contains data that can be iterated.
# [2] Examples (String, List, Set, Tuple, Dictionary)

# Iterator
# [1] Object used to iterate over iterable using "next()" method, it returns 1 element at a time
# [2] You can generate iterator from iterable when using "iter()" method
# [3] loops behind the scene, calls "iter()" method on the iterable
# [4] It calls "StopIteration" if there is no next element
#----------------------------------------------------------------------------------------------------------------#

# myString = "Osama"
# myList = [1, 2, 3, 4, 5]
# myNumber = 10
# myNumber = str(101)

# # for letter in myString:
# #     print(letter, end= " ")

# for number in myNumber:
#     print(number)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#################################################
#------------------Generators-------------------#
#################################################

# [1] A function uses "yield" instead if "return"
# [2] It supports iteration and return the gen. iterator by calling "yield"
# [3] Generator function can have one or more "yield"
# [4] By using "next()" it resumes from where it stopped, not from the beginning
# [5] When the function is called, it does not start automatically, but it gives you the control
#----------------------------------------------------------------------------------------------------------------#

def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

myGen = myGenerator()

print(next(myGen))
print("Printing Next Iteration")
print(next(myGen))
print("Printing Next Iteration")
print(next(myGen))
print("Printing Next Iteration")
print(next(myGen))
print("Printing Next Iteration")
print(next(myGen))
