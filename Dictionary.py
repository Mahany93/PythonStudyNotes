#####################################
#------------Dictionary-------------#
#####################################

# Dictionary
# user = {
#     "Name" : "Osama",
#     "Age" : 27,
#     "Country" : "Egypt",
#     "Skills" : ["HTML", "Css", "JS"],
#     "rating" : 10.5
# }

# print(user)
# print(user["Country"])
# print(user.keys())
# print(user.values())

#---------------------------------------------------------------#

# Two-Dimensional Dictionary
# languages = {
#     "One" : {
#         "Name" : "HTML",
#         "Progress" : "80%"
#     }, 
#     "Two" : {
#         "Name" : "CSS",
#         "Progress" : "95%"
#     },
#     "Three" : {
#         "Name" : "JS",
#         "Progress" : "95%"
#     }
# }

#print(languages)
# print(languages["One"])
# print(languages["Three"])
# print(languages["Two"]["Name"])
# print(len(languages["Two"]))

#---------------------------------------------------------------#

# Create Dictionary From Variables
# frameworkOne = {
#     "Name" : "Vujes",
#     "Progress" : "80%" 
# }

# frameworkTwo = {
#     "Name" : "ReactJs",
#     "Progress" : "50%" 
# }

# frameworkThree = {
#     "Name" : "Angular",
#     "Progress" : "60%" 
# }

# allFrameWork = {
#     "One" : frameworkOne,
#     "Two" : frameworkTwo,
#     "Three" : frameworkThree
# }

# print(allFrameWork)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#####################################
#--------Dictionary Methods---------#
#####################################

# clear()
# user = {
#     "Name" : "Osama",
#     "Age" : 27,
#     "Country" : "Egypt",
#     "Skills" : ["HTML", "Css", "JS"],
#     "rating" : 10.5
# }

# print(user)
# user.clear()
# print(user)

#---------------------------------------------------------------#

# update()
# member = {
#     "Name" : "Mahmoud"
# }
# print(member)
# member["Age"] = 36
# print(member)
# member.update({"Country" : "Egypt"})
# print(member)

#---------------------------------------------------------------#

# copy()
# main = {
#     "Name" : "Mahmoud"
# }
# b = main.copy()
# print(b)
# main.update({"Age" : "27"})
# print(main)
# print(b)

#---------------------------------------------------------------#

# keys + value
# main = {
#     "Name" : "Mahmoud",
#     "Age" : "27"
# }
# print(main.keys())
# print(main.values())

#---------------------------------------------------------------#

# setdefault()
# user = {
#     "Name" : "Mahmoud",
# }
# print(user)
# print(user.setdefault("Age", 27))
# print(user)

#---------------------------------------------------------------#

# popitem()
# member = {
#     "Name" : "Mahmoud",
#     "Skill" : "PC Gaming"
# }
# print(member.items())
# print(member)
# # member.update({"Age" : 27})
# # print(member.popitem())

#---------------------------------------------------------------#

# popitem()
view = {
    "Name" : "Mahmoud",
    "Skill" : "PC Gaming"
}

allItems = view.items()
print(view)
view["Age"] = 27
print(allItems)