number_guessing_logo = """ _____                       _   _                                  _               
|  __ \                     | | | |                                | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
"""

import random

# If easy, user gets 10 tries
# If hard, user gets 5 tries 
easy_level = 10
hard_level = 5

# Defining the difficulty level for the game
def difficulty():
    # Asking user to pick a difficulty level
    level_type = input("Choose a difficulty. Type 'easy' or 'hard': ")
    # Assigning the appropriate amount of turns depending on user's input
    if level_type == 'easy':
        return easy_level
    else: 
        return hard_level

# Function that compares the random_number and the user's guess number
def compare(random_number, guess, turns):
    "Function compares the guess against the answer. Will also return the number of turns left."
    # created users_live so I don't change the global variable within this function
    if guess > random_number:
        print("Too High")
        return turns - 1
    elif guess < random_number:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {guess}")

# Defining function for game
def game():

    # Intro to game
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Asking user to pick a difficulty level
    turns = difficulty()


    # Generating a random number from 1 to 100
    random_number = random.randint(1,101)

    # print(random_number)

    guess = 0

    while guess != random_number:
        print(f"You have {turns} attemps remaining to guess the number.")

        # Getting user's input and comparing it to random number generated
        guess = int(input("Make a guess: "))
        turns = compare(random_number, guess, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != random_number:
            print("Guess again.")

# This function call the function to play the game
game()