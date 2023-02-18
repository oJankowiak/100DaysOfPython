# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# print(names)
number_of_people = len(names)

# print(number_of_people)

import random

person_who_pay = random.randint(0, number_of_people - 1)
name_of_person = (names[person_who_pay])

print(f"{name_of_person} is going to buy the meal today!")
