from tkinter import *
from tkinter import ttk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CARD_COLOR = "#ffffff"
CORRECT_COLOR = "#3cb371"
WRONG_COLOR = "#e74c3c"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # ---------- WINDOW ----------
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        # ---------- TOP BAR ----------
        self.title_label = Label(
            text="Quizzler Trivia",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 18, "bold")
        )
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="w")

        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 12, "bold")
        )
        self.score_label.grid(row=0, column=1, sticky="e")

        # Question counter below title
        self.counter_label = Label(
            text="Q 0 / 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial", 10, "italic")
        )
        self.counter_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

        # ---------- QUESTION CARD ----------
        self.canvas = Canvas(width=340, height=260, bg=CARD_COLOR, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            170,
            130,
            text="Some question text",
            width=300,
            font=("Arial", 16, "bold"),
            fill=THEME_COLOR,
        )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=(0, 20))

        # ---------- PROGRESS BAR ----------
        total_questions = len(self.quiz.question_list)
        self.progress = ttk.Progressbar(
            self.window,
            orient="horizontal",
            length=340,
            mode="determinate",
            maximum=total_questions,
        )
        self.progress.grid(row=3, column=0, columnspan=2, pady=(0, 10))

        # ---------- BUTTONS ----------
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(
            image=self.true_img,
            bg=THEME_COLOR,
            highlightthickness=0,
            activebackground=THEME_COLOR,
            borderwidth=0,
            command=self.true_pressed,
        )
        self.true_button.grid(row=4, column=0, pady=(10, 0), padx=(0, 10))

        self.false_button = Button(
            image=self.false_img,
            bg=THEME_COLOR,
            highlightthickness=0,
            activebackground=THEME_COLOR,
            borderwidth=0,
            command=self.false_pressed,
        )
        self.false_button.grid(row=4, column=1, pady=(10, 0), padx=(10, 0))

        # Start quiz
        self.update_meta()
        self.get_next_question()

        self.window.mainloop()

    # ---------- QUIZ FLOW ----------

    def update_meta(self):
        """Update score label, question counter, and progress bar."""
        current = self.quiz.question_number
        total = len(self.quiz.question_list)
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.counter_label.config(text=f"Q {current}/{total}")
        self.progress["value"] = current

    def get_next_question(self):
        self.canvas.config(bg=CARD_COLOR)
        self.enable_buttons()

        if self.quiz.still_has_questions():
            self.update_meta()
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz!\n\nFinal score: {self.quiz.score}",
            )
            self.disable_buttons()

    def true_pressed(self):
        self.handle_answer("True")

    def false_pressed(self):
        self.handle_answer("False")

    def handle_answer(self, user_answer: str):
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)

    # ---------- UI HELPERS ----------

    def give_feedback(self, is_right: bool):
        self.disable_buttons()
        if is_right:
            self.canvas.config(bg=CORRECT_COLOR)
        else:
            self.canvas.config(bg=WRONG_COLOR)
        # wait, then load next question
        self.window.after(800, self.get_next_question)

    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def enable_buttons(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
