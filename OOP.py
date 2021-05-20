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
    def __init__(self, first_name, middle_name, last_name, gender):

        self.fname = first_name
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender

    def full_name(self):
        return f"{self.fname} {self.mname} {self.lname}"
    
    def name_with_title(self):
        if self.gender == "Male":
            return f"Hello Mr. {self.fname}"
        elif self.gender == "Female":
            return f"Hello Ms. {self.fname}"
        else:
            return f"{self.fname}"

    def get_all_info(self):
        return f"{self.name_with_title()}, your full name is: \"{self.full_name()}\", and your gender is: \"{self.gender}\""

member_one = member("Mahmoud", "Mahany", "Mahmoud", "Male")
# member_two = member("Mahany")
member_three = member("Mona", "Ali", "Mahmoud", "Female")

# print(member_one.fname, member_one.mname, member_one.lname)
# print(member_one.name)
# print(member_two.name)
# print(member_three.name)

# print(member_one.full_name())
# print(member_one.name_with_title())
# print(member_three.name_with_title())
print(member_one.get_all_info())
print(member_three.get_all_info())

#---------------------------------------------------------------------------------------------------------------------------------------------#

