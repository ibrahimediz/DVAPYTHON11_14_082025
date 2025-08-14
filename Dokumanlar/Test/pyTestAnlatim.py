
def topla(a,b):
    return a+b

def cikar(a,b):
    return a-b

def carp(a,b):
    return a*b

def faktoriyel(a):
    sonuc = 1
    if not a:
        raise ValueError("Değer Hatası")
    for i in range(1,a+1):
        sonuc *= i
    return sonuc

def bol(a,b):
    if b == 0:
        raise ZeroDivisionError("Sıfıra Bölme")
    return a/b


def setUp(function):
        print(function.__name__,"Test Başlıyor")

def tearDown(function):
    print(function.__name__,"Test Bitti")

def test_topla():
    assert topla(3,4) == 7

def test_cikar():
    assert cikar(2,3) == -1

def test_carp():
    assert carp(3,5) == 15

def test_faktoriyel():
    assert faktoriyel(5) == 120

def test_bol():
    assert bol(15,3) == 5.0

def test_faktoriyel_sifir():
    try:
        faktoriyel(0)
        assert False
    except ValueError as e:
        assert str(e) == "Değer Hatası"

def test_bol_sifira():
    try:
        bol(5,0)
        assert False
    except ZeroDivisionError as e:
        assert str(e) == "Sıfıra Bölme"
