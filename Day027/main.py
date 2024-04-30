from tkinter import *
window = Tk()
window.title("First GUI")
# window.minsize(width=300,height=300) 

my_label = Label(text="this is a label")
my_label.grid(row=0,column=0)

def butt_clicked():
    my_label["text"] = "label changed"
    #0r
    # my_label.config(text="label changed")

input = Entry(width=20)
input.grid(row=3,column=3)

def inpToLabel():
    my_label["text"] = input.get()
    my_label.config(text=input.get())
    #changing the label with the input box
    

#creating a button
my_button = Button(text = "click me",command=inpToLabel)
#command will do the assign task if the btton is clicked
my_button.grid(column=1,row=1)

my_button2 = Button(text="2nd button")
my_button2.grid(row=0,column=2)


#creating a input box

#make him alive
window.mainloop()