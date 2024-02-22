import random
word_list = ['cello','sport','boat']
word = random.choice(word_list)
word_input = input("enter your guess latter\n")

for latter in word:
    if(latter == word_input):
        print("right")
    else:
        print("wrong")
print(f"the word is {word}")