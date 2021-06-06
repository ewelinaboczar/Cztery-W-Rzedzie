import tkinter as tk
import numpy as np
import os
import time
import itertools as IT
from functools import partial
from tkinter import ttk

from sprawdzanie_wygranej import czy_wygrana_pion, czy_wygrana_poziom, czy_wygrana_skos
from gra import graj, GameException, FullColumn, MoveOutOfRange

ROWS = 6
COLUMNS = 7


class okienko(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cztery w rzędzie")
        sprawdzanie_wygranej = [czy_wygrana_skos(), czy_wygrana_poziom(), czy_wygrana_pion()]
        self.ustawienie_regul = graj(reguly=sprawdzanie_wygranej)

        # Tworzenie canvas dla gry
        canvas = tk.Canvas(self, bg="#0055FF")
        self.wyswietlanie_tablicy(canvas)
        canvas.pack(fill=tk.BOTH, expand=True)

        # Tworzenie dolnego panelu powiadomień
        panel = tk.Frame(self)
        self.napis1 = tk.Label(panel, bd=1, text="Runda 1", relief=tk.RAISED, bg="lightgrey", fg="black")
        self.napis2 = tk.Label(panel, bd=1, text="Tura gracza nr 1", relief=tk.RAISED, bg="lightgrey", fg="black")
        self.napis3 = tk.Label(panel, bd=1, text="", relief=tk.RAISED, bg="white", fg="black")
        self.napis4 = tk.Button(panel, bd=1, text="Reset", relief=tk.RAISED, bg="lightgrey", fg="black",
                                command=self.reset)

        panel.columnconfigure(0, weight=1)
        panel.columnconfigure(1, weight=1)
        panel.columnconfigure(2, weight=1)
        panel.columnconfigure(3, weight=1)
        panel.columnconfigure(4, weight=1)
        self.napis1.grid(row=1, column=0, sticky=tk.E + tk.W)
        self.napis2.grid(row=1, column=1, sticky=tk.E + tk.W)
        self.napis3.grid(row=1, column=2, sticky=tk.E + tk.W)
        self.napis4.grid(row=1, column=3, sticky=tk.E + tk.W)

        # Tworzenie przycisku rozwijalnego z regulami
        jakie_reguly = ["Wszystkie"] + [str(regula) for regula in sprawdzanie_wygranej]
        self.jakie_reguly_Combobox = ttk.Combobox(panel, width=15, values=jakie_reguly, state='readonly')
        self.jakie_reguly_Combobox.set("Wszystkie")
        self.jakie_reguly_Combobox.grid(row=1, column=4, sticky=tk.E + tk.W)
        panel.pack(side=tk.BOTTOM, fill=tk.X)

        # Tworzenie przycisków do wrzucania
        przyciski_wrzut = tk.Frame(self)
        [tk.Button(przyciski_wrzut, text=str(i + 1), width=10, command=partial(self.wrzuc_monete, i + 1)).grid(column=i,
                                                                                                               row=0)
         for i in range(COLUMNS)]
        for i in range(COLUMNS):
            przyciski_wrzut.columnconfigure(i, weight=1)
        przyciski_wrzut.pack(side=tk.TOP, fill=tk.X)

        self.reset()
        reg = ()
        reg = self.jaka_regula()
        self.game = graj(reg)

    def wyswietlanie_tablicy(self, canvas):
        self.plansza = [[None] * COLUMNS for _ in range(ROWS)]
        self.kolka = [[None] * COLUMNS for _ in range(COLUMNS)]
        kolor = ["lightgrey", "red", "yellow"]
        for i, j in IT.product(range(ROWS), range(COLUMNS)):
            self.plansza[ROWS - 1 - i][j] = L = tk.Canvas(canvas, bg="#0055FF", height=50, width=50, relief="raised",
                                                          highlightthickness=0)
            padding = 2
            numer = self.ustawienie_regul.tablica[i][j]
            if numer == 'X':
                numer = 1
            elif numer == 'Y':
                numer = 2
            else:
                numer = 0
            id = self.kolka[ROWS - 1 - i][j] = L.create_oval((padding, padding, 50 + padding, 50 + padding),
                                                             fill=kolor[numer])
            width = L.winfo_reqwidth()
            height = L.winfo_reqheight()
            L.configure(width=width, height=height)

            canvas.rowconfigure(i, weight=1)
            canvas.columnconfigure(j, weight=1)
            L.grid(row=i, column=j, padx=3, pady=3, sticky=tk.E + tk.W + tk.N + tk.S)

    def wrzuc_monete(self, kolumna):
        gracz = self.game.tura
        self.gracz1_kolor = 'Red' if gracz == 'X' else 'Yellow'
        self.gracz2_kolor = 'Yellow' if gracz == 'Y' else 'Red'

        try:
            self.game.twoj_ruch(kolumna)
            self.napis3.config(text="".format(kolumna))
        except FullColumn as exept:
            self.napis3.config(text="Kolumna {} jest pełna".format(kolumna))
            return

        self.napis2.config(text="Tura gracza {}".format(self.gracz))
        self.wyswietlanie_tablicy()
        self.canvas.update()

    def jaka_regula(self):
        sprawdzanie_wygranej = [czy_wygrana_skos(), czy_wygrana_poziom(), czy_wygrana_pion()]
        wybor = self.jakie_reguly_Combobox.get()
        if wybor == "Wszystkie":
            self.ustawienie_regul.reguly = sprawdzanie_wygranej
        else:
            inna_regula = [regula for regula in sprawdzanie_wygranej if str(regula) == wyboor]
            if inna_regula:
                self.ustawienie_regul.reguly = inna_regula

    def reset(self):
        pass


app = okienko()
app.mainloop()





