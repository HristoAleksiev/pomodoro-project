from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 5
cycle_count = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global cycle_count

    cycle_count += 1

    if cycle_count == 8:
        timer_count(LONG_BREAK_MIN * 60)
        title.config(text="Break", fg=RED)
        cycle_count = 0
    else:
        if cycle_count % 2 == 0:
            timer_count(SHORT_BREAK_MIN * 60)
            title.config(text="Break", fg=PINK)
        else:
            timer_count(WORK_MIN * 60)
            title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def timer_count(count):
    minutes_to_count = math.floor(count / 60)
    second_to_count = count % 60

    if second_to_count < 10:
        second_to_count = f"0{second_to_count}"

    canvas.itemconfig(timer_display, text=f"{minutes_to_count}:{second_to_count}")
    if count > 0:
        window.after(200, timer_count, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Column 1

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

# Column 2

title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_display = canvas.create_text(100, 130, text=0, fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

checkmark = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
checkmark.grid(column=1, row=3)

# Column 3

reset = Button(text="Reset", highlightthickness=0)
reset.grid(column=2, row=2)

window.mainloop()
