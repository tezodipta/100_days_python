from tkinter import *
import pandas as pd
import random as rm

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_lern = {}
try:
    data = pd.read_csv("Day031/data/unknown_words.csv")
except FileNotFoundError:
    data = pd.read_csv("Day031/data/french_words.csv")
    to_lern = data.to_dict(orient="records")
else:
    to_lern = data.to_dict(orient="records")



def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = rm.choice(to_lern)
    canvas.itemconfig(card_titile,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front)
    flip_timer = window.after(3000,flip_card)

def is_known():
    to_lern.remove(current_card)
    data = pd.DataFrame(to_lern)
    data.to_csv("Day031/data/unknown_words.csv",index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_titile,text="English",fill = "white")
    canvas.itemconfig(card_word,text=current_card["English"], fill = "white")
    canvas.itemconfig(card_background,image=card_back)

window =Tk()
window.title("flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,flip_card)

canvas = Canvas(width=800,height=526)
card_front = PhotoImage(file="Day031\images\card_front.png")
card_back = PhotoImage(file="Day031\images\card_back.png")
card_background = canvas.create_image(400,263,image=card_front)
card_titile = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image = PhotoImage(file="Day031\images\wrong.png")
wrong_button = Button(image=cross_image,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

check_image = PhotoImage(file="Day031/images/right.png")
right_button = Button(image=check_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

next_card()

window.mainloop()