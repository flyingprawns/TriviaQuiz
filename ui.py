import tkinter

THEME_COLOR = "#375362"
SCORE_FONT = ("Arial", 12, "bold")
QUESTION_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self):
        # Create GUI window
        self.window = tkinter.Tk()
        self.window.title("Trivia Quiz!")
        self.window.config(pady=20, padx=35, bg=THEME_COLOR)
        self.window.minsize(width=374, height=522)
        # Create score
        self.score = tkinter.Label(text="Score: 0", font=SCORE_FONT)
        self.score.config(bg=THEME_COLOR, fg="white")
        self.score.grid(row=1, column=2, sticky="W", pady=10)
        # Create question
        self.question = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.question.create_text(150, 125, text="question text",
                                                       fill=THEME_COLOR, font=QUESTION_FONT)
        self.question.grid(row=2, column=1, columnspan=2, pady=20)
        # Create "true" button
        true_img = tkinter.PhotoImage(file="./images/true.png")
        self.true_button = tkinter.Button(image=true_img)
        self.true_button.config(bg=THEME_COLOR)
        self.true_button.grid(row=3, column=1, pady=20)
        # Create "false" button
        false_img = tkinter.PhotoImage(file="./images/false.png")
        self.false_button = tkinter.Button(image=false_img)
        self.false_button.config(bg=THEME_COLOR)
        self.false_button.grid(row=3, column=2, pady=20)
        # Keep window open
        self.window.mainloop()

    def show_window_size(self):
        # For debugging purposes. Prints the measurements of the main window.
        print(self.window.winfo_width(), self.window.winfo_height())
        