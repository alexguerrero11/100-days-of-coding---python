import tkinter

# creating windows and label with Tkinter
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()  # will keep the window on screen and listen for keys
