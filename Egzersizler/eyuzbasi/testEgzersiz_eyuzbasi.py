from factorial import factorial

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

def faktoriyel(a):
    sonuc = 1
    if not a:
        raise ValueError()
    for i in range(1,a+1):
        sonuc *= i
    return sonuc

import unittest

class TestMathOps(unittest.TestCase):
    def setUp(self):
        print("Test Başlıyor")

    def tearDown(self):
        print("Test Bitti")

    def test_topla(self):
        assert bol(15,3) == 5.0

    def test_bol(self):
        assert bol(15,3) == 5.0

    def test_factorial(self):
        self.assertEqual(factorial(3),6)
        self.assertEqual(factorial(6),720)

    def test_sıfırFactorial(self):
        with self.assertRaises(ValueError):
          factorial(0)

if __name__ == "__main__":
    unittest.main()



"""
yukarıda yer alan kod bloğu içerisine bir faktoriyel fonksiyonu ekleyin
bu fonksiyon ve kalan diğer fonksiyonlara yönelik test unitleri yazın.
farklı olarak faktoriyel fonksiyonuna 0 parametresi geldiğinde değer hatası verilmesini ve 
bu hatanının kontrolünü de unit olarak ekleyin
"""