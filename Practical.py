#######################################
#---------------User Input------------#
#######################################

# fname = input("What is Your First Name?")
# lname = input("What\'s Your Last Name?")

# fname = fname.strip().capitalize()
# lname = lname.strip().capitalize()

# print(f"Hello {fname} {lname}. We are Happy to See You")
# print(f"Hello {fname:.1s} {lname}. We are Happy to See You")


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#######################################
#----------------Slicing--------------#
#######################################

# fname = input("What\'s Your First Name?").strip().capitalize()
# lname = input("What\'s Your Last Name?").strip().capitalize()

# email = (fname + "." + lname + "@fti.de").lower()
# print(f"Hi {fname} Your Email Address is \"{email}\"")

#---------------------------------------------------------------#

# email = "mahmoud.mahany@fti.de"
# # email = input("Please Enter the Email Address:")
# name = email.replace('.', ' ')[0:email.index("@")].title()
# # domain = email.replace('.', ' ')[email.index("@"):] # includes "@"
# domain = email[email.index("@") + 1:] # starts after @
# print(f"The User Display Name is \"{name}\" \nThe Domain is \"{domain}\"")

#---------------------------------------------------------------#

age = int(input('What\'s Your Age? ').strip())

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"You have been living for \"{months:,}\" Months, \"{weeks:,}\" Weeks, \"{days:,}\" Days, \"{hours:,}\" Hours, \"{minutes:,}\" Minutes and \"{seconds:,}\" Seconds")
