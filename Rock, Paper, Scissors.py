import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
pick = int(input())

cpuchoice = random.randint(0,2)


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


    
if pick == 0:
    print(rock)

elif pick == 1:
    print(paper)

elif pick == 2:
    print(scissors)




print("Computer picked:")


if cpuchoice == 0:
    print(rock)

elif cpuchoice == 1:
    print(paper)

elif cpuchoice == 2:
    print(scissors)



if pick == cpuchoice:
    print("Draw")
    
elif pick == 0 and cpuchoice == 2:
    print("You Won")

elif pick == 2 and cpuchoice == 1:
    print("You Won")

elif pick == 1 and cpuchoice == 0:
    print("You won")

else:
    print("Computer Won")
    














