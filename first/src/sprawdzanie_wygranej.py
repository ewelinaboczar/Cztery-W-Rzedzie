ROWS = 6
COLUMNS = 7

class regula:
    def sprawdz_wygrana(self,tablica):
        pass

class czy_wygrana_pion(regula):
    def sprawdz_wygrana(self,tablica):
        for i in range(COLUMNS):
            aktualny = None
            for j in range(ROWS - 3):
                if tablica[j][i] != 'O':
                    aktualny = tablica[j][i]
                    if tablica[j][i] == aktualny and tablica[j + 1][i] == aktualny and tablica[j + 2][i] == aktualny and tablica[j + 3][i] == aktualny:
                        return tablica[j][i]
                else:
                    aktualny=0
        return "O"
    def __str__(self):
        return "cztery w pionie"

class czy_wygrana_poziom(regula):
    def sprawdz_wygrana(self, tablica):
        for i in range(COLUMNS - 3):
            aktualny = None
            for j in range(ROWS):
                if tablica[j][i] != 'O':
                    aktualny = tablica[j][i]
                    if tablica[j][i] == aktualny and tablica[j][i + 1] == aktualny and tablica[j][i + 2] == aktualny and tablica[j][i + 3] == aktualny:
                        return tablica[j][i]
                else:
                    aktualny=0
        return "O"
    def __str__(self):
        return "cztery w poziomie"

class czy_wygrana_skos(regula):
    def sprawdz_wygrana(self,tablica):
        for i in range(COLUMNS - 3):
            aktualny1 = None
            for j in range(ROWS - 3):
                if tablica[j][i] != 'O':
                    aktualny1 = tablica[j][i]
                    if tablica[j][i] == aktualny1 and tablica[j + 1][i + 1] == aktualny1 and tablica[j + 2][i + 2] == aktualny1 and tablica[j + 3][i + 3] == aktualny1:
                        return tablica[j][i]
                else:
                    aktualny1=0


        for i in range(COLUMNS - 3):
            aktuany2 = None
            for j in range(3, ROWS):
                if tablica[j][i] != 'O':
                    aktualny2 = tablica[j][i]
                    if tablica[j][i] == aktualny2 and tablica[j - 1][i + 1] == aktualny2 and tablica[j - 2][i + 2] == aktualny2 and tablica[j - 3][i + 3] == aktualny2:
                        return tablica[j][i]
                else:
                    aktualny2 = 0
        return "O"
    def __str__(self):
        return "cztery po skosie"