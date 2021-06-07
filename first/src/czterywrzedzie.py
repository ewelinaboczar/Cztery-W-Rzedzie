import tkinter as tk
import numpy as np
import os
import time
import itertools as IT
from functools import partial
from tkinter import ttk,messagebox

from sprawdzanie_wygranej import czy_wygrana_pion, czy_wygrana_poziom, czy_wygrana_skos
from gra import graj, GameException, FullColumn, MoveOutOfRange

ROWS = 6
COLUMNS = 7


class okienko(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cztery w rzędzie")
        sprawdzanie_wygranej = [czy_wygrana_skos(), czy_wygrana_poziom(), czy_wygrana_pion()]

        # Tworzenie canvas dla gry
        canvas = tk.Canvas(self, bg="#0055FF")
        self.wyswietlanie_tablicy(canvas)
        canvas.pack(fill=tk.BOTH, expand=True)

        # Tworzenie przycisku rozwijalnego z regulami
        panel = tk.Frame(self)
        jakie_reguly = ["Wszystkie"] + [str(regula) for regula in sprawdzanie_wygranej]
        jakie_reguly_combb = ttk.Combobox(panel, width=15, values=jakie_reguly, state='readonly')
        jakie_reguly_combb.set("Wszystkie")
        jakie_reguly_combb.grid(row=1, column=4, sticky=tk.E + tk.W)
        panel.pack(side=tk.BOTTOM, fill=tk.X)

        # Tworzenie dolnego panelu powiadomień
        self.napis1 = tk.Label(panel, bd=1, text="Runda 1", relief=tk.RAISED, bg="lightgrey", fg="black")
        self.napis2 = tk.Label(panel, bd=1, text="Tura gracza nr 1", relief=tk.RAISED, bg="lightgrey", fg="black")
        self.napis3 = tk.Label(panel, bd=1, text="", relief=tk.RAISED, bg="white", fg="black")
        self.napis4 = tk.Button(panel, bd=1, text="Reset", relief=tk.RAISED, bg="lightgrey", fg="black",
                                command=self.reset(canvas,jakie_reguly_combb))

        panel.columnconfigure(0, weight=1)
        panel.columnconfigure(1, weight=1)
        panel.columnconfigure(2, weight=1)
        panel.columnconfigure(3, weight=1)
        panel.columnconfigure(4, weight=1)
        self.napis1.grid(row=1, column=0, sticky=tk.E + tk.W)
        self.napis2.grid(row=1, column=1, sticky=tk.E + tk.W)
        self.napis3.grid(row=1, column=2, sticky=tk.E + tk.W)
        self.napis4.grid(row=1, column=3, sticky=tk.E + tk.W)

        # Tworzenie przycisków do wrzucania
        przyciski_wrzut = tk.Frame(self)
        [tk.Button(przyciski_wrzut, text=str(i + 1), width=10, command=partial(self.wrzuc_monete,i+1,canvas)).grid(column=i,row=0)for i in range(COLUMNS)]
        for i in range(COLUMNS):
            przyciski_wrzut.columnconfigure(i, weight=1)
        przyciski_wrzut.pack(side=tk.TOP, fill=tk.X)

        messagebox.showinfo("Kto jest kim", f"Gracz X -> red\nGracz Y -> yellow")
        reg = self.jaka_regula(jakie_reguly_combb)
        self.game = graj(reg)

    def wyswietlanie_tablicy(self, canvas):
        self.plansza = [[None] * COLUMNS for _ in range(ROWS)]
        self.kolka = [[None] * COLUMNS for _ in range(COLUMNS)]
        for i, j in IT.product(range(ROWS), range(COLUMNS)):
            self.L =self.plansza[ROWS - 1 - i][j] =  tk.Canvas(canvas, bg="#0055FF", height=50, width=50, relief="raised",highlightthickness=0)
            padding = 2
            self.id=self.kolka[ROWS - 1 - i][j] = self.L.create_oval((padding, padding, 50 + padding, 50 + padding),fill="lightgrey")
            width = self.L.winfo_reqwidth()
            height = self.L.winfo_reqheight()
            self.L.configure(width=width, height=height)

            canvas.rowconfigure(i, weight=1)
            canvas.columnconfigure(j, weight=1)
            self.L.grid(row=i, column=j, padx=3, pady=3, sticky=tk.E + tk.W + tk.N + tk.S)

    def wrzuc_monete(self, kolumna,canvas):
        padding = 2
        kolor=["lightgrey","red","yellow"]
        try:
            self.game.twoj_ruch(kolumna-1)
            self.napis3.config(text="{}".format(kolumna))
        except FullColumn as exept:
            self.napis3.config(text="Kolumna {} jest pełna".format(kolumna))
            return
        except MoveOutOfRange as exept:
            self.napis3.config(text="Bledny numer kolumny")
            return

        for i in range(ROWS):
            for j in range(COLUMNS):
                numer = self.game.tablica[i][j]
                if numer == 'X':
                    numer = 1
                elif numer == 'Y':
                    numer = 2
                elif numer != 'Y' and numer != 'X':
                    numer = 0
                padding = 2
                self.plansza[i][j].itemconfig(self.id,fill=kolor[numer])

        self.napis2.config(text="Tura gracza {}".format(self.game.tura))
        self.napis1.config(text="Runda {}".format(self.game.runda))
        if self.game.ktory_gracz_wygral():
            self.napis3.config(text="Zwyciezyl gracz {}".format(self.game.zwyciesca))
            self.napis2.config(text="Koniec gry")
            messagebox.showinfo("Status gry", f"Wygrał gracz {self.game.zwyciesca}")
            return

    def jaka_regula(self,jakie_reguly_combb):
        wybor = jakie_reguly_combb.get()
        return wybor

    def reset(self,canvas,jakie_reguly_combb):
        self.napis1.config(text="Runda 1")
        self.napis2.config(text="Tura gracza X")
        self.napis3.config(text="")
        #self.game.resetowanie_gry()
        self.wyswietlanie_tablicy(canvas)
        self.gracz=1
        self.czy_gramy_dalej=True



app = okienko()
app.mainloop()





