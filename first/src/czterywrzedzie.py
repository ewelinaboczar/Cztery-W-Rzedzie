import tkinter as tk
import numpy as np

ROWS=6
COLUMNS=7

def tworzenie_tablicy():
    tablica=np.zeros((ROWS,COLUMNS))
    return tablica

def wyswietlanie_tablicy(tablica):
    print(np.flip(tablica,0))

def rzuc_monete(tablica,col,row,moneta):
    tablica[row][col] = moneta
    pass

def czy_puste(tablica,col):
    if tablica[ROWS-1][col]==0:
        return True

def ktory_wiersz_pusty(tablica,col):
    for i in range(ROWS):
        if tablica[i][col]==0:
            return i

def czy_wygrana_pion(tablica,moneta):
    for i in range(COLUMNS-3):
        for j in range(ROWS):
            if tablica[i][j] == moneta and tablica[i+3][j]==moneta and tablica[i+2][j]==moneta and tablica[i+1][j] == moneta:
                return True

def czy_wygrana_poziom(tablica,moneta):
    for i in range(COLUMNS):
        for j in range(ROWS-3):
            if tablica[i][j] == moneta and tablica[i][j+3]==moneta and tablica[i][j+2]==moneta and tablica[i][j+1] == moneta:
                return True

def czy_wygrana_skos1(tablica,moneta):
    for i in range(COLUMNS-3):
        for j in range(ROWS-3):
            if tablica[i][j] == moneta and tablica[i+3][j+3]==moneta and tablica[i+2][j+2]==moneta and tablica[i+1][j+1] == moneta:
                return True

def czy_wygrana_skos2(tablica,moneta):
    for i in range(COLUMNS-3):
        for j in range(3,ROWS):
            if tablica[i][j] == moneta and tablica[i-3][j+3]==moneta and tablica[i-2][j+2]==moneta and tablica[i-1][j+1] == moneta:
                return True

def czy_wygrana(tablica,moneta):
    if czy_wygrana_pion(tablica,moneta) or czy_wygrana_poziom(tablica,moneta) or czy_wygrana_skos1(tablica,moneta) or czy_wygrana_skos2(tablica,moneta):
        return True

def graj(tablica):
    czy_koniec=True
    gracz=0
    while(czy_koniec):
        if gracz == 0:
            print("Tura gracza nr 1")
            jaka_kolumna=int(input("Podaj numer kolumny do ktorej chcesz wrzucic monete (0,6): "))
            moneta=1
            if czy_puste(tablica,jaka_kolumna):
                jaki_wiersz=ktory_wiersz_pusty(tablica,jaka_kolumna)
                rzuc_monete(tablica,jaka_kolumna,jaki_wiersz,moneta)
                wyswietlanie_tablicy(tablica)
                if czy_wygrana(tablica,moneta):
                    czy_koniec = False
                    return print("Wygral gracz nr 1")
        else:
            print("Tura gracza nr 2")
            jaka_kolumna = int(input("Podaj numer kolumny do ktorej chcesz wrzucic monete (0,6): "))
            moneta = 2
            if czy_puste(tablica, jaka_kolumna):
                jaki_wiersz = ktory_wiersz_pusty(tablica, jaka_kolumna)
                rzuc_monete(tablica, jaka_kolumna, jaki_wiersz, moneta)
                wyswietlanie_tablicy(tablica)
                if czy_wygrana(tablica,moneta):
                    czy_koniec=False
                    return print("Wygral gracz nr 1")

        gracz+=1
        gracz=gracz%2


tablica=tworzenie_tablicy()
wyswietlanie_tablicy(tablica)
graj(tablica)