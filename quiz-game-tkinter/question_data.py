import requests
import time
from question_model import Question
import html

TRIVIA_API_URL = "https://opentdb.com/api.php"


class QuestionData:

    def __init__(self, q_num: int) -> None:
        self.question_list = self.load_question(q_num)

    def load_question(self, q_num: int) -> list[Question]:
        response = requests.get(
            url=TRIVIA_API_URL,
            params={
                "amount": q_num,  # Kérdések száma
                "type": "boolean",  # True/False típus kérdéseket szeretnék lekérdezni
            })
        response.raise_for_status()

        data = response.json()
        if data["response_code"] != 0:
            time.sleep(1)
            return self.load_question(q_num)

        return [Question(html.unescape(question["question"]), question["correct_answer"] == "True")
                for question in data["results"]]
