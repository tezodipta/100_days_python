#creating a list having a upper and lower case letters
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#creating a list having a numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#creating a list having a symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
#taking input from the user
inp_letters= int(input("How many letters would you like in your password?\n"))
inp_symbols = int(input(f"How many symbols would you like?\n"))
inp_numbers = int(input(f"How many numbers would you like?\n"))
 #easy level
password = ""
for char in range(0, inp_letters ):
  password += random.choice(letters)
for char in range(0, inp_symbols ):
    password += random.choice(symbols)
for char in range(0, inp_numbers ):
    password += random.choice(numbers)
print(f"Your password is: {password}")

#hard level
password_list = []
for char in range(0, inp_letters ):
  password_list.append(random.choice(letters))
for char in range(0, inp_symbols ):
    password_list += random.choice(symbols)
for char in range(0, inp_numbers ):
    password_list += random.choice(numbers)
random.shuffle(password_list)
password = ""
for char in password_list:
  password += char
print(f"Your password is: {password}")


                            