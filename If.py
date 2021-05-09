#######################################
#-----------if, elif, else----------#
#######################################

# uName = "Mahmoud"
# # uCountry = "Egypt"
# # uCountry = "KSA"
# # uCountry = "UAE"
# isStudent = input("Are you Student?")
# uCountry = input("What is your Country?")
# cName = "Python Basics"
# cPrice = 100

# if uCountry == "Egypt" or uCountry == "KSA":
#     print(f"Hello {uName}, The course \"{cName}\" will cost you ${cPrice - 60}")
#     if isStudent == "Yes":
#         print(f"Hello {uName}, because you are student, the course \"{cName}\" will cost you ${cPrice - 90}")

# else:
#     print(f"Hello {uName}, Because you are from {uCountry}, the course \"{cName}\" will cost you ${cPrice - 20}")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

##########################################
#---------Age Calculator Practice--------#
##########################################

# Collect Age data
age = input("Please enter your age:").strip()

# Collect Time Unit
unit = input("Please choose the desired age unit from Months, Weeks, Days: ").strip().lower()

# Get Time Unit
months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == 'months':
    print(f"Your age is {months} Months")

elif unit == 'weeks':
    print(f"Your age is {weeks} Weeks")

elif unit == 'days':
    print(f"Your age is {days} Days")











#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#