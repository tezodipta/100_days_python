#it is a hangman game 
#in this game there is a bug - life a type a already typed currect latter it will only repeat the same nothing will change
#can fix this bug just by using 
# if word_input in blank_list:
#     life -=1

print(r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   ''')

import random
import hangman_words
import hangman_logo


HANGMANPICS = hangman_logo.HANGMANPICS

word_list = hangman_words.word_list
word = random.choice(word_list)


blank_list = []
for latter in word:
    blank_list += '_'

# print(f"the word is {word}")
life = 6

hangman_count = 0

while("_" in blank_list):
    word_input = input("enter your guess latter\n")
    if word_input not in word:
        life -= 1
        print(f"You guess {word_input}, that's not in the word ,You lose a life")
        hangman_count +=1
        print(HANGMANPICS[hangman_count])
        if life == 0:
            print("Game over")
            exit(0)
    else:
        for space in range(0,len(word)):
            if(word_input == word[space]):
                blank_list[space] = word_input
        
        print(blank_list)
        print(HANGMANPICS[hangman_count])

    

        




