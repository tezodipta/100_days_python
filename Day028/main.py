from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
marks = None
timer_loop = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer_loop)
    name_label.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    global marks
    marks = ""
    tick_label.config(text=marks)
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN *60
    break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        timer(long_break_sec)
        name_label.config(text="BREAK",fg=RED)

    elif REPS % 2 == 0:
        timer(break_sec)
        name_label.config(text="BREAK",fg=PINK)

    else:
        timer(work_sec)
        name_label.config(text="WORK",fg=GREEN)
            
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer(count):
    count_min = count // 60
    if count_min < 10:
        count_min = f"0{count_min}"

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer_loop
        timer_loop=window.after(1000,timer,count-1)

    else:
        start_timer()
        marks = ""
        work_session = REPS // 2
        for i in range(work_session):
            marks += "✔"
            tick_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

name_label = Label(text="Timer",font=(FONT_NAME,36,"bold"),bg=YELLOW,fg=GREEN)
name_label.grid(row=0,column=1)

photo = PhotoImage(file ="Day028/tomato.png")
canvas = Canvas(width=202,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(101,112,image=photo)

timer_text = canvas.create_text(102,134,text="00:00",font=(FONT_NAME,30,"bold"))
canvas.grid(row=1,column=1)

start_button = Button(text="START",command=start_timer)
start_button.grid(row=2,column=0)

tick_label = Label(text="",font=(FONT_NAME,18),bg=YELLOW,fg=GREEN)
tick_label.grid(row=3,column=1)

reset_button = Button(text="RESET",command=reset)
reset_button.grid(row=2,column=2)

window.mainloop()