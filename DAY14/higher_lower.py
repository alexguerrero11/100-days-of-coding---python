#This game is a replica of the higher lower.
#This game compares instagram followers of two celebrities

import random #random package needed
import higher_lower_art #clip art
from higher_lower_data import data #game data

length = len(data) #determine how much data we got


def get_random_person():
    #function that generates a random int and returns data using it as an index
    random_int = random.randint(1,length)
    return(data[random_int])

def compare_followers(personA, personB):
    #function compares followers and returns letter
    if personA['follower_count'] > personB['follower_count']:
        return "A"
    else:
        return "B"    
    
# Game
def game():
    print(higher_lower_art.logo) #1)print logo
    
    #2)select Person A
    personA = get_random_person()
    message1 = f"Compare A: {personA['name']}, {personA['description']} from {personA['country']}"
    print(message1)
    
    print(higher_lower_art.vs) #3)print VS
    
    #4)select Person B
    personB = get_random_person()
    message2 = f"Compare B: {personB['name']}, {personB['description']} from {personB['country']}"
    print(message2)
    
    #asking for user's input
    user_input = input('Q: Who has more followers? Type "A" or "B": ')
    
    #actual winner
    winner = compare_followers(personA,personB)
    
    #score
    score = 0
    
    #user's response feedback
    if user_input != winner:
        print('Sorry, that is wrong. Final Score: ')
    elif user_input == winner:
        print(f'You are right! Current Score: ')

game()