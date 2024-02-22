import random
word_list = ['cello','sport','boat']
word = random.choice(word_list)
word_input = input("enter your guess latter\n")


blank_list = []
for latter in word:
    blank_list += '_'

    
for space in range(0,len(word)):
    if(word_input == word[space]):
        blank_list[space] = word_input
        
print(f"the word is {word}")
print(blank_list)