####################################
#--------------Lists---------------#
####################################

# myFriends = ["Osama", "Ahmed", "Sayed"]
# myFriends.append("Alaa")
# myFriends.append(100)
# myFriends.append("test")

# print(myFriends)
# print(myFriends[5])

#---------------------------------------------------------------#

# extend
# a = [1, 2, 3, 4]
# b = ["A", "B", "C"]
# c = ["test"]
# a.extend(b)
# a.extend(c)
# print(a)

#---------------------------------------------------------------#

# remove
# x = [1, 2, 3, 4, 'A', 'B', 'C', 'test', "Mahmoud", "Mahmoud"]
# x.remove("Mahmoud")
# print(x)

#---------------------------------------------------------------#

# # sort
# y = [1, 2, 67, 15, 851, -20, -199]
# y.sort()
# print(y)

#---------------------------------------------------------------#

# clear()
# y = [1, 2, 67, 15, 851, -20, -199]
# print(y)
# y.clear()
# print(y)

#---------------------------------------------------------------#

# copy() "Shallow Copy"
# a = [1, 2, 3, 4]
# b = a.copy()
# b.append(5)
# print(a) # Main List
# print(b) # Copied\Modified List

#---------------------------------------------------------------#

# count()
# a = [1, 2, 3, 4, 1, 2, 5, 1, 6, 1]
# print(a.count(1))

#---------------------------------------------------------------#

# index()
# e = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Mahmoud"]
# print(e.index("Ahmed"))

#---------------------------------------------------------------#

# insert()
# a = [1, 2, 3, 4, "A", "B", "D"]
# print(a)
# a.insert(0, 'Test')
# a.insert(-1, 'Test')
# print(a)

#---------------------------------------------------------------#

# pop()
# a = [1, 2, 3, 4, "A", "B", "D"]
# print(a.pop(0))