#######################################
#---------------Function--------------#
#######################################

# def                       => Function Keyword [Define]
# say_hello                 => Function Name
# name                      => Parameter

# a, b, c, = "Osama", "Ahmed", "Sayed"

# def say_hello(name):

#     print(f"Hello {name}")

# say_hello("Omar")
# say_hello(a)
# say_hello(b)
# say_hello(c)

#-------------------------------------------------------------------------------------#

# def addition(n1, n2):
#     if type(n1) != int or type(n2) != int:
#         print("Only Integers are allowed")
#     else:
#         print(n1 + n2)

# addition(10, "Omar")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#################################################
#-----------Function Default Parameters---------#
#################################################

# def say_hello(name="Unknown", age="Unknown"):
#     print(f"Hello {name} your age is {age}")

# say_hello("Mahmoud", 25)
# say_hello("Omar")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

###########################################################
#--Function Packing, Unpacking Arguments *Args, **KWArgs--#
###########################################################

# def say_hello(*people):
#  print(type(people))
#     for name in people:
#         print(f"Hello {name}")

# say_hello("Amr", "Ahmed", "Omar")

#-------------------------------------------------------------------------------------#

# def show_skills(**skills):
#     print(type(skills))
    
#     for skill, value in skills.items():
#         print(f"{skill} => {value}")

# show_skills(HTML= "70%", JS= "65%", CSS= "82%")

#-------------------------------------------------------------------------------------#

# mySkills = {
#     "HTML" : "60%",
#     "JS" : "70%"
# }

# def show_skills(**skills):
#     for skill, value in skills.items():
#         print(f"{skill} => {value}")

# show_skills(**mySkills)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

####################################################
#--Function Packing, Unpacking Arguments Training--#
####################################################

# def show_skills(name, *skills, **skillsWithProgress):
#     print(f"Hello {name} \nSkills without Progress are: ")

#     for skill in skills:
#         print(f"- {skill}")

#     print(f"Skills With Progress are: ")
#     for skill_key, skill_value in skillsWithProgress.items():
#         print(f"- {skill_key} => {skill_value}")

# show_skills("Mahmoud", "HTML", "CSS", "JS", Python= "80%")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#################################################
#-----------------Function Scope----------------#
#################################################

x = 0 # Global Scope

def one():
    global x
    print(f"Print Variable Explicitly From Global Scope within the Function {x}")
    
    x = 1 # Function Scope
    print(f"Print Variable From Function One Scope {x}")

def two():
    x = 2 # Function Scope
    print(f"Print Variable From Function Two Scope {x}")

def three():
    #x = 2 # Function Scope
    print(f"Function Three has no defined \"x\" variable, it will use the GLobal Scope value {x}")


print(f"Print Variable From Global Scope {x}")
one()
two()
three()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#################################################
#-----------------Function Scope----------------#
#################################################


