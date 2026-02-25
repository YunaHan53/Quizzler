from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler Trivia")
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)
        #Canvas card & text
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
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
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
