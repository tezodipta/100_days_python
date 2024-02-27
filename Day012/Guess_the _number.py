#its a simple game where we are going to guess number between 1 to 100
import random
from art import logo

while True:
    print(logo)
    print("welcome to the number guessing game :")
    NUMBER = random.randint(1,100)

    def level(inp):
        """this function will take difficulty and return player life based on difficulty"""
        if inp == "easy":
            return 10
        elif inp == "hard":
            return 5
        else:
            print("Invalid input")
            return 0
        
    def guess(inp_number):
        """this function will check the guessed numberd is currect or not and return the result."""
        if inp_number == NUMBER:
            print("You win the game")
            return False
        elif inp_number > NUMBER:
            print("Too high")
            return True
        else:
            print("Too low")
            return True
        
    life = level(input("choose your diffucalty level,'easy; or 'hard': ").lower())

    for attempt in range(life):
        print(f"you have {life} attempt left to guess the numeber")
        guess_number = int(input("Make a guess: "))
        life -= 1
        if not guess(guess_number):
            break

    if life == 0:
        print(f"you have no attempt left, the correct number is {NUMBER}")

    if input("Type 'yes' to play again or any other key to exit: ").lower() != "yes":
        exit()
