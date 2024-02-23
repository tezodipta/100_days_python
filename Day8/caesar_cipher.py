alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
             'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
             't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your massage:\n").lower()
shift = int(input("Type the shift number:\n"))

def encript(text,shift):
    enc_text = ""
    for i in text:
        position = alphabet.index(i)
        new_position = position + shift
        new_letter = alphabet[new_position]
        enc_text += new_letter
        
    print(f"Your encoded message is {enc_text}")

def decript(text,shift):
    dec_text = ""
    for i in text:
        position = alphabet.index(i)
        new_position = position - shift
        new_letter = alphabet[new_position]
        dec_text += new_letter
        
    print(f"Your decoded massage is {dec_text}")

if direction == "encode":
    encript(text,shift)
elif direction == "decode":
    decript(text,shift)
else:
    print("Invalid input")

