from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler Trivia")
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)
        #Canvas card & text
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 290,
            text="Trivia Question goes here",
            fill=THEME_COLOR,
            font=("Arial", 14, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        #Score Label
        self.score_label = Label(text=f"Score: {0}", bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=1)
        #True/False Buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.respond_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.respond_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def respond_true(self):
        user_answer = "True"
        self.quiz.check_answer(user_answer)
        self.get_next_question()

    def respond_false(self):
        user_answer = "False"
        self.quiz.check_answer(user_answer)
        self.get_next_question()