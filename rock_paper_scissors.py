import random
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

#Create a list of the choices above
hands = [rock, paper, scissors]
#create random choice for computer
computer_choice = random.randint(0,2)

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if user_choice == 0:
    print(rock)
    if computer_choice == 0:
        outcome = "Draw"
    elif computer_choice == 1:
        outcome = "You lose"
    elif computer_choice == 2:
        outcome = "You win"
elif user_choice == 1:
    print(paper)
    if computer_choice == 0:
        outcome = "You win"
    elif computer_choice == 1:
        outcome = "Draw"
    elif computer_choice == 2:
        outcome = "You lose"
elif user_choice == 2:
    print(scissors)
    if computer_choice == 0:
        outcome = "You lose"
    elif computer_choice == 1:
        outcome = "You win"
    elif computer_choice == 2:
        outcome = "Draw"
print("Computer chose:")
print(hands[computer_choice])
print(outcome)