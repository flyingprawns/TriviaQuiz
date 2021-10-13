import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE_FONT = ("Arial", 12, "bold")
QUESTION_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # Create quiz
        self.quiz = quiz_brain
        # Create GUI window
        self.window = tkinter.Tk()
        self.window.title("Trivia Quiz!")
        self.window.config(pady=20, padx=35, bg=THEME_COLOR)
        self.window.minsize(width=374, height=562)
        self.window.maxsize(width=374, height=562)
        # Create score
        self.score = tkinter.Label(text="Score: 0", font=SCORE_FONT)
        self.score.config(bg=THEME_COLOR, fg="white")
        self.score.grid(row=1, column=2, sticky="W", pady=10)
        # Create question
        self.question = tkinter.Canvas(width=300, height=270, bg="white")
        self.question_text = self.question.create_text(150, 135, text="default question",
                                                       width=280,
                                                       fill=THEME_COLOR, font=QUESTION_FONT)
        self.question.grid(row=2, column=1, columnspan=2, pady=30)
        # Create "true" button
        true_img = tkinter.PhotoImage(file="./images/true.png")
        self.true_button = tkinter.Button(image=true_img,
                                          command=self.true_button_press)
        self.true_button.config(bg=THEME_COLOR)
        self.true_button.grid(row=3, column=1, pady=20)
        # Create "false" button
        false_img = tkinter.PhotoImage(file="./images/false.png")
        self.false_button = tkinter.Button(image=false_img,
                                           command=self.false_button_press)
        self.false_button.config(bg=THEME_COLOR)
        self.false_button.grid(row=3, column=2, pady=20)
        # Display first question
        self.next_question()
        # Keep window open
        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            # Update the score and quiz text.
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question.itemconfig(self.question_text, text=q_text)
            # (re)-enable buttons so user can answer
            self.enable_buttons()
        else:
            # Show end message and disable buttons
            self.question.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.disable_buttons()
        # Change question background to white
        self.question.config(bg="white")

    def true_button_press(self):
        # Disable buttons to prevent bugs
        self.disable_buttons()
        # Check answer and give feedback
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_button_press(self):
        # Disable buttons to prevent bugs
        self.disable_buttons()
        # Check answer and give feedback
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        # Change question canvas to green/red for 1 second
        if is_right:
            self.question.config(bg="green")
        else:
            self.question.config(bg="red")
        # Get next question
        # WARNING: be very careful with this method. It is not well documented and can lead to unexpected bugs.
        self.window.after(1000, self.next_question)

    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def enable_buttons(self):
        self.true_button.config(state="active")
        self.false_button.config(state="active")

    def show_window_size(self):
        # For debugging purposes. Prints the measurements of the main window.
        print(self.window.winfo_width(), self.window.winfo_height())
