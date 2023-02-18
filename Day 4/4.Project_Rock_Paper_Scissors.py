rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game = [rock, paper, scissors]
you_chose = int(input("What do you choose? Type 0 for Rock, 1 for Pepper or 2 for Scissors."))
import random

computer_chose = random.randint(0,2)

computer = game[computer_chose]
you = game[you_chose]

print(f"{you} /n Computer chose: {computer}\n ")

if you_chose >= 3 or you_chose < 0: 
  print("You typed an invalid number, you lose!") 
elif you_chose == 0 and computer_chose == 2:
  print("You win!")
elif computer_chose == 0 and you_chose == 2:
  print("You lose")
elif computer_chose > you_chose:
  print("You lose")
elif you_chose > computer_chose:
  print("You win!")
elif computer_chose == you_chose:
  print("It's a draw")

    





