from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.config(pady=20, padx=20, background=THEME_COLOR)
        self.window.title("Quizzler")
        self.cur_score = 0

        self.score_label = Label(text=f"Score: {self.cur_score}", background=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(self.window, width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Hello", font=("Arial 20 italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, columnspan=2, pady=20, padx=20)

        img_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=img_true, highlightthickness=0, command=self.check_if_true)
        self.button_true.grid(row=2, column=1)

        img_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=img_false, highlightthickness=0, command=self.check_if_false)
        self.button_false.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def check_if_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def check_if_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)






