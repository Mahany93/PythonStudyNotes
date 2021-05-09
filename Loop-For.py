##########################################
#----------------Loop-For--------------#
##########################################

# myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

# for number in myNumbers:
#     #print(number * 10)
#     if number % 2 == 0:
#         print(f"The number \"{number}\" Is Even")
#     else:
#         print(f"The number \"{number}\" Is Odd")
# else:
#     print("The loop Is Done.")

#------------------------------------------------------------------------------------------------------------------#

# myName = "Mahmoud"
# for letter in myName:
#    print(letter.lower())

#------------------------------------------------------------------------------------------------------------------#

# # Range
# myRange = range(1, 51)

# for number in myRange:
#     print(number)


# # Dictionary
# mySkills = {
#     "HTML": "90%",
#     "CSS": "60%",
#     "PHP": "70%",
#     "JS": "80%",
#     "Python": "85%"
# }
# # print(mySkills['HTML'])

# for skill in mySkills:
#     print(f"My Progress in {skill} is: {mySkills[skill]}")

#------------------------------------------------------------------------------------------------------------------#

# people = ["Mahmoud", "Ahmed", "Amin", "Ali"]
# skills = ["HTML", "CSS", "JS"]

# for name in people:     # Outer Loop
#     print(f"{name} Skills are: ")
#     for skill in skills:    # Inner Loop
#         print(f"- {skill}")

people = {
    "Mahmoud":{
        "HTML": "90%",
        "CSS": "60%",
        "PHP": "70%",
        "JS": "80%",
        "Python": "85%"
    },

    "Ahmed":{
        "HTML": "60%",
        "CSS": "57%",
        "PHP": "95%",
        "JS": "78%",
        "Python": "56%"
    },

    "Amin":{
        "HTML": "43%",
        "CSS": "20%",
        "PHP": "85%",
        "JS": "73%",
        "Python": "85%"   
    },

    "Ali":{        
        "HTML": "60%",
        "CSS": "82%",
        "PHP": "55%",
        "JS": "91%",
        "Python": "63%"
    } 
}

# print(people["Mahmoud"])
# print(people["Mahmoud"]["CSS"])

for name in people:
    print(f"The skills and progress for {name} are: ")
    for skill in people[name]:
        print(f"{skill} => {people[name][skill]}")