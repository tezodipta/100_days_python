import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
new_dict = {
    row.letter:row.code for(index,row) in data.iterrows()
}

user_inp = input("Enter your name:").upper()

user_name = [new_dict[latter] for latter in user_inp]
print(user_name)


