####################################
#--------------Tuple---------------#
####################################

# Tuple Syntax & Type
# myTupleOne = ("Mahmoud", "Mahany")
# myTupleTwo = "Osama", "Ahmed"
# myTupleThree = (1, 2, 3, 4, 5)

# print(type(myTupleOne))
# print(type(myTupleTwo))
# print(type(myTupleThree))

# print(myTupleOne)
# print(myTupleTwo)
# print(myTupleTwo[0])
# print(myTupleThree[-1])
# print(myTupleThree[2])

#---------------------------------------------------------------#

# Tuple Assign Values
myTupleFour = (1, 2, 3, 4, 5)

#---------------------------------------------------------------#

# Tuple With One Element 
# TupOne = ("Mahmoud")
# TupTwo = "Osama"
# TupThree = ("Mahmoud",)
# TupFour = "Osama",

# print(TupOne)
# print(TupTwo)
# print(TupThree)
# print(TupFour)

# print(type(TupOne))
# print(type(TupTwo))
# print(type(TupThree))
# print(type(TupFour))

#---------------------------------------------------------------#

# Tuple, List, String Repeat (*)
# myString = "Mahmoud"
# myList = [1, 2]
# myTuple = ("A", "B")

# print(myString * 5)
# print(myList * 5)
# print(myTuple * 5)

#---------------------------------------------------------------#

# Tuple Count()
# a = [1, 2, 3, 4, 1, 2, 5, 1, 6, 1]
# print(a.count(2))

#---------------------------------------------------------------#

# Tuple index()
# a = [1, 2, 3, 4, 1, 2, 5, 1, 6, 1]
# print("The Position of Index is: {:d}".format(a.index(5)))
# print(f"The Position of Index is: {a.index(5)}")

#---------------------------------------------------------------#

# Tuple destruct()
# a = ("A", "B", "C")
# x, y, z = a
# print(x)
# print(y)
# print(z)

b = ("A", "B", 4, "C")
#x, y, z = b # ValueError: too many values to unpack
x, y, _, z = b # Ignores unwanted element (4)
print(x)
print(y)
print(z)