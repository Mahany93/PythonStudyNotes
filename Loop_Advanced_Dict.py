##########################################
#--------------Advanced-Loop-------------#
##########################################

# # Dictionary
mySkills = {
    "HTML": "90%",
    "CSS": "60%",
    "PHP": "70%",
    "JS": "80%",
    "Python": "85%"
}
# print(mySkills.items())

# # First Method
# for skill in mySkills:
#     print(f"{skill} => {mySkills[skill]}")

# Second Method
# for skill_name, skill_progress in mySkills.items():
#     print(f"{skill_name} => {skill_progress}")
#------------------------------------------------------------------------------------------------------------------#

myUltimateSkills = {
    "HTML": {
        "Main": "80%",
        "Pugjs": "60%"
    },
    "CSS": {
        "Main": "90%",
        "Sass": "70%"
    }
}

for main_key, main_value in myUltimateSkills.items():
    print(f" \n {main_key} Progress is: ")
    for sub_key, sub_value in main_value.items():
        print(f"- {sub_key} => {sub_value}")