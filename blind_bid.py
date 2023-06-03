import os

def Highest_Bid(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids = {}

bidding_finished = False

while not bidding_finished : 
    name = input("What is your name ? : ")
    price = int(input("What's your bid ? : $"))
    bids[name] = price
    should_continue = input("Are there any other bidder ? type yes or no : ")
    if should_continue == "no" :
        bidding_finished = True
        Highest_Bid(bids)
    elif should_continue == "yes" : 
        os.system('cls')
