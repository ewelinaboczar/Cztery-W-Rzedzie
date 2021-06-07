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
        fontStyle = ('Raleway', 10)

        # Tworzenie canvas dla gry
        self.canvas = tk.Canvas(self, bg="#00BFFF")
        self.wyswietlanie_tablicy()
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Tworzenie przycisku rozwijalnego z regulami
        panel = tk.Frame(self)
        self.jakie_reguly = ["Wszystkie","cztery w pionie","cztery w poziomie","cztery po skosie"]
        self.jakie_reguly_combb = ttk.Combobox(panel,font = fontStyle, width=15,height=2, values=self.jakie_reguly,postcommand=lambda:self.ustaw(),state='readonly')
        self.jakie_reguly_combb.set("Wszystkie")
        self.jakie_reguly_combb.grid(row=1, column=3, sticky=tk.E + tk.W)
        panel.pack(side=tk.BOTTOM, fill=tk.X)

        # Tworzenie dolnego panelu powiadomień
        self.napis1 = tk.Label(panel, bd=1,height=2,font = fontStyle, text="Runda 1", relief=tk.RAISED, bg="lightgrey", fg="black")
        self.napis2 = tk.Label(panel, bd=1,height=2,font = fontStyle, text="Tura gracza X", relief=tk.RAISED, bg="lightgrey", fg="black")
        self.przycisk_reset_set = tk.Button(panel, bd=1,height=2,font = ('Raleway',8), text="Reset\nZatwierdź wybór reguł", relief=tk.RAISED, bg="lightgreen", fg="black",command=lambda:self.reset())

        panel.columnconfigure(0, weight=1)
        panel.columnconfigure(1, weight=1)
        panel.columnconfigure(2, weight=1)
        panel.columnconfigure(3, weight=1)

        self.napis1.grid(row=1, column=0, sticky=tk.E + tk.W)
        self.napis2.grid(row=1, column=1, sticky=tk.E + tk.W)
        self.przycisk_reset_set.grid(row=1, column=2, sticky=tk.E + tk.W)

        # Tworzenie przycisków do wrzucania
        przyciski_wrzut = tk.Frame(self)
        [tk.Button(przyciski_wrzut, text=str(i + 1), width=10, command=partial(self.wrzuc_monete,i+1)).grid(column=i,row=0)for i in range(COLUMNS)]
        for i in range(COLUMNS):
            przyciski_wrzut.columnconfigure(i, weight=1)
        przyciski_wrzut.pack(side=tk.TOP, fill=tk.X)

        self.reset()

    def wyswietlanie_tablicy(self):
        self.plansza = [[None] * COLUMNS for _ in range(ROWS)]
        self.kolka = [[None] * COLUMNS for _ in range(COLUMNS)]
        for i, j in IT.product(range(ROWS), range(COLUMNS)):
            self.L =self.plansza[ROWS - 1 - i][j] =  tk.Canvas(self.canvas, bg="#00BFFF", height=50, width=50, relief="raised",highlightthickness=0)
            padding = 2
            self.id=self.kolka[ROWS - 1 - i][j] = self.L.create_oval((padding, padding, 50 + padding, 50 + padding),fill="lightgrey")
            width = self.L.winfo_reqwidth()
            height = self.L.winfo_reqheight()
            self.L.configure(width=width, height=height)

            self.canvas.rowconfigure(i, weight=1)
            self.canvas.columnconfigure(j, weight=1)
            self.L.grid(row=i, column=j, padx=3, pady=3, sticky=tk.E + tk.W + tk.N + tk.S)



    def wrzuc_monete(self, kolumna):
        padding = 2
        kolor=["lightgrey","#DC143C","#FFD700"]
        try:
            self.game.twoj_ruch(kolumna-1)
        except FullColumn as exept:
            messagebox.showinfo("Błąd!", f"Kolumna {kolumna} jest pełna")
            return
        except MoveOutOfRange as exept:
            messagebox.showinfo("Błąd!", f"Błędny numer kolumny")
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

        self.napis2.config(text="Tura gracza {}".format('red' if self.game.tura == 'X' else 'yellow'))
        self.napis1.config(text="Runda {}".format(self.game.runda))
        gracz=self.game.tura
        if self.game.ktory_gracz_wygral():
            self.napis2.config(text="Koniec gry")
            wygrany='red' if gracz == 'X' else 'yellow'
            messagebox.showinfo("Wygrana!", f"Wygrał gracz {wygrany}")
            return

    def ustaw(self):
        wybor=self.jakie_reguly_combb.get()
        return wybor

    def reset(self):
        self.game = graj(self.ustaw())
        self.game.resetowanie_gry()
        self.napis1.config(text="Runda 1")
        self.napis2.config(text="Tura gracza red")
        self.wyswietlanie_tablicy()
        self.czy_gramy_dalej=True
        print("reset koniec")





app = okienko()
app.update()
app.update_idletasks()
app.mainloop()
