from game_data import data
from art import logo, vs
import random
import os

def clear():
    """Clear the console."""
    os.system('cls')

print(logo)

def vs_display(choice1,choice2):
    """Display the choices to the user."""
    print(f"Compare A: {choice1['name']}, a {choice1['description']}, from {choice1['country']}")
    print(vs)
    print(f"Against B: {choice2['name']}, a {choice2['description']}, from {choice2['country']}")

def check_follower(choice1,choice2,user_inp):
    """Check the follower count and return the result."""
    if choice1['follower_count'] == choice2['follower_count']:
        print(f"Both have same number of followers,game over ,total score is {score}")
    
    elif choice1['follower_count'] > choice2['follower_count']:
        if user_inp == 'a':
            return True
        else:
            return False

    else:
        if user_inp == 'b':
            return True
        else:
            return False

score = 0

random_choice_1 = random.choice(data)

while True:
    random_choice_2 = random.choice(data)
    vs_display(random_choice_1,random_choice_2)
    user_inp = input("who have higher follwers? 'A' or 'B': ").lower()
    result = check_follower(random_choice_1,random_choice_2,user_inp)
    
    if result:

        if user_inp == 'a' and result == True:
            random_choice_1 = random_choice_1
        else:
            random_choice_1 = random_choice_2
    
        score += 1
        clear()
        print(f"You are right and your current score is {score}")

    else:
        clear()
        print(f"wrong answer!, your total score is {score}")
        exit()