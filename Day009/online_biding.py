#importing
import os
from Day012.art import logo


#clear function to clear console
def clear():
    os.system('cls')


print(logo)

#creating a empty dictionary
bidders = {}

#function to find the highest bidder
def highest_bidder(bidders):
    highest_bid = 0
    for bid in bidders:
        bid_amount = bidders[bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid

    print(f"The winner is {winner} with the bid of {highest_bid}")
    

while True:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))
    bidders[name]=price

    more = input("are there any other bidders? type 'yes or 'no': ").lower()
    if more == "no":
        clear()
        highest_bidder(bidders)
        break
    elif more == "yes":
        clear()
    else:
        print("Invalid input")
        break


