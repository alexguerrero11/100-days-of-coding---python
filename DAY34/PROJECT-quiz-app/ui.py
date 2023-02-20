from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.questions_text = self.canvas.create_text(150, 100, width=280, text="", font=("Ariel", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_img = PhotoImage(file="images/false.png")
        self.unknown_button = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.unknown_button.grid(row=2, column=0)
        true_img = PhotoImage(file="images/true.png")
        self.known_button = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.known_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questions_text, text=q_text)
        else:
            self.canvas.itemconfig(self.questions_text, text="End of Quiz")
            # disable the buttons
            self.unknown_button.config(state="disabled")
            self.known_button.config(state="disabled")

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        # if answer is correct we want a green background
        if is_right:
            self.canvas.config(bg="green")
        # else if answer is wrong we want a red background
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
