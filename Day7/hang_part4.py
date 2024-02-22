import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word_list = ['cello','sport','boat']
word = random.choice(word_list)


blank_list = []
for latter in word:
    blank_list += '_'

print(f"the word is {word}")
life = 7

hangman_count = 0

while("_" in blank_list):
    word_input = input("enter your guess latter\n")
    if word_input not in word:
        life -= 1
        print("wrong guess")
        print(HANGMANPICS[hangman_count])
        hangman_count +=1
        if life == 0:
            print("Game over")
            exit(0)
    else:
        for space in range(0,len(word)):
            if(word_input == word[space]):
                blank_list[space] = word_input
        
    print(blank_list)
    

        




