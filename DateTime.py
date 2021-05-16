#################################################
#-----------------Date and Time-----------------#
#################################################

# import datetime

# # print(dir(datetime))

# # Current Date&Time
# print(f"\n{'#' * 40}")
# print(f"Full Date is: {datetime.datetime.now()}")
# print("#" * 40)

# # Current Year
# print(f"Year is: {datetime.datetime.now().year}")
# print("#" * 40)

# # Current Month
# print(f"Month is: {datetime.datetime.now().month}")
# print("#" * 40)

# # Current Day
# print(f"Day is: {datetime.datetime.now().day}")
# print("#" * 40)

# # Start and End date
# print(f"Start Date is: {datetime.datetime.min}")
# print(f"End Date is: {datetime.datetime.max}")
# print("#" * 40)

# # Start and End Time
# print(f"Start Time is: {datetime.time.min}")
# print(f"End Time is: {datetime.time.max}")
# print("#" * 40)

# # Current Time
# print(f"Current \"Time\" is: {datetime.datetime.now().time()}")
# print(f"Current \"Hour\" is: {datetime.datetime.now().time().hour}")
# print(f"Current \"Minute\" is: {datetime.datetime.now().time().minute}")
# print(f"Current \"Second\" is: {datetime.datetime.now().time().second}")
# print(f"Current \"Micro Second\" is: {datetime.datetime.now().time().microsecond}")
# print("#" * 40)

# # Specific Date
# birthDay = datetime.datetime(1993, 7, 3, 15, 30)
# dateNow = datetime.datetime.now()

# print(f"Birthday is: {datetime.datetime(1993, 7, 3, 15, 30)}")
# print(f"Time Since Birthday is: {dateNow - birthDay}")
# print("#" * 40)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#################################################
#--------------Date and Time Format-------------#
#-------------(https://strftime.org/)-----------#
#################################################

import datetime
myBirthday = datetime.datetime(1993,7,3)
print(myBirthday)

# Python "strftime" Directives (https://strftime.org/)
print(myBirthday.strftime("%A, %B, %m, %Y"))

#---------------------------------------------------------------------------------------------------------------------------------------------#










