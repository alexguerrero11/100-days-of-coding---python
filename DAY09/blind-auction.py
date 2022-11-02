# Problem - 
""" Create a blind auction
requirement: insert name and bid for each bidder, after everyone placed their bids output the highest bidder with its bid. """
#

blind_auction_logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(blind_auction_logo)


# from replit import clear
# HINT: You can call clear() to clear the output in the console.

# defining variable to help loop thru code
continueBid = True

bid_dictionary = {}

# function which identifies highest bigger
def find_highest_bidder(bidding_record):
    highest_bid = 0 #initial value
    winner = ""
    #looping thru each player to compare their bid
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while continueBid:
    input_name = input("Insert your name?: ")
    input_bid = int(input("What is your bid?: $"))

    bid_dictionary[input_name] = input_bid

    # print(bid_dictionary)
    continue_bid = input("Is there any other users who want to bid? yes or no\n")

    if continue_bid == "no":
        continueBid = False

# calling function to identiy highest bidder
find_highest_bidder(bid_dictionary)
