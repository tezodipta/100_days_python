#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
"""name extraction"""
with open("Input/Names/invited_names.txt","r")as names_file:
    names = names_file.readlines()
    
        
    
"""name replacement and creating new letter"""
with open("Input/Letters/starting_letter.txt",mode="r")as letter:
    data = letter.read()
    for name in names:
        stripped_name = name.strip("\n")
        word_replaced = data.replace(PLACEHOLDER,stripped_name)

        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as send:
            send.write(word_replaced)
    
