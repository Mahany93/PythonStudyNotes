#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#################################################
#-----------------File Handling-----------------#
#################################################
# "a" Append    -   Open file for appending values, creates the file if it does not exist.
# "r" Read    -   [Default Value]Open file for read, gives error if file does not exist.
# "w" Write    -   Open file for writing, create file if it does not exist.
# "x" Create    -   Create file, give error if it does not exist.
#---------------------------------------------------------------------------------------------------------------------------------------------#

# import os

# # Main current working directory
# print(os.getcwd)    

# print("#"*100)

# # Absolute path for current file
# print(os.path.abspath(__file__))   

# print("#"*100)

# # Directory for the opened file
# print(os.path.dirname(os.path.abspath(__file__))) 

# print("#"*100)

# # Change current working directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print("#"*100)

#---------------------------------------------------------------------------------------------------------------------------------------------#

# # The r in open(r), indicates that the following line is raw string. Nothing will be treated as a method or switch.
# myFile = open(r"D:\Courses\Coding\Python\ElZeroWebSchool\files\mahmoud.txt", "r")

# print(myFile) # File Data Object
# print(myFile.name)
# print(myFile.mode)

# print(myFile.read())
# print(myFile.read(5)) # Read 5 words
# print(myFile.readline()) # Read line number 5
# print(myFile.readlines(50))
# print(type(myFile.readlines()))

# for line in myFile:
#     print(line)
#     if line.startswith("05"):
#         break

# myFile.close()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# myFile = open(r"D:\Courses\Coding\Python\ElZeroWebSchool\files\test2.txt", "w")
# myFile.write("Test Line\n" * 1000)

# myList = ["Line1\n", "Line2\n", "Line3"]
# myFile = open(r"D:\Courses\Coding\Python\ElZeroWebSchool\files\test2.txt", "w")
# myFile.writelines(myList)
# myFile.close()

#---------------------------------------------------------------------------------------------------------------------------------------------#

# myFile = open(r"D:\Courses\Coding\Python\ElZeroWebSchool\files\test2.txt", "a")
# myFile.write("\nLast Line\n")
# myFile.close()