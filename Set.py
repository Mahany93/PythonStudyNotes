####################################
#---------------Set----------------#
####################################

# mySetOne = {"Osama", "Ahmed", 100}
# print(mySetOne)

#mySetThree = {"Osama", 100, 105.6, True, [1, 2, 3]} # unhashable type: 'list'
#mySetThree = {"Osama", 100, 105.6, True, (1, 2, 3)}
# mySetFour = {"Osama", "Ahmed", 100, "Osama", 1, 2, 3, 5, 1, (6, 1, 7)}
# print(mySetFour)

#---------------------------------------------------------------#

# Set clear()
# a = {1, 2, 3, 4, 5}
# a.clear()
# print(a)

#---------------------------------------------------------------#

# Set union()
# b = {6, 7, 8, 9, 10}
# c = {11, 12, 13, 14}
# x = {"Zero", "Cool"}
# print(b | c)
# print(b.union(c, x))

#---------------------------------------------------------------#

# Set copy() remove() discard()
# e = {1, 2, 3, 4, 5}
# f = e.copy()
# print(e)
# print(f)

# e.add(6)
# print(e)
# print(f)

# e.remove(6)
# print(e)
# print(f)

# e.remove(6) # no error if element not found
# print(e)
# print(f)

#---------------------------------------------------------------#

# pop()
# i = {"A", True, 1, 2, 3, 4, 5}
# print(i.pop())

#---------------------------------------------------------------#

# update()
# j = {1, 2, 3, 4}
# k = {2, 3, 4, 5, 6}
# j.update(k) # merge both, but remove dublicates
# j.update(['Html', 'Css'])
# print(j)

#---------------------------------------------------------------#

# difference() difference.update()
# a = {1, 2, 3, 4}
# b = {2, 3, "Mahmoud", "Mahany","Test"}
# print(a.difference(b))
# print(a)
# print("=" * 20)
# print(a.difference_update(b)) # get difference and update it in a
# print(a)

#---------------------------------------------------------------#

# intersection() intersection_update ()
# e = {1, 2, 3, 4, "X"}
# f = {"Osama", "X", 2}
# print(e)
# print(e.intersection(f))
# print(e.intersection_update(f))
# print(e)

#---------------------------------------------------------------#

# symmetric_difference() intersection_update ()
# i = {1, 2, 3, 4, "X"}
# j = {"Osama", "Mahmoud", "X", 2, 4}
# print(i)
# print(i.symmetric_difference(j))
# print(i.symmetric_difference_update(j))
# print(i)

#---------------------------------------------------------------#

# issuperset() "The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False."
# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# c = {1, 2, 3, 4, 5}

# print(a.issuperset(b)) # True if all elements of the set b exists in a
# print(a.issuperset(c))# True if all element of the set c exists in a

#---------------------------------------------------------------#

# issubset() "The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False."
# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# f = {1, 2, 3, 4, 5}

# print(a.issubset(b)) # True if all elements of the set b exists in a
# print(a.issubset(f))

#---------------------------------------------------------------#

# isdisjoint()
# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# i = {10, 11, 12}

# print(a.isdisjoint(b))
# print(a.isdisjoint(i))