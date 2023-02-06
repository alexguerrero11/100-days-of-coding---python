from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ---------------------------- DATA ------------------------------- #
filename = "data/french_words.csv"
try:
    data = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    master_data = pd.read_csv(filename)
    to_learn = master_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# TODO - Creating a window in tkinter
# -------------------------- UI SETUP ------------------------------ #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# ------------------------- FUNCTION ------------------------------- #
# TODO - function to get next word
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# TODO - function to flip card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)


# TODO - function is going to remove known words from list
def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pd.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index=False)


flip_timer = window.after(3000, func=flip_card)

# front card image
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Creating the two buttons for the cards
# Unknown button for cards not fully known
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# Known button for cards that are known pretty well
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
