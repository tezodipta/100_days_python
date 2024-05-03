from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters = [choice(letters) for i in range(randint(8,10))]
    password_symbols = [choice(symbols) for i in range(randint(2,4))]
    password_numbers = [choice(numbers) for i in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.delete(0,END)
    pass_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open("Day030/advance_pw_generator/data.json","r") as data_file:
            data = json.load(data_file)
            search_mail = data[website]["email"]
            search_pass = data[website]["password"]
    except FileNotFoundError:
        messagebox.showerror(title="ERROR",message="No Data File Found")
    except KeyError:
        messagebox.showerror(title="ERROR",message="No details for the website exists")
    else:
        messagebox.showinfo(title = website,message=f"Email: {search_mail}\nPassword: {search_pass}")
        pyperclip.copy(f"{search_mail} {search_pass}")  

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()

    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }

    if(not website or not email or not password ):
        messagebox.showerror(title="ERROR",message="Please Dont leave any empty fields")

    else:
        isok = messagebox.askokcancel(title="ARE YOU SURE",message=f"The details are:\nWebsite: {website}\nEmail: {email}\nPassword: {password}\nIS it ok to Save??")
        if isok:
            try:
                with open("Day030/advance_pw_generator/data.json","r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("Day030/advance_pw_generator/data.json","w") as data_file:
                    json.dump(new_data,data_file,indent = 4)
            else:
                data.update(new_data)
                with open("Day030/advance_pw_generator/data.json","w") as data_file:
                    json.dump(data,data_file,indent = 4)
            
            website_input.delete(0,END)
            pass_input.delete(0,END)
            email_input.delete(0,END)
            email_input.insert(END,"@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
photo=PhotoImage(file="Day029\logo.png")
canvas = Canvas(width=200,height=200)
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_input = Entry(width=31)
website_input.grid(column=1,row=1)
website_input.focus()

search_button = Button(text="Search",width=14,command=search)
search_button.grid(column=2,row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_input = Entry(width=50)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(END,"@gmail.com")

pass_label = Label(text="Password:")
pass_label.grid(column=0,row=3)

pass_input = Entry(width=31)
pass_input.grid(column=1,row=3)

generate_button = Button(text="Generate Password",command=generate_pass)
generate_button.grid(column=2,row=3)

add_button = Button(text="Add",width=42,command=save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()