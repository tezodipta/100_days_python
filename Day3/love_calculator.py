#its a program to calculate love % 
print("LOVE CALCULATOR")
user1 = input("Enter your name\n")
user2 = input("Enter their name\n")
combined_name = (user1+user2).lower()

T = combined_name.count("t")
R= combined_name.count("r")
U= combined_name.count("u")
E= combined_name.count("e")

true=T+R+U+E

L= combined_name.count("l")
O= combined_name.count("o")
V= combined_name.count("v")
E= combined_name.count("e")

love = L+O+V+E

# print(f"T occure {T} times\n")
# print(f"R occure {R} times\n")
# print(f"U occure {U} times\n")
# print(f"E occure {E} times\n")
# print(f"total = {true}\n\n")


# print(f"L occure {L} times\n")
# print(f"O occure {O} times\n")
# print(f"V occure {V} times\n")
# print(f"E occure {E} times\n")
# print(f"total = {love}\n\n")

love_score = int(str(true)+str(love))
print("your love score is: ",love_score)
 
if (love_score < 10 or love_score >90):
    print("you go like coke and mentos")
elif (love_score >= 40 or love_score <=50):
    print("you are alright together")











