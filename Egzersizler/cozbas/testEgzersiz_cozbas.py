def topla(a,b):
    return a+b

def cikar(a,b):
    return a-b

def carp(a,b):
    return a*b
def faktoriyel(a):
    sonuc=1
    if not a: 
        return ValueError
    else:
        if a<2:
            return 1
        else:
            return a*faktoriyel(a-1)
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
    print(str(faktoriyel()))
    unittest.main()


    
"""
yukarıda yer alan kod bloğu içerisine bir faktoriyel fonksiyonu ekleyin
bu fonksiyon ve kalan diğer fonksiyonlara yönelik test unitleri yazın.
farklı olarak faktoriyel fonksiyonuna 0 parametresi geldiğinde değer hatası verilmesini ve 
bu hatanının kontrolünü de unit olarak ekleyin
"""