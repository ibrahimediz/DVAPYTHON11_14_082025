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
    fact=1
    if a==0:
        raise ValueError()
    
    for i in range(1, a+1):
        fact = fact * i
    return fact
    

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

    def test_faktoriyel(self):
        self.assertEqual(faktoriyel(3),6)
        self.assertEqual(faktoriyel(5),120)
        self.assertEqual(faktoriyel(1),1)

    def test_sifir_faktoriyel(self):
        with self.assertRaises(ZeroDivisionError):
            faktoriyel(0)

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