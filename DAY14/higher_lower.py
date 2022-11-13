#This game is a replica of the higher lower.
#This game compares instagram followers of two celebrities

import random #random package needed
import higher_lower_art #clip art
from higher_lower_data import data #game data

def compare_followers(personA, personB):
    #function compares followers and returns letter
    if personA['follower_count'] > personB['follower_count']:
        return "A"
    else:
        return "B"

def game():
    
    print(higher_lower_art.logo) #1)print logo
    
    #initialize variables
    personA = random.choice(data)
    personB = random.choice(data)
    
    #pre-req
    game_continues = True
    score = 0  #initialize score
    
    #game starts
    while game_continues == True:        
        personA = personB
        personB = random.choice(data)
        
        # Main Message Displayed
        message1 = f"Compare A: {personA['name']}, {personA['description']} from {personA['country']}"
        print(message1)
        print(higher_lower_art.vs)
        message2 = f"Compare B: {personB['name']}, {personB['description']} from {personB['country']}"
        print(message2)
        
        # DEBUGGING - ANSWER
        print(compare_followers(personA,personB))
        
        # User's Input
        user_input = input('Q: Who has more followers? Type "A" or "B": ')
        # Actaul winner
        winner = compare_followers(personA,personB)
                
        # Checking if game can continue
        if user_input == winner:
            score = score + 1
            print(f'You are right! Current Score: {score}')
        else:
            game_continues = False
            print(f'Sorry, that is wrong. Final Score: {score}')

game()