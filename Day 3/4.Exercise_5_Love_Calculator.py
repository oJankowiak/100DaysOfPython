# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = (name1 + name2)
names = names.lower()

true_T = names.count("t")
true_R = names.count("r")
true_U = names.count("u")
true_E = names.count("e")
true_total = true_T + true_R + true_U + true_E

love_L = names.count("l")
love_O = names.count("o")
love_V = names.count("v")
love_E = names.count("e")
love_total = love_L + love_O + love_V + love_E

number = str(true_total) + str(love_total)
score = int(number)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")