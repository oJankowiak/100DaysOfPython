print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

corridor = input("In front of you are two corridors, one leading to the left and the other to the right, witch one you choose? \n")
corridor = corridor.lower()

if corridor == "right":
    noise = input("As you walked along the narrow passage, you heard strange noises behind your back, which are getting louder and louder, do you want to stay or go futher.\n")
    noise = noise.lower()
    if noise == "stay":
        print("Suddenly, the you saw a figure moving towards you. It was a monster, with sharp claws and glowing eyes.\nYour body froze, unsure of what to do. The monster lunged forward, and you realized that you had made a terrible mistake.\nGame Over")
    else:
        dor = input("As you walked along the narrow passage you encountered 4 pairs of mysterious doors, each of the doors has a different color: Red, Blue, Yellow and Green. Which door do you want to open? \n")
        dor = dor.lower()
        if dor == "red":
            print("The only thing you managed to notice was a blast of heat and a big fire\nGame Over!")
        elif dor == "blue":
            print("The only thing you managed to notice was the big eyes, then you felt a sharp pain in your neck\nGame Over!")
        elif dor == "yellow":
            print("You found yourself in a room filled with treasure - gold, silver, jewels, and other valuable items - and you knew that you had found what you had been seeking.\n Congratulations, you've won!")
        else:
            print ("Suddenly you opened your eyes and discovered that the whole story was just a dream")
else:
            print("You sprained your ankle tripping over a stone and your pants burst, revealing old underwear that were the only clean ones. \nEmbarrassed and sore, you returned to your home, vowing never to return here\nGame Over!")
