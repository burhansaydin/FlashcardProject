BACKGROUND_COLOR = "#B1DDC6"


from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)




canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 260, image=image)
canvas.create_text(400,150, text="German", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="sadfa", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

image_1 = PhotoImage(file="images/wrong.png")
button_1 = Button(image=image_1, bg=BACKGROUND_COLOR, highlightthickness=0)
button_1.grid(column=0, row=1)

image_2 = PhotoImage(file="images/right.png")
button_2 = Button(image=image_2, bg=BACKGROUND_COLOR, highlightthickness=0)
button_2.grid(column=1, row=1)














window.mainloop()
