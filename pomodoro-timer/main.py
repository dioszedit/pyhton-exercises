from constants import *
from tkinter import *
import pomodoro_timer


def proceed_timer() -> None:
    """
    Timer folyamatos frissítése: minden másodpercben meghívódik.
    Frissíti a UI elemeket (cím, időzítő, befejezett körök).
    """
    pomodoro.processing()

    # Cím és színének frissítése
    title_data = pomodoro.timer_status_data()
    title_label.config(text=title_data['text'], fg=title_data['color'])

    # Időzítő szövegének frissítése
    canvas.itemconfig(timer_label, text=pomodoro.timer_text())

    # Befejezett körök jelzésének frissítése
    check_mark_label.config(text=pomodoro.level_text())

    # Újrahívás 1000ms (1 másodperc) múlva
    window.after(1000, proceed_timer)


# ---------------------------- UI SETUP ------------------------------- #

# Főablak létrehozása és beállítása
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Pomodoro timer példány létrehozása
pomodoro = pomodoro_timer.PomodoroTimer()

# Cím label (Időzítő/Munka/Szünet)
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Canvas a paradicsom képpel és az időzítővel
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)

# Időzítő szöveg a canvas-on
timer_label = canvas.create_text(100, 130, text=pomodoro.timer_text(), fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start gomb
start_button = Button(
    text="Start",
    font=(FONT_NAME, 18),
    highlightthickness=0,
    borderwidth=1,
    padx=10,
    pady=5,
    command=pomodoro.start
)
start_button.grid(column=0, row=2)

# Mégse (Reset) gomb
cancel_button = Button(
    text="Mégse",
    font=(FONT_NAME, 18),
    highlightthickness=0,
    borderwidth=1,
    padx=10,
    pady=5,
    command=pomodoro.reset
)
cancel_button.grid(column=2, row=2)

# Befejezett körök jelzése (check mark-ok)
check_mark_label = Label(text=pomodoro.level_text(), fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20), )
check_mark_label.grid(column=1, row=3)

# Timer indítása
proceed_timer()
window.mainloop()
