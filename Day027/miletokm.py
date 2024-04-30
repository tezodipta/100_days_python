from tkinter import *
window = Tk()
window.title("miles to km")
window.minsize(width=200,height=100)
window.config(padx=20,pady=20)

def MileToKm():
    RSlabel["text"]= float(input.get()) * 1.609

input = Entry(width=8)
input.grid(row = 0,column = 1)

Mlabel = Label(text="Miles")
Mlabel.grid(column=2,row=0)

EQlabel = Label(text="is eqal to")
EQlabel.grid(column=0,row=1)

RSlabel = Label(text="0")
RSlabel.grid(column=1,row=1)

KMlabel =Label(text="Km")
KMlabel.grid(column=2,row=1)

button = Button(text="calculate",command=MileToKm)
button.grid(column=1,row=2)

window.mainloop()