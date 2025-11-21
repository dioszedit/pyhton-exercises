import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"
FONT_SIZE = 20
FONT_STYLE = "italic"


class QuizUI:

    def __init__(self, quiz: QuizBrain) -> None:
        self.quiz = quiz
        self.score = 0
        self.after_id = None

        # Főablak létrehozása és beállítása
        self.window = Tk()
        self.window.title("Quiz Game - True or False")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(
            text=f"Score: {len(self.quiz.question_list)}/{self.score}",
            fg="white",
            bg=THEME_COLOR,
            font=(FONT_NAME, 18),
        )
        self.score_label.grid(column=0, row=0, columnspan=2, sticky=E, padx=10, pady=10)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="",
                                                     width=280,
                                                     fill="black",
                                                     font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_button = Button(
            text="✓",
            highlightthickness=0,
            bg="green",
            fg="white",
            font=(FONT_NAME, 18),
            padx=15,
            pady=15,
            command=lambda: self.check_answer(True)
        )
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(
            text="✗",
            highlightthickness=0,
            bg="red",
            fg="white",
            font=(FONT_NAME, 18),
            padx=15,
            pady=15,
            command=lambda: self.check_answer(False)
        )
        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        # Az alkalmazás főciklusa - ez tartja futva az ablakot
        self.window.mainloop()

    def get_next_question(self) -> None:
        self.canvas.itemconfig(
            self.question_text,
            text=self.quiz.next_question(),
            fill="black"
        )

    def check_answer(self, answer: bool) -> None:
        is_correct = self.quiz.check_answer(answer)
        self.score_label.config(text=f"Score: {len(self.quiz.question_list)}/{self.quiz.score}")

        self.canvas.itemconfig(self.question_text, fill="white")
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.true_button.config(state="disabled", bg="gray")
        self.false_button.config(state="disabled", bg="gray")
        self.after_id = self.window.after(2000, func=self.still_has_questions)

    def still_has_questions(self) -> None:
        if self.after_id is not None:
            self.window.after_cancel(self.after_id)
            self.after_id = None

        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.true_button.config(state="normal", bg="green")
            self.false_button.config(state="normal", bg="red")
            self.get_next_question()
        else:
            self.true_button.destroy()
            self.false_button.destroy()
            self.canvas.itemconfig(
                self.question_text,
                text="You've completed the quiz!",
                fill="black"
            )
