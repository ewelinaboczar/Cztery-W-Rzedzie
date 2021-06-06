import tkinter as tk
import numpy as np
import os
import time

ROWS = 6
COLUMNS = 7


class GameException(Exception):
    pass


class FullColumn(GameException):
    pass


class MoveOutOfRange(GameException):
    pass


class graj(object):
    tura = None
    runda = None
    gracze = ["X", "Y"]
    tablica = None
    zwyciesca = None
    gracz_skonczyl = None

    def __init__(self, reguly):
        self.runda = 1
        self.gracz_skonczyl = False
        self.zwyciesca = None
        self.ruchy = list()
        self.tura = self.gracze[0]
        self.sprawdz_kolumne = [0] * 7
        self._reguly = reguly

        self.tablica = list()
        for i in range(ROWS):
            self.tablica.append(['O'] * 7)

    @property
    def reguly(self):
        return self._reguly

    @reguly.setter
    def reguly(self, nowa_regula):
        self._reguly = nowa_regula

    def ktory_gracz_wygral(self, wiersz, kolumna):
        print(reguly)
        for i in self._reguly:
            wygrana = sprawdzanie_wygranej.sprawdz_wygrana(tablica=self.tablica)
            if wygrana is not None:
                return True
            else:
                return False

    def bledny_ruch(self, kolumna):  # zrobione#
        if not 0 <= kolumna <= 6:
            raise MoveOutOfRange
        if self.sprawdz_kolumne[kolumna] == 6:
            raise FullColumn
        return True

    def twoj_ruch(self, kolumna):
        if self.zwyciesca:
            return

        self.bledny_ruch(kolumna)

        wiersz = self.sprawdz_kolumne[kolumna]

        self.ruchy.append(kolumna)
        self.tablica[wiersz][kolumna] = self.tura
        self.sprawdz_kolumne[kolumna] += 1

        if self.ktory_gracz_wygral(wiersz, kolumna):
            self.zwyciesca = self.tura
            return

        if self.runda >= 42:
            self.gracz_skonczyl = True
            self.zwyciesca = 'N'

        self.ktory_gracz_gra()
        self.tablica[wiersz][kolumna] = numer

    def drukuj_tablice(self):  # zrobione#
        os.system(['clear', 'cls'][os.name == 'nt'])

        print("\n0 1 2 3 4 5 6")
        print("-- Kolumny --")
        for w in reversed(self.tablica):
            print(" ".join(w))
        print("")

    def ktory_gracz_gra(self):  # zrobione#
        if self.tura == self.gracze[0]:
            print("Tura gracza 1")
            self.tura = self.gracze[1]
        else:
            print("Tura gracza 2")
            self.tura == self.gracze[0]
        self.runda += 1


