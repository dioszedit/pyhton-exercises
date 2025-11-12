from constants import *


class PomodoroTimer:
    """
    Pomodoro időzítő osztály, ami kezeli a munka- és szünetidőket.

    A Pomodoro technika: 25 perc munka, 5 perc rövid szünet,
    4 ciklus után 20 perc hosszú szünet.
    """

    def __init__(self) -> None:
        """Inicializálás: alaphelyzetbe állítjuk a számlálókat."""
        self.reps = 0  # Hányadik körben vagyunk (munka és szünet egyaránt számít)
        self.timer = 0  # Hátralévő idő másodpercekben

    def start(self) -> None:
        """Timer indítása: nullázás és az első munka periódus kezdése."""
        self.reps = 0
        self.start_work()

    def reset(self) -> None:
        """Timer visszaállítása alaphelyzetbe."""
        self.reps = 0
        self.timer = 0

    def start_break(self, is_short: bool) -> None:
        """
        Szünet indítása.

        Args:
            is_short: True = rövid szünet (5 perc), False = hosszú szünet (20 perc)
        """
        self.reps += 1
        if is_short:
            self.timer = SHORT_BREAK_MIN * 60
        else:
            self.timer = LONG_BREAK_MIN * 60

    def start_work(self) -> None:
        """Munka periódus indítása (25 perc)."""
        self.reps += 1
        self.timer = WORK_MIN * 60

    def processing(self) -> None:
        """
        Timer feldolgozása: minden másodpercben meghívódik.
        Kezeli az átmeneteket munka és szünet periódusok között.
        """
        if self.reps > 0:  # Csak akkor fut, ha el van indítva
            self.timer -= 1  # Egy másodperc levonása

            # Ha lejárt az idő, eldöntjük mi következik
            if self.timer == 0 and self.reps % 8 == 0:
                # 8. kör után (4 teljes Pomodoro) vége, alap helyzetbe állítjuk
                self.reset()
            elif self.timer == 0 and self.reps % 7 == 0:
                # 7. kör után (4. munka után) hosszú szünet következik
                self.start_break(is_short=False)
            elif self.timer == 0 and self.reps % 2 == 0:
                # Páros körök végén (szünet után) munka következik
                self.start_work()
            elif self.timer == 0 and self.reps % 2 == 1:
                # Páratlan körök végén (munka után) rövid szünet következik
                self.start_break(is_short=True)

    def timer_text(self) -> str:
        """
        Timer szövegének formázása "00:00" alakban (perc:másodperc).

        Returns:
            Formázott időt tartalmazó string (pl. "24:59")
        """
        minutes = self.timer // 60  # Egész osztás: hány teljes perc van
        seconds = self.timer % 60  # Maradék: hány másodperc marad
        """
        f-string-nél használt formázással érem el a megfelelő formátumot, ahol
        ´:02d´ a következőt jelenti
            - ´:´ jelzi hogy formázás következik
            - ´0´ nullával való kitöltés ha kell
            - ´2´ összesen 2 karakter széles legyen
            - ´d´ decimális egész szám
        """
        return f"{minutes:02d}:{seconds:02d}"

    def level_text(self) -> str:
        """
        Befejezett Pomodoro körök vizuális jelzése check mark-okkal.

        Returns:
            String, ami annyi check mark-ot tartalmaz, ahány kört befejezett
        """
        check_marks = ""
        completed_work_sessions = self.reps // 2  # Minden 2. kör egy befejezett munka
        for _ in range(completed_work_sessions):
            check_marks += CHECK_MARK

        return check_marks

    def timer_status_data(self) -> dict[str, str]:
        """
        Timer aktuális állapotának adatai (cím és szín).

        Returns:
            Dictionary 'text' és 'color' kulcsokkal
        """
        if self.reps == 0:
            # Alaphelyzet, még nem indult el
            return {'text': 'Időzítő', 'color': GREEN}
        elif self.reps % 2 == 1:
            # Páratlan körök: munka periódus
            return {'text': 'Munka', 'color': GREEN}
        elif self.reps % 8 == 0:
            # 8. kör: hosszú szünet
            return {'text': 'Szünet', 'color': RED}
        else:
            # Egyéb páros körök: rövid szünet
            return {'text': 'Szünet', 'color': PINK}
