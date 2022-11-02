# ASCII art for the hand signals 
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

import random

print("Ready to play Rock, Paper, Scissor")

# User inputs choice 
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0: 
    print("Invalid input!")
else:
    img_list = [rock, paper, scissors]
    string_list = ["Rock", "Paper", "Scissors"]

    user_choice_string =  string_list[user_choice]
    print(f"Player chose {user_choice_string}\n")
    print(img_list[user_choice])


    # Computer choice 
    computer_choice = random.randint(0, 2)
    computer_choice_string =  string_list[computer_choice]
    print(f"Computer chose {computer_choice_string}\n")
    print(img_list[computer_choice])

    # Condition Statements 
    if user_choice == 0 and computer_choice == 2:
        print("Player win!")
    elif computer_choice == 0 and user_choice == 2:
        print("Player lose!")
    elif computer_choice > user_choice:
        print("Player lose!")
    elif user_choice > computer_choice:
        print("Player win!")
    elif computer_choice == user_choice:
        print("It's a draw!")

