#import packages
import random
import hangman_art
import hangman_words

# Generate a random word - list of words
list_of_words = hangman_words.word_list

#import from name and logo from separate file
print(hangman_art.name)
print(hangman_art.logo)

#get random word from our list of words
random_word = random.choice(list_of_words)

### REVEAL WORD ###
#print(f"The selected random word is: {random_word}")
### REVEAL WORD ###

# Generate as many blanks as letters in word 
game_display = []

for _ in range(len(random_word)):
    game_display += "_"
print(game_display)


end_of_game = False
users_life = 6

while not end_of_game:
    # User input 
    letter_choice = input("Guess a letter: ").lower()
    print(f"Guess a letter: {letter_choice}")

    # 
    if letter_choice in game_display:
        print("You have guessed this letter already. Try again.")


    # Letter is checked agaisnt word
    for position in range(len(random_word)):
        letter = random_word[position]
        if letter == letter_choice:
            game_display[position] = letter

    print(game_display)


    #from hangman_art import stages
    if letter_choice not in random_word:
        users_life -= 1
        print(hangman_art.stages[users_life])
        print(f"You have {users_life} lives.")
        if users_life == 0:
            end_of_game = True
            print("You lose the game! =( ")

    if "_" not in game_display:
        end_of_game = True
        print("You win the game! =)")
