alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
             'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your massage:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text,shift,direction):
    if direction == "decode":
        shift *= -1
    new_text = ""
    for i in text:
        position = alphabet.index(i)
        new_position = position + shift
        new_letter = alphabet[new_position]
        new_text += new_letter
        
    print(f"Your {direction} message is {new_text}")


caesar(text,shift,direction)


