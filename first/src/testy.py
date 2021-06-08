import unittest
from sprawdzanie_wygranej import czy_wygrana_pion, czy_wygrana_poziom, czy_wygrana_skos
from gra import graj, GameException, FullColumn, MoveOutOfRange
ROWS = 6
COLUMNS = 7

class TestGry(unittest.TestCase):
    def setUp(self):
        self.nowa_gra=graj("Wszystkie")

    def test_rzut_moneta(self):                                     #Wykonanie po dwa ruchy przez każdego z graczy –
        kol=[1,1,4,3]                                               #monety spadają na dół pola gry lub zatrzymują
        [self.nowa_gra.twoj_ruch(kolumna) for kolumna in kol ]      #się na już wrzuconym żetonie
        self.assertEqual(self.nowa_gra.tablica[0][1], 'X')
        self.assertEqual(self.nowa_gra.tablica[1][1], 'Y')
        self.assertEqual(self.nowa_gra.tablica[0][4], 'X')
        self.assertEqual(self.nowa_gra.tablica[0][3], 'Y')

    def test_czy_wygrana_poziom(self):                              #Ułożenie poziomej linii monet przez jednego gracza -
        kol=[1,1,2,2,3,3,4]                                         #oczekiwana informacja o jego wygranej
        [self.nowa_gra.twoj_ruch(kolumna) for kolumna in kol]
        self.assertEqual(self.nowa_gra.zwyciesca,'X')

    def test_czy_wygrana_pion(self):                                #Ułożenie pionowej linii monet przez jednego gracza -
        kol=[1,2,1,2,1,2,1]                                         #oczekiwana informacja o jego wygranej
        [self.nowa_gra.twoj_ruch(kolumna) for kolumna in kol]
        self.assertEqual(self.nowa_gra.zwyciesca,'X')

    def test_czy_wygrana_skos(self):                                #Ułożenie skośnej linii monet przez jednego gracza -
        kol=[1,2,2,3,3,4,3,4,4,2,4]                                 #oczekiwana informacja o jego wygranej
        [self.nowa_gra.twoj_ruch(kolumna) for kolumna in kol]
        self.assertEqual(self.nowa_gra.zwyciesca, 'X')

    def test_czy_remis(self):                                       #zapełnienie pola gry tak że jeden gracz nie ułożył linii -
        self.nowa_gra.reguly = ["cztery w poziomie"]                #zekiwana informacja o remisie
        for w in range(ROWS):
            for i in range(COLUMNS):
                self.nowa_gra.twoj_ruch(i)
        self.assertTrue(self.nowa_gra.czy_remis())

    def test_wygrana_wiecej_niz_4(self):                            #Ułożenie linii dłuższej niż 4 przez jednego z graczy -
        kol=[0,0,1,1,2,2,4,4,5,5,6,6,3]                             #oczekiwana informacja o jego wygranej
        [self.nowa_gra.twoj_ruch(kolumna) for kolumna in kol]
        self.assertEqual(self.nowa_gra.zwyciesca, 'X')

    def test_zapelniona_kolumna(self):                              #próba wrzucenia monety do zapełnionej kolumny -
        for i in range(ROWS):                                       #oczekiwana informacja o błędzie
            self.nowa_gra.twoj_ruch(0)
        self.assertRaises(FullColumn,lambda :self.nowa_gra.twoj_ruch(0))

if __name__ == '__main__':
    unittest.main()
