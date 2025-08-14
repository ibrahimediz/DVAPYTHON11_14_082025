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

def faktoriyel(n):
    if n== 1:
        return 1
    if n==0:
   
        return "ValueError not raised"
    else:
        return n * faktoriyel(n-1)



import unittest
class TestMathOps(unittest.TestCase):
    def setUp(self):
        print("Test Başlıyor")

    def tearDown(self):
        print("Test Bitti")
           
    def test_faktoriyel(self):
        self.assertEqual(faktoriyel(0),"ValueError not raised")
       
    def test_faktoriyel(self):
        self.assertEqual(faktoriyel(5),120)
    # def sifir_deger(self):
    #     with self.assertRaises(ZeroDivisionError):
    #         bol(0,1)
    # # def test_bol_sifira(self):
    # #     with self.assertRaises(ZeroDivisionError):
    # #         bol(5,0)

if __name__ == "__main__":
    unittest.main()





"""
yukarıda yer alan kod bloğu içerisine bir faktoriyel fonksiyonu ekleyin
bu fonksiyon ve kalan diğer fonksiyonlara yönelik test unitleri yazın.
farklı olarak faktoriyel fonksiyonuna 0 parametresi geldiğinde değer hatası verilmesini ve 
bu hatanının kontrolünü de unit olarak ekleyin
"""