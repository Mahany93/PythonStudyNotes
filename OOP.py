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
# class member:

#     not_allowed_names = ["Shit", "Hell"]
#     user_num = 0

#     def __init__(self, first_name, middle_name, last_name, gender):

#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender
#         member.user_num += 1 

#     def full_name(self):
#         if self.name in member.not_allowed_names:
#             raise ValueError("Name Not Allowed")
#         else:   
#             return f"{self.fname} {self.mname} {self.lname}"
    
#     def name_with_title(self):
#         if self.gender == "Male":
#             return f"Hello Mr. {self.fname}"
#         elif self.gender == "Female":
#             return f"Hello Ms. {self.fname}"
#         else:
#             return f"{self.fname}"

#     def get_all_info(self):
#         return f"{self.name_with_title()}, your full name is: \"{self.full_name()}\", and your gender is: \"{self.gender}\""
    
#     def delete_user(self):
#         member.user_num -= 1 
#         return f"User {self.fname} is Deleted"

# member_one = member("Mahmoud", "Mahany", "Mahmoud", "Male")
# # member_two = member("Mahany")
# member_three = member("Mona", "Ali", "Mahmoud", "Female")
# print(member.user_num)
# print(member_one.delete_user())
# print(member.user_num)

# # print(member_one.fname, member_one.mname, member_one.lname)
# # print(member_one.name)
# # print(member_two.name)
# # print(member_three.name)

# # print(member_one.full_name())
# # print(member_one.name_with_title())
# # print(member_three.name_with_title())
# # print(member_one.get_all_info())
# # print(member_three.get_all_info())

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Class & Static Methods

# class member:
    
#     not_allowed_names = ["Shit", "Hell"]
#     user_num = 0

#     @classmethod
#     def show_users_count(cls):
#         print(f"We have {cls.user_num} Users in Our System")

#     @staticmethod
#     def say_hello():
#         print("Hello From Static Method")

#     def __init__(self, first_name, middle_name, last_name, gender):

#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender
#         member.user_num += 1 

#     def full_name(self):
#         if self.name in member.not_allowed_names:
#             raise ValueError("Name Not Allowed")
#         else:   
#             return f"{self.fname} {self.mname} {self.lname}"
    
#     def name_with_title(self):
#         if self.gender == "Male":
#             return f"Hello Mr. {self.fname}"
#         elif self.gender == "Female":
#             return f"Hello Ms. {self.fname}"
#         else:
#             return f"{self.fname}"

#     def get_all_info(self):
#         return f"{self.name_with_title()}, your full name is: \"{self.full_name()}\", and your gender is: \"{self.gender}\""
    
#     def delete_user(self):
#         member.user_num -= 1 
#         return f"User {self.fname} is Deleted"


# member_one = member("Mahmoud", "Mahany", "Mahmoud", "Male")
# member_three = member("Mona", "Ali", "Mahmoud", "Female")

# print(member.user_num)
# member.show_users_count()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# Magic Method

class skill:
    def __init__(self):
        self.skills = ["HTML", "CSS", "JS"]

profile = skill()
print(profile)
print(profile.__class__)