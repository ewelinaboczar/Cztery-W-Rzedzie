import unittest
from sprawdzanie_wygranej import czy_wygrana_pion, czy_wygrana_poziom, czy_wygrana_skos
from gra import graj, GameException, FullColumn, MoveOutOfRange
ROWS = 6
COLUMNS = 7

class TestGry(unittest.TestCase):
    def setUp(self):
        self.nowa_gra=graj("Wszystkie")

    def test_rzut_moneta(self):
        kol=[1,1,4,3]
        [self.nowa_gra.twoj_ruch(kolumna) for kolumna in kol ]
        self.assertEqual(self.nowa_gra.tablica[0][1], 'X')
        self.assertEqual(self.nowa_gra.tablica[1][1], 'Y')
        self.assertEqual(self.nowa_gra.tablica[0][4], 'X')
        self.assertEqual(self.nowa_gra.tablica[0][3], 'Y')

    def test_czy_wygrana_poziom(self):
        kol=[1,1,2,2,3,3,4]
        [self.nowa_gra.twoj_ruch(kolumna) for kolumna in kol]
        self.assertEqual(self.nowa_gra.zwyciesca,'X')

    def test_czy_wygrana_pion(self):
        kol=[1,2,1,2,1,2,1]
        [self.nowa_gra.twoj_ruch(kolumna) for kolumna in kol]
        self.assertEqual(self.nowa_gra.zwyciesca,'X')

    def test_czy_wygrana_skos(self):
        kol=[1,2,2,3,3,4,3,4,4,2,4]
        [self.nowa_gra.twoj_ruch(kolumna) for kolumna in kol]
        self.assertEqual(self.nowa_gra.zwyciesca, 'X')

    def test_czy_remis(self):
        self.nowa_gra.reguly = ["cztery w poziomie"]
        for w in range(ROWS):
            for i in range(COLUMNS):
                self.nowa_gra.twoj_ruch(i)
        self.assertTrue(self.nowa_gra.czy_remis())

    def test_wygrana_wiecej_niz_4(self):
        kol=[0,0,1,1,2,2,4,4,5,5,6,6,3]
        [self.nowa_gra.twoj_ruch(kolumna) for kolumna in kol]
        self.assertEqual(self.nowa_gra.zwyciesca, 'X')

    def test_zapelniona_kolumna(self):
        for i in range(ROWS):
            self.nowa_gra.twoj_ruch(0)
        self.assertRaises(FullColumn,lambda :self.nowa_gra.twoj_ruch(0))

if __name__ == '__main__':
    unittest.main()
