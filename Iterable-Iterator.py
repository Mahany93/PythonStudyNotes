#################################################
#--------------Date and Time Format-------------#
#################################################

# Iterable
# [1] Object contains data that can be iterated.
# [2] Examples (String, List, Set, Tuple, Dictionary)
#----------------------------------------------------------------------------------------------------------------#
# Iterator
# [1] Object used to iterate over iterable using "next()" method, it returns 1 element at a time
# [2] You can generate iterator from iterable when using "iter()" method
# [3] loops behind the scene, calls "iter()" method on the iterable
# [4] It calls "StopIteration" if there is no next element
#----------------------------------------------------------------------------------------------------------------#

myString = "Osama"
myList = [1, 2, 3, 4, 5]
myNumber = 10
myNumber = str(101)

# for letter in myString:
#     print(letter, end= " ")

for number in myNumber:
    print(number)