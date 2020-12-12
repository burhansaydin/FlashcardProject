from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/german_words.csv", delimiter="\t")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_word = current_card["German"]
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=f"{current_word}", fill="black")
    canvas.itemconfig(card_background, image=new_image,)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


def flip_card():
    canvas.itemconfig(card_background, image=old_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
new_image = PhotoImage(file="images/card_front.png")
old_image = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 260, image=new_image)
card_title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

image_1 = PhotoImage(file="images/wrong.png")
button_1 = Button(image=image_1, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_word)
button_1.grid(column=0, row=1)

image_2 = PhotoImage(file="images/right.png")
button_2 = Button(image=image_2, bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
button_2.grid(column=1, row=1)


next_word()


window.mainloop()
