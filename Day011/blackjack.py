#it is a card gane names b;ack jack 
import random
import os
from art import logo
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def add_card():
    """return random card from the deck"""
    return random.choice(cards)


def calculate_score(cards): 
    """take a list of cards and return the score calculated from the cards"""
    if sum(cards) > 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
    """compare the user and computer score and return the result of the game"""

    if user_score == comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif comp_score > 21:
        return "Opponent went over. You win"
    elif user_score > comp_score:
        return "You win"
    else:
        return "You lose"


while True:
    print(logo)
    user_cards = []
    comp_cards = []
    is_game_over = False
    for i in range(2):
        user_cards.append(add_card())
        comp_cards.append(add_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score ==0 or user_score ==0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal == "y":
                user_cards.append(add_card())
            else:
                is_game_over = True


    while comp_score !=0 and comp_score <17:
        comp_cards.append(add_card())
        comp_score = calculate_score(comp_cards)


    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))

    if input("do you want to play a game of blackjack? type 'y' to continue and any other key to exit: ").lower() == "y":
        os.system('cls')
    else:
        exit()
        

