alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
             'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z']

import logo
pic = logo.logo
print(pic)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your massage:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    def caesar(text,shift,direction):
        if direction == "decode":
            shift *= -1
        new_text = ""
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                new_letter = alphabet[new_position]
                new_text += new_letter
            else:
                new_text += char
            
        print(f"Your {direction} message is {new_text}")

    caesar(text,shift,direction)
    repeat = input("Do you want to go again? Type 'yes' or 'no': ").lower()
    if repeat == "no":
        break


