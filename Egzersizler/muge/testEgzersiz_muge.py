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
yukarıda yer alan kod bloğu içerisine bir faktoriyel fonksiyonu ekleyin
bu fonksiyon ve kalan diğer fonksiyonlara yönelik test unitleri yazın.
farklı olarak faktoriyel fonksiyonuna 0 parametresi geldiğinde değer hatası verilmesini ve 
bu hatanının kontrolünü de unit olarak ekleyin
"""

import math

def faktoriyel(n):
    return math.factorial(n)

class TestFaktoriyel(unittest.TestCase):
    def test_sifir(self):
        self.assertEqual(faktoriyel(0),1)
    def test_bir(self):
        self.assertEqual(faktoriyel(1),1)
    def test_pozitif(self):
        self.assertEqual(faktoriyel(5),120)
    def test_buyuk_sayi(self):
        self.assertEqual(faktoriyel(10),3628800)
    def test_negatif(self):
        with self.assertRaises(ValueError):
            faktoriyel(-3)
if __name__ == "__main__":
    unittest.main()