import tkinter as tk
import numpy as np
import os
import time

ROWS = 6
COLUMNS = 7

from sprawdzanie_wygranej import czy_wygrana_pion, czy_wygrana_poziom, czy_wygrana_skos

class GameException(Exception):
    pass
class FullColumn(GameException):
    pass
class MoveOutOfRange(GameException):
    pass

class graj(object):
    tura = None
    runda = None
    gracze = ["X","Y"]
    tablica = None
    zwyciesca = None

    def __init__(self, reguly):
        self.runda = 1
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

    def ktory_gracz_wygral(self):
        if self._reguly == "Wszystkie":
            wygrana1 = czy_wygrana_poziom.sprawdz_wygrana(self,tablica=self.tablica)
            wygrana2 = czy_wygrana_pion.sprawdz_wygrana(self,tablica=self.tablica)
            wygrana3 = czy_wygrana_skos.sprawdz_wygrana(self,tablica=self.tablica)
            if wygrana1 != "O":
                return wygrana1
            elif wygrana2 != "O":
                return wygrana1
            elif wygrana3 != "O":
                return wygrana1
        elif self._reguly == "cztery po skosie":
            wygrana1 = czy_wygrana_skos.sprawdz_wygrana(self,tablica=self.tablica)
            if wygrana1 != "O":
                return wygrana1
        elif self._reguly == "cztery w pionie":
            wygrana1 = czy_wygrana_pion.sprawdz_wygrana(self,tablica=self.tablica)
            if wygrana1 != "O":
                return wygrana1
        elif self._reguly == "cztery w poziomie":
            wygrana1 = czy_wygrana_poziom.sprawdz_wygrana(self,tablica=self.tablica)
            if wygrana1 != "O":
                return wygrana1

    def bledny_ruch(self, kolumna):
        if not 0 <= kolumna <= 6:
            raise MoveOutOfRange
        if self.sprawdz_kolumne[kolumna] == 6:
            raise FullColumn
        return True

    def twoj_ruch(self, kolumna):
        if self.zwyciesca:
            return

        self.bledny_ruch(kolumna)
        wiersz=self.sprawdz_kolumne[kolumna]
        self.ruchy.append(kolumna)
        self.tablica[wiersz][kolumna]=self.tura
        self.sprawdz_kolumne[kolumna] += 1

        if self.ktory_gracz_wygral():
            self.zwyciesca = self.tura
            self.resetowanie_gry()
            return

        self.ktory_gracz_gra()

    def drukuj_tablice(self):
        print("\n0 1 2 3 4 5 6")
        print("-- Kolumny --")
        for w in reversed(self.tablica):
            print(" ".join(w))
        print("")

    def ktory_gracz_gra(self):
        self.runda += 1
        self.tura = (self.gracze[0] if self.tura == self.gracze[1] else self.gracze[1])

    def resetowanie_gry(self):
        for i in range(ROWS):
            self.tablica.append(['O'] * 7)
        self.tura=self.gracze[0]
        self.runda=1
        self.zwyciesca=None
        self.ruchy=list()





