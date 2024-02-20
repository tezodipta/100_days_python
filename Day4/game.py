#it is a stone paper scissor game 
import random
print("it is a stone paper game where ")
comp_inp = ['stone','paper','scissor']
comp_result = random.choice(comp_inp)
my_inp = input("enter your choice (stone,paper,scissor): ").lower()


stone = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
# print("comp= \n")
# if(comp_result == 'stone'):
#     print(stone_img)
# elif(comp_result == 'paper'):
#     print(paper_img)
# else:
#     print(scissor_img)


# print("User \n")
# if(my_inp == 'stone'):
#     print(stone_img)
# elif(my_inp == 'paper'):
#     print(paper_img)
# else:
#     print(scissor_img)






def logic(comp,user):
    if (comp == user):
        print("draw")
    elif ((comp == 'stone' and user == 'paper') or (comp == 'scissor' and user == 'paper')):
        print("computer own the game")
    else:
        print("you win")

logic(comp_result,my_inp)
