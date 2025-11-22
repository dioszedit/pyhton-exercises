from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"
FONT_SIZE = 18
FONT_STYLE = "italic"


class QuizUI:
    """
    A QuizUI osztály létrehozza és kezeli a kvízjáték grafikus felhasználói felületét.

    Az osztály Tkinter-t használ a GUI megjelenítéséhez, és kezeli a felhasználói
    interakciókat, vizuális visszajelzéseket és a kérdések megjelenítését.

    Attributes:
        quiz (QuizBrain): A kvíz logikáját kezelő objektum
        score (int): A játékos jelenlegi pontszáma
        after_id (str | None): A tervezett callback azonosítója (késleltetett műveletek kezeléséhez)
        window (Tk): A főablak objektum
        score_label (Label): Pontszám megjelenítő címke
        canvas (Canvas): Kérdések megjelenítéséhez használt vászon
        question_text (int): A vásznon megjelenő kérdés szövegének azonosítója
        true_button (Button): Igaz válasz gomb
        false_button (Button): Hamis válasz gomb
    """

    def __init__(self, quiz: QuizBrain) -> None:
        """
        Inicializálja a QuizUI objektumot és létrehozza a grafikus felületet.

        Args:
            quiz (QuizBrain): A kvíz logikáját kezelő objektum
        """
        self.quiz = quiz
        self.after_id = None

        # Főablak létrehozása és beállítása
        self.window = Tk()
        self.window.title("Quiz Game - True or False")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Pontszám megjelenítő címke
        self.score_label = Label(
            text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}",
            fg="white",
            bg=THEME_COLOR,
            font=(FONT_NAME, FONT_SIZE),
        )
        self.score_label.grid(column=0, row=0, columnspan=2, sticky=E, padx=10, pady=10)

        # Kérdés megjelenítő vászon
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="",
                                                     width=280,
                                                     fill="black",
                                                     font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Igaz gomb (zöld, pipa jel)
        self.true_button = Button(
            text="✓",
            highlightthickness=0,
            bg="green",
            fg="white",
            font=(FONT_NAME, FONT_SIZE),
            padx=15,
            pady=15,
            command=lambda: self.check_answer(True)
        )
        self.true_button.grid(column=0, row=2)

        # Hamis gomb (piros, x jel)
        self.false_button = Button(
            text="✗",
            highlightthickness=0,
            bg="red",
            fg="white",
            font=(FONT_NAME, FONT_SIZE),
            padx=15,
            pady=15,
            command=lambda: self.check_answer(False)
        )
        self.false_button.grid(column=1, row=2)

        # Első kérdés betöltése
        self.get_next_question()

        # Az alkalmazás főciklusa - ez tartja futva az ablakot
        self.window.mainloop()

    def get_next_question(self) -> None:
        """
        Betölti és megjeleníti a következő kérdést a vásznon.

        A metódus lekéri a következő kérdést a QuizBrain-től és frissíti
        a vászon szövegét fekete színnel.
        """
        self.canvas.itemconfig(
            self.question_text,
            text=self.quiz.next_question(),
            fill="black"
        )

    def check_answer(self, answer: bool) -> None:
        """
        Ellenőrzi a felhasználó válaszát és vizuális visszajelzést ad.

        A metódus:
        - Ellenőrzi a választ a QuizBrain segítségével
        - Frissíti a pontszámot
        - Vizuális visszajelzést ad (zöld/piros háttér)
        - Letiltja a gombokat
        - 2 másodperc után automatikusan betölti a következő kérdést

        Args:
            answer (bool): A felhasználó által választott válasz (True/False)
        """
        is_correct = self.quiz.check_answer(answer)

        # Pontszám frissítése
        self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")

        # Vizuális visszajelzés
        self.canvas.itemconfig(self.question_text, fill="white")
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # Gombok letiltása a válasz után
        self.true_button.config(state="disabled", bg="gray")
        self.false_button.config(state="disabled", bg="gray")

        # 2 másodperc várakozás után következő kérdés vagy befejezés
        self.after_id = self.window.after(2000, func=self.still_has_questions)

    def still_has_questions(self) -> None:
        """
        Ellenőrzi, hogy van-e még kérdés, és ennek megfelelően folytatja vagy befejezi a játékot.

        Ha van még kérdés:
        - Visszaállítja a vászon háttérszínét fehérre
        - Újra engedélyezi a gombokat
        - Betölti a következő kérdést

        Ha nincs több kérdés:
        - Eltávolítja a gombokat
        - Befejező üzenetet jelenít meg
        """
        # Tervezett callback törlése
        if self.after_id is not None:
            self.window.after_cancel(self.after_id)
            self.after_id = None

        # Vászon alaphelyzetbe állítása
        self.canvas.config(bg="white")


        if self.quiz.still_has_questions():
            # Van még kérdés - folytatás
            self.true_button.config(state="normal", bg="green")
            self.false_button.config(state="normal", bg="red")
            self.get_next_question()
        else:
            # Nincs több kérdés - játék vége
            self.score_label.destroy()
            self.true_button.destroy()
            self.false_button.destroy()
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've completed the quiz!\n\nFinal Score: {self.quiz.score}/{len(self.quiz.question_list)}",
                fill="black"
            )
