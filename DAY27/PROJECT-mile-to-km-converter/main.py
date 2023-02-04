from tkinter import *

# TODO - set up window layout
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)


# TODO - function for conversion between miles to km when button clicked
def button_click():
    miles = float(user_input.get())
    km = 1.609344 * miles
    km_result.config(text=f"{km}")


# TODO - first row
user_input = Entry(width=7)
user_input.grid(row=0, column=1)
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

# TODO - second row
equal_label = Label(text="Miles")
equal_label.grid(row=1, column=0)
km_result = Label(text=0)
km_result.grid(row=1, column=1)
km_label = Label(text="Km")
km_label.grid(row=1, column=2)

# TODO - third row
button = Button(text="Calculate", command=button_click)
button.grid(row=2, column=1)

window.mainloop()
