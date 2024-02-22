import random
word_list = ['cello','sport','boat']
word = random.choice(word_list)


blank_list = []
for latter in word:
    blank_list += '_'

print(f"the word is {word}")


while("_" in blank_list):
    word_input = input("enter your guess latter\n")
    for space in range(0,len(word)):
        if(word_input == word[space]):
            blank_list[space] = word_input
        
    print(blank_list)
    

        




