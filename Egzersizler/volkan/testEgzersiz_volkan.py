"""
def topla(a,b):
    return a+b

def cikar(a,b):
    return a-b

def carp(a,b):
    return a*b

def bol(a,b):
    if b == 0:
        raise ZeroDivisionError()
    return a/b

import unittest
class TestMathOps(unittest.TestCase):
    def setUp(self):
        print("Test Başlıyor")

    def tearDown(self):
        print("Test Bitti")

    def test_topla(self):
        self.assertEqual(topla(3,5),8)
        self.assertEqual(topla(-1,5),4)
        self.assertEqual(topla(3,-5),-2)

    def test_bol_sifira(self):
        with self.assertRaises(ZeroDivisionError):
            bol(5,0)

if __name__ == "__main__":
    unittest.main()
"""


"""
yukarıda yer alan kod bloğu içerisine bir faktoriyel fonksiyonu ekleyin
bu fonksiyon ve kalan diğer fonksiyonlara yönelik test unitleri yazın.
farklı olarak faktoriyel fonksiyonuna 0 parametresi geldiğinde değer hatası verilmesini ve 
bu hatanının kontrolünü de unit olarak ekleyin
"""

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
    if n == 0:
        raise ValueError("0 için faktoriyel hesaplanmaz!")
    if n < 0:
        raise ValueError("Negatif sayılar için faktoriyel tanımsızdır!")
    sonuc = 1
    for i in range(1, n+1):
        sonuc *= i
    return sonuc

import unittest
class TestMathOps(unittest.TestCase):
    def setUp(self):
        print("Test Başlıyor")

    def tearDown(self):
        print("Test Bitti")

    def test_topla(self):
        self.assertEqual(topla(3,5), 8)
        self.assertEqual(topla(-1,5), 4)
        self.assertEqual(topla(3,-5), -2)

    def test_cikar(self):
        self.assertEqual(cikar(10, 3), 7)
        self.assertEqual(cikar(0, 5), -5)

    def test_carp(self):
        self.assertEqual(carp(4, 5), 20)
        self.assertEqual(carp(-2, 3), -6)

    def test_bol(self):
        self.assertEqual(bol(10, 2), 5)
        self.assertAlmostEqual(bol(5, 2), 2.5)

    def test_bol_sifira(self):
        with self.assertRaises(ZeroDivisionError):
            bol(5, 0)

    def test_faktoriyel(self):
        self.assertEqual(faktoriyel(5), 120)
        self.assertEqual(faktoriyel(1), 1)

    def test_faktoriyel_sifir(self):
        with self.assertRaises(ValueError):
            faktoriyel(0)

    def test_faktoriyel_negatif(self):
        with self.assertRaises(ValueError):
            faktoriyel(-3)

if __name__ == "__main__":
    unittest.main()