#################################
#---------Concatination---------#
#################################

# msg = "I Love"
# lang = "Python"
# print(msg + " " +lang)
# print(msg + "\n" +lang)

##################################
#------Indexing and Slicing------#
##################################

# y= "I Love Python"
# print(y[0:2])  #Select Range
# print(y[0:]) # If end s not there, it will go to the end of the string
# print(y[:5]) # If start is notthere, it will begin from the start of the string
# print(y[::2]) # start from the beginnig, but print in steps of 2

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


#################################
#------------Strings------------#
#################################

###########################
##  \'	Single Quote     ##
##  \\	Backslash        ##
##  \n	New Line         ##
##  \r	Carriage Return  ##
##  \t	Tab              ##
##  \b	Backspace        ##
##  \f	Form Feed        ##
##  \ooo	Octal value	 ##
##  \xhh	Hex value    ##
###########################

# print("Hello\b World") # Will remove o
# print("Hello World \nSecond Line") # new line
# print('I love \'Single Quote\'') # Escape Quotes
# print("I love \"Double Quote\"") # Escape Quotes
# print("testtest\rAbcde") # Carriage Return
# print("Hello\tWorld") # Tab
# print("\x4d\x61\x68\x6d\x6f\x75\x64\x20\x4d\x61\x68\x61\x6e\x79") # Hex Value

#---------------------------------------------------------------#

# mystring1 = 'This is Single Quotes "Test"'
# mystring2 = "This is Double Quotes'Test'"
# mystring3 = '''First
# Second \
# Third'''
# mystring4 = """First
# Second 'Test' \\ "Test"
# Third"""
# print(mystring1)
# print(mystring2)
# print(mystring3)
# print(mystring4)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


#################################
#---------String Methods--------#
#################################

# # Length
# a= "I Love Python"
# b= "I    Love    Python"
# print(len(a))
# print(len(b))

#---------------------------------------------------------------#


# strip() rstrip() lstrip()
# a= "    I Love Python    "
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())

# a= "@#@#I Love Python@#@#"
# print(a.strip("@#"))
# print(a.rstrip("@#"))
# print(a.lstrip("@#"))

#---------------------------------------------------------------#

# title() & capitalize()
# b= "I Love 2d Graphics and 3g technology and Python"
# print(b.title())

# c= "I Love 2d Graphics and 3g technology and Python"
# print(b.capitalize())

#---------------------------------------------------------------#

# zfill()
# c, d, e = "1", "11", "111"

# print(c.zfill(3))
# print(d.zfill(3))
# print(e.zfill(3))

#---------------------------------------------------------------#

# zfill()
# n = "mahMoUd"
# print(n.lower())
# print(n.upper())

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


#################################
#---------String Methods--------#
#################################

# split() rsplit(a)
# a= "I Love Python and PHP"
# print(a.split())

# b= "I-Love-Python-and-PHP-and-MySQL"
# print(b.split("-"))
# print(b.split("-", 2))
# print(b.rsplit("-", 3))

#---------------------------------------------------------------#

# center()
# n= "Mahmoud"
# print(n.center(11)) #space
# print(n.center(11, "#")) #hash
# print(n.center(11, "@")) #@ 

#---------------------------------------------------------------#

# count
# f= "I Love Python and PHP, Because PHP is Easy"
# print(f.count("PHP"))
# print(f.count("PHP", 0, 25)) #Position/Index

#---------------------------------------------------------------#

# swapcase()
# g= "I Love Python"
# h= "i lOVE pYTHON"
# print(g.swapcase())
# print(h.swapcase())

#---------------------------------------------------------------#

# startswith() endswith()
# i= "I Love Python"
# print(i.startswith("I"))
# print(i.startswith("S"))
# print(i.startswith("P", 7, 12))
# print(i.endswith("e", 2, 6))

#---------------------------------------------------------------#

# index(SubString, Start, End)
# a = "I Love Python"
# print(a.index("P")) # Index Number 7
# print(a.index("P", 0, 10)) # Index Number 7 in Range 0,10
# print(a.index("P", 0, 5)) # Value Error

#---------------------------------------------------------------#

# find(SubString, Start, End)
# b = "I Love Python"
# print(a.find("P")) # Index Number 7
# print(a.find("P", 0, 10)) # Index Number 7 in Range 0,10
# print(a.find("P", 0, 5)) # -1 Instead of Value Error

#---------------------------------------------------------------#

# rjust(Width, Fill Char) ljust()
# c = "Mahmoud"
# print(c.rjust(10, "$"))
# print(c.ljust(10, "$"))

#---------------------------------------------------------------#

# splitlines()
# e = """First Line
# Second Line
# Third Line"""
# print(type(c))
# print(c.splitlines())

# f = "First Line\nsecond Line\nThird Line"
# print(type(f))
# print(f.splitlines())

#---------------------------------------------------------------#

# expandtabs()
# g = "Hello\tWorld\tI\tLove\tPython"
# print(g)
# print(g.expandtabs(5))

#---------------------------------------------------------------#

# is
# one = "I Love Python And Coding"
# two = " "
# print(one.istitle())
# print(two.isspace())

# three = "AaaaaaaBBbbbb"
# four = "AaaaaaaBBbb123"
# print(three.isalpha())
# print(four.isalpha())
# print(four.isalnum())

#---------------------------------------------------------------#

# replace(Old Value, New Value, Count)
# a = "Hello One Two Three One One"
# print(a.replace("One", "1"))

#---------------------------------------------------------------#

# join(Iterable)
# myList= ["Mahmoud", "Mahany", "Mahmoud"]
# print(myList)
# print(type(myList))
# print("-".join(myList))
# print(type("-".join(myList)))

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#


################################
#--------Strings Formatting-----
################################

# %s => String
# %d => Number
# %f => Float

# name= "Mahmoud"
# age = 27
# rank = 10

# print("My Name is: " + name)
# #print("My Name is: " + name + " and My Age is: " + age) # Type Error
# print("My Name is: %s" % "Test")
# print("My Name is: %s and My Age is: %d and My Rank is: %.2f" % (name, age, rank))

#---------------------------------------------------------------#

# print("My Name is: {}".format(name))
# print("My Name is: {} and My Age is: {} and My Rank is: {}".format(name, age, rank))
# print("My Name is: {:s} and My Age is: {:d} and My Rank is: {:.1f}".format(name, age, rank))

#---------------------------------------------------------------#

# Truncate String
# myLongString= "Hello Peoples of Elzero Web School I Love You all"
# print(myLongString)
# print("Message is: %.5s" % myLongString)

#---------------------------------------------------------------#

# Format Money
# myMoney = 500168621437
# print("My Money Amount Is: {:_d}".format(myMoney))
# print("My Money Amount Is: {:,d}".format(myMoney))

#---------------------------------------------------------------#

# Rearrange Items
 
# a, b, c = "One", "Two", "Three"
# print("Hello {} {} {}".format(a, b, c))
# print("Hello {2} {1} {0}".format(a, b, c)) # Hello Three Two One
# print("Hello {2} {0} {1}".format(a, b, c)) # Hello Three One Two

# x, y, z = 10, 20, 30
# print("Hello {} {} {}".format(x,y,z))
# print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x,y,z))

#---------------------------------------------------------------#

# Format in Version 3.6+

# myName = "Mahmoud"
# myAge = 36
# print("My Name is: {myName} and My Age is: {myAge}")
# print(f"My Name is: {myName} and My Age is: {myAge}")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#