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
        self.current_question = None
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

    def next_question(self) -> str:
        """
        Megjeleníti a következő kérdést és bekéri a felhasználó válaszát.
        A válasz helyességét automatikusan ellenőrzi és frissíti a pontszámot.
        """
        # Aktuális kérdés lekérése a listából
        self.current_question = self.question_list[self.question_number]
        # Kérdésszám növelése (felhasználóbarát megjelenítéshez 1-től kezdjük)
        self.question_number += 1

        return f"Q{self.question_number}: {self.current_question.text}"

    def check_answer(self, user_answer: bool) -> bool:
        """
       Ellenőrzi a felhasználó válaszát és frissíti a pontszámot.
       Visszajelzést ad a válasz helyességéről.

       Args:
           user_answer (bool): A felhasználó által megadott válasz
       """
        if user_answer == self.current_question.answer:
            self.score += 1
            return True
        return False
