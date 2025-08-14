def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        raise ZeroDivisionError()
    return a / b

def faktoriyel(n):
    if n < 0:
        raise ValueError("Negatif sayılar için faktoriyel tanımsızdır.")
    if n == 0:
        raise ValueError("0 için faktoriyel fonksiyonu bu tanımda geçersizdir.")
    sonuc = 1
    for i in range(1, n + 1):
        sonuc *= i
    return sonuc

import unittest

class TestMathOps(unittest.TestCase):
    def setUp(self):
        print("Test Başlıyor")

    def tearDown(self):
        print("Test Bitti")

    def test_topla(self):
        self.assertEqual(topla(3, 5), 8)
        self.assertEqual(topla(-1, 5), 4)
        self.assertEqual(topla(3, -5), -2)

    def test_cikar(self):
        self.assertEqual(cikar(10, 5), 5)
        self.assertEqual(cikar(-2, -3), 1)
        self.assertEqual(cikar(0, 7), -7)

    def test_carp(self):
        self.assertEqual(carp(3, 4), 12)
        self.assertEqual(carp(-1, 5), -5)
        self.assertEqual(carp(0, 99), 0)

    def test_bol(self):
        self.assertEqual(bol(10, 2), 5)
        self.assertAlmostEqual(bol(7, 3), 2.3333, places=4)

    def test_bol_sifira(self):
        with self.assertRaises(ZeroDivisionError):
            bol(5, 0)

    def test_faktoriyel(self):
        self.assertEqual(faktoriyel(1), 1)
        self.assertEqual(faktoriyel(5), 120)
        self.assertEqual(faktoriyel(3), 6)

    def test_faktoriyel_negatif(self):
        with self.assertRaises(ValueError):
            faktoriyel(-4)

    def test_faktoriyel_sifir(self):
        with self.assertRaises(ValueError):
            faktoriyel(0)

if __name__ == "__main__":
    unittest.main()
