from typing import List
from question_model import Question

class QuizBrain:
    """
    A QuizBrain osztály kezeli a kvízjáték logikáját.

    Attributes:
        question_number (int): Az aktuális kérdés sorszáma (0-tól kezdve)
        score (int): A játékos jelenlegi pontszáma
        question_list (List[Question]): A kvíz kérdéseinek listája
    """

    def __init__(self, q_list: List[Question]) -> None:
        """
        Inicializálja a QuizBrain objektumot.

        Args:
           q_list: A Question objektumok listája
        """
        self.question_number: int = 0
        self.score: int = 0
        self.question_list: List[Question] = q_list

    def still_has_questions(self) -> bool:
        """
        Ellenőrzi, hogy van-e még kérdés a kvízben.

        Returns:
            bool: True, ha van még kérdés, False, ha már nincs
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> None:
        """
        Megjeleníti a következő kérdést és bekéri a felhasználó válaszát.
        A válasz helyességét automatikusan ellenőrzi és frissíti a pontszámot.
        """
        # Aktuális kérdés lekérése a listából
        current_question = self.question_list[self.question_number]
        # Kérdésszám növelése (felhasználóbarát megjelenítéshez 1-től kezdjük)
        self.question_number += 1

        # Felhasználói válasz bekérése
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # Válasz ellenőrzése
        self.check_answer(user_answer, current_question.answer)
        print("\n")

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        """
       Ellenőrzi a felhasználó válaszát és frissíti a pontszámot.
       Visszajelzést ad a válasz helyességéről.

       Args:
           user_answer (str): A felhasználó által megadott válasz
           correct_answer (str): A helyes válasz
       """
        if user_answer.title() == correct_answer.title():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}.")

        print(f"Your current score is: {self.score}/{self.question_number}.")

    def final_score(self) -> None:
        """
        Megjeleníti a kvíz végső eredményét.
        Kiírja az összpontszámot és a kérdések teljes számát.
        """
        print(f"You've completed the quiz.")
        print(f"Your final score was: {self.score}/{self.question_number}.")
