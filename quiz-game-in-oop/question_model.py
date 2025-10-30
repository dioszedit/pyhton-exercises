class Question:
    """
    A Question osztály egy kvízkérdést reprezentál.

    Attributes:
        text (str): A kérdés szövege
        answer (str): A kérdés helyes válasza (általában "True" vagy "False")
    """

    def __init__(self, q_text: str, q_answer: str) -> None:
        """
        Inicializálja a Question objektumot.

        Args:
            q_text (str): A kérdés szövege
            q_answer (str): A helyes válasz
        """
        self.text = q_text
        self.answer = q_answer
