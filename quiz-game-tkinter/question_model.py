class Question:
    """
    A Question osztály egy kvízkérdést reprezentál.

    Attributes:
        text (str): A kérdés szövege
        answer (bool): A kérdés helyes válasza
    """

    def __init__(self, q_text: str, q_answer: bool) -> None:
        """
        Inicializálja a Question objektumot.

        Args:
            q_text (str): A kérdés szövege
            q_answer (bool): A helyes válasz
        """
        self.text = q_text
        self.answer = q_answer
