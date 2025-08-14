# def topla(a,b):
#     return a+b

# def cikar(a,b):
#     return a-b

# def carp(a,b):
#     return a*b

# def bol(a,b):
#     if b == 0:
#         raise ZeroDivisionError()
#     return a/b

# import unittest
# class TestMathOps(unittest.TestCase):
#     def setUp(self):
#         print("Test Başlıyor")

#     def tearDown(self):
#         print("Test Bitti")

#     def test_topla(self):
#         self.assertEqual(topla(3,5),8)
#         self.assertEqual(topla(-1,5),4)
#         self.assertEqual(topla(3,-5),-2)

#     def test_bol_sifira(self):
#         with self.assertRaises(ZeroDivisionError):
#             bol(5,0)

# if __name__ == "__main__":
#     unittest.main()



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
        raise ValueError("0 için faktoriyel hesaplanamaz.")
    sonuc = 1
    for i in range(1, n + 1):
        sonuc *= i
    return sonuc


import unittest
import pytest

def setUp(function):
    print(function.__name__,"Test Başlıyor")

def tearDown(function):
    print(function.__name__,"Test Bitti")

def test_topla():
    assert topla(3, 5) == 8
    

def test_cikar():
    assert cikar(10, 5) == 5


def test_carp():
    assert carp(3, 4) == 12
    
def test_bol():
    assert bol(10, 2) == 5
    

if __name__ == "__main__":
    unittest.main()
