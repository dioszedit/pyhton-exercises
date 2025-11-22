import requests
import time
from question_model import Question
import html

TRIVIA_API_URL = "https://opentdb.com/api.php"


class QuestionData:
    """
    A QuestionData osztály felelős a kvízkérdések betöltéséért az Open Trivia Database API-ból.

    Az osztály automatikusan kezeli az API kommunikációt, a válasz feldolgozását és a
    HTML entitások dekódolását.

    Attributes:
        question_list (list[Question]): A betöltött Question objektumok listája
    """

    def __init__(self, q_num: int) -> None:
        """
        Inicializálja a QuestionData objektumot és betölti a kérdéseket.

        Args:
            q_num (int): A betöltendő kérdések száma
        """
        self.question_list = self.load_question(q_num)
        self.max_retry_count = 5 # Adat betöltések maximális száma

    def load_question(self, q_num: int) -> list[Question]:
        """
        Kérdések letöltése az Open Trivia Database API-ból.

        A metódus igaz/hamis típusú kérdéseket tölt le, és HTML entitásokat dekódol.
        Hiba esetén 1 másodperc várakozás után újrapróbálkozik.

        Args:
            q_num (int): A letöltendő kérdések száma

        Returns:
            list[Question]: A betöltött Question objektumok listája

        Raises:
            requests.exceptions.HTTPError: Ha az API kérés sikertelen
        """
        response = requests.get(
            url=TRIVIA_API_URL,
            params={
                "amount": q_num,  # Kérdések száma
                "type": "boolean",  # True/False típus kérdéseket szeretnék lekérdezni
            })
        response.raise_for_status()

        data = response.json()
        # Ha az API hibakódot ad vissza, várunk és újrapróbálkozunk
        if data["response_code"] != 0 and self.max_retry_count > 0:
            time.sleep(1)
            self.max_retry_count -= 1
            return self.load_question(q_num)

        if data["response_code"] != 0 and self.max_retry_count == 0:
            raise Exception("The maximum number of retries for loading data has been reached.")

        # Question objektumok létrehozása, HTML entitások dekódolásával
        return [Question(html.unescape(question["question"]), question["correct_answer"] == "True")
                for question in data["results"]]
