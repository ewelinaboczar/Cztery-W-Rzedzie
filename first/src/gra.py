import tkinter as tk
import numpy as np
import os
import time

ROWS = 6
COLUMNS = 7

from sprawdzanie_wygranej import czy_wygrana_pion, czy_wygrana_poziom, czy_wygrana_skos     #importowanie regul

class GameException(Exception):
    pass
class FullColumn(GameException):                                                            #wyjatek czy kolumna pelna
    pass
class MoveOutOfRange(GameException):                                                        #wyjatek czy ruch poza zakresem
    pass

class graj(object):
    tura = None                                                                             #zmienna tura pokazuje jaki gracz ma ruch
    runda = None                                                                            #zmienna runda pokazuje numer rundy
    gracze = ["X","Y"]                                                                      #tablica graczy
    tablica = None                                                                          #tablica rekordow rzutow
    zwyciesca = None                                                                        #zmienna zwyciesca pokazuje wygranego gracza

    def __init__(self, reguly):
        self.runda = 1
        self.zwyciesca = None
        self.tura = self.gracze[0]
        self.sprawdz_kolumne = [0] * 7
        self.remis=None
        self._reguly = reguly
        self.tablica = list()
        for i in range(ROWS):                                                               #wypelnianie tablicy 'O'
            self.tablica.append(['O'] * 7)

    @property
    def reguly(self):
        return self._reguly

    @reguly.setter
    def reguly(self, nowa_regula):                                                          #pobieranie nowych regul
        self._reguly = nowa_regula

    def ktory_gracz_wygral(self):                                                           #metoda sprawdzajaca wygrana
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

    def czy_remis(self):                                                                    #metoda sprawdzajaca czy jest remis
        for i in range(ROWS):
            for j in range(COLUMNS):
                if self.tablica[i][j] == 'O':
                    return False
        return True

    def bledny_ruch(self, kolumna):                                                         #metoda pilnujaca zeby nie wystapily wyjatki
        if not 0 <= kolumna <= 6:
            raise MoveOutOfRange
        if self.sprawdz_kolumne[kolumna] == 6:
            raise FullColumn
        return True

    def twoj_ruch(self, kolumna):                                                           #metoda ustawiajaca monete w odpowiednim miejscu
        if self.zwyciesca:                                                                  #srawdzanie czy jest juz zwyciesca
            return

        self.bledny_ruch(kolumna)                                                           #sprawdzanie wyjatkow
        wiersz=self.sprawdz_kolumne[kolumna]
        self.tablica[wiersz][kolumna]=self.tura
        self.sprawdz_kolumne[kolumna] += 1

        if self.ktory_gracz_wygral():                                                       #sprawdzanie wygranej
            self.zwyciesca = self.tura

        self.ktory_gracz_gra()                                                              #zmiana gracza na gracza kolejnego

    def drukuj_tablice(self):                                                               #metoda wyswietlajaca tablice
        print("\n0 1 2 3 4 5 6")
        print("-- Kolumny --")
        for w in reversed(self.tablica):
            print(" ".join(w))
        print("")

    def ktory_gracz_gra(self):                                                              #metoda zmieniajaca aktualnego gracza
        self.runda += 1                                                                     #inkrementacja rundy
        self.tura = (self.gracze[0] if self.tura == self.gracze[1] else self.gracze[1])

    def resetowanie_gry(self):                                                              #metoda resetujaca plansze i inne zmienne
        for i in range(ROWS):
            self.tablica.append(['O'] * 7)
        self.tura=self.gracze[0]
        self.runda=1
        self.zwyciesca=None







