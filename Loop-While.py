##########################################
#----------------Loop-While--------------#
##########################################

# While Condition is True, Code Will Run

# a = 0 
# while a < 10:
#     print(a)
#     a += 1
# else:
#     print("The Loop is Done") #When true Becomes False

#------------------------------------------------------------------------------------------------------------------#

# myF= ["Osama", "Ahmed", "Gamal", "Omar", "Mahmoud", "Tamer", "Mohsen", "Ramy", "Walid", "Amr", ]

# a = 0

# while a < len((myF)):
#     print(f"#{str(a + 1).zfill(2)} {myF[a]}")
#     a += 1
# else:
#     print("The Loop is Done")

#------------------------------------------------------------------------------------------------------------------#

##########################################
#-------------Bookmark Manager-----------#
##########################################

# Empty List
myFavoriteWeb = []
maxWeb = 5

while maxWeb > 0:
    web = input("Enter the Website Name without https:// ")
    myFavoriteWeb.append(f"https://{web.strip().lower()}")

    maxWeb -= 1
    print(f"Website Added, You Have {maxWeb} Left")
    print(f"\n{myFavoriteWeb}")
else:
    print("Bookmarks Are Full")

#------------------------------------------------------------------------------------------------------------------#