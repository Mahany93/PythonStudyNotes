#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#########################################################
#--------------Object Oriented Programming--------------#
#########################################################

# class member:
#     def __init__(self):

#         print("A new member has been added")

# member()

# member_one = member()
# member_two = member()
# member_three = member()

# print(member_one.__class__)

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Instance Attributes and Methods
class member:
    def __init__(self, first_name, middle_name, last_name):

        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name

member_one = member("Mahmoud", "Mahany", "Mahmoud")
# member_two = member("Mahany")
# member_three = member("Omar")

print(member_one.fname, member_one.mname, member_one.lname)
# print(member_one.name)
# print(member_two.name)
# print(member_three.name)