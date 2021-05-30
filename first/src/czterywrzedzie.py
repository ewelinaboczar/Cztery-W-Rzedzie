import tkinter as tk
import numpy as np
import os
import time

ROWS=6
COLUMNS=7

class GRA(object):
    tura=None
    runda=None
    gracze=[None,None]
    kolory=["ż","c"]
    tablica=None
    zwyciesca=None
    gracz_skonczyl=None

    def __init__(self):
        self.runda=1
        self.gracz_skonczyl=False
        self.zwyciesca=None

        while self.gracze[0] == None:
            imie=str(input("Graczu 1 podaj swoje imie:"))
            self.gracze[0]=GRACZ(imie,self.kolory[0])
        while self.gracze[1] == None:
            imie=str(input("Graczu 2 podaj swoje imie:"))
            self.gracze[1]=GRACZ(imie,self.kolory[1])
        print("{0} bedzie kolorem {1}".format(self.gracze[0].imie, self.kolory[0]))
        print("{0} bedzie kolorem {1}".format(self.gracze[1].imie, self.kolory[1]))

        self.tura = self.gracze[0]

        self.tablica = []
        for i in range(ROWS):
            self.tablica.append("[]")
            for j in range(COLUMNS):
                self.tablica.append(' ')

    def resetowanie_gry(self):
        self.runda = 1
        self.gracz_skonczyl = False
        self.zwyciesca = None

        self.tura = self.gracze[0]

        self.tablica = []
        for i in range(ROWS):
            self.tablica.append("[]")
            for j in range(COLUMNS):
                self.tablica.append(' ')

    def ktory_gracz_gra(self):
        if self.tura == self.gracze[0]:
            print("Tura gracza 1")
            self.tura = self.gracze[1]
        else:
            print("Tura gracza 2")
            self.tura == self.gracze[0]
        self.runda += 1

    def twoj_ruch(self):
        if self.runda>42:
            self.gracz_skonczyl=True
            return

        jaki_ruch = GRACZ.czy_puste(self.tablica)

        for i in range(ROWS):
            if self.tablica[i][jaki_ruch] == ' ':
                self.tablica[i][jaki_ruch] = GRACZ.kolor
                self.ktory_gracz_gra()
                self.czy_wygrana()
                self.drukuj_tablice()
                return

        print("Kolumna jest pelna")
        return

    def drukuj_tablice(self):
        os.system(['clear','cls'][os.name == 'nt'])
        print("Runda: "+str(self.runda))

        for i in range(5,-1,-1):
            print("\t",end="")
            for j in range(6):
                print("| "+str(self.tablica[i][j])+" ")
            print("|")
            print("\t _ _ _ _ _ _ _")
            print("\t 1 2 3 4 5 6 7")

            if self.gracz_skonczyl:
                print("Koniec gry!")
                if self.zwyciesca != None:
                    print("Gratulacje "+str(self.zwyciesca.imie)+" zwyciężył!")
                else:
                    print("Tablica zostala narysowana")


    def czy_wygrana_pion(self):
        for i in range(COLUMNS):
            for j in range(ROWS - 3):
                if self.tablica[j][i] == GRACZ.kolor and self.tablica[j + 1][i] == GRACZ.kolor and self.tablica[j + 2][i] == GRACZ.kolor and self.tablica[j + 3][i] == GRACZ.kolor:
                    return True

    def czy_wygrana_poziom(self):
        for i in range(COLUMNS - 3):
            for j in range(ROWS):
                if self.tablica[j][i] == GRACZ.kolor and self.tablica[j][i + 1] == GRACZ.kolor and self.tablica[j][i + 2] == GRACZ.kolor and self.tablica[j][i + 3] == GRACZ.kolor:
                    return True

    def czy_wygrana_skos1(self):
        for i in range(COLUMNS - 3):
            for j in range(ROWS - 3):
                if self.tablica[j][i] == GRACZ.kolor and self.tablica[j + 1][i + 1] == GRACZ.kolor and self.tablica[j + 2][i + 2] == GRACZ.kolor and self.tablica[j + 3][i + 3] == GRACZ.kolor:
                    return True

    def czy_wygrana_skos2(self):
        for i in range(COLUMNS - 3):
            for j in range(3, ROWS):
                if self.tablica[j][i] == GRACZ.kolor and self.tablica[j - 1][i + 1] == GRACZ.kolor and self.tablica[j - 2][i + 2] == GRACZ.kolor and self.tablica[j - 3][i + 3] == GRACZ.kolor:
                    return True

    def czy_wygrana(self):
        if czy_wygrana_pion() or czy_wygrana_poziom() or czy_wygrana_skos1() or czy_wygrana_skos2():
            self.gracz_skonczyl=True
            return



class GRACZ(object):
    imie=None
    kolor=None

    def __init__(self,imie,kolor):
        self.imie=imie
        self.kolor=kolor

    def czy_puste(self, state):
        kolumna=None
        while kolumna == None:
            try:
                wybor=int(input("Wybierz kolumne (1-7):"))-1
            except ValueError:
                wybor = None
            if wybor >= 0 and wybor <=6:
                kolumna=wybor
            else:
                print("Podales bledna kolumne, sprobuj jeszcze raz")
        return kolumna


def main():
    gra=GRA()
    gra.drukuj_tablice()
    gracz1=gra.gracze[0]
    gracz2=gra.gracze[1]

    tabela_zwyciestw=[0,0,0]

    while not koniec_gry:
        while not gra.gracz_skonczyl:
            gra.twoj_ruch()
        gra.drukuj_tablice()

        if gra.zwyciesca == None:
            tabela_zwyciestw[2] += 1
        if gra.zwyciesca == gracz1:
            tabela_zwyciestw[0] += 1
        if gra.zwyciesca == gracz2:
            tabela_zwyciestw[1] += 1

        drukuj_tabele_zwyciestw(gracz1,gracz2,tabela_zwyciestw)

def drukuj_tabele_zwyciestw(gracz1,gracz2,tabela_zwyciestw):
    print("{0}: {1} wygranych, {2}: {3} wygranych, {4}-> remisow".format(gracz1.imie,tabela_zwyciestw[0],gracz2.imie,tabela_zwyciestw[1],tabela_zwyciestw[2]))

main()
