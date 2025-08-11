"""
diagram1.png dosyasını dikkate alarak 4 class oluşturalım.
"""


class karaAraclari : 

    def __init__(self,tekerSayisi,motor):
        self.tekerSayisi = tekerSayisi
        self.motor = motor
    def soyle (self):
        print ("Kara Araclari")
    def soyleKara (self):
        print("Teker Sayisi:", self.tekerSayisi)
        print("Motor:" ,self.motor)
        print("\n")

objA = karaAraclari(4,2000)
objA.soyleKara()

class araba (karaAraclari):
    def __init__(self, tekerSayisi,motor,vites):
        super().__init__(tekerSayisi,motor)
        self.vites = vites
    def soyleAraba (self):
        print("Teker Sayisi:", self.tekerSayisi)
        print("Motor:" ,self.motor)
        print("vites:",self.vites)
        print("\n")

objB = araba(4,2000,"otomatik")
objB.soyleAraba()

class kamyon (karaAraclari):
    def __init__(self, tekerSayisi,motor,yakit):
        super().__init__(tekerSayisi,motor)
        self.yakit = yakit
    def soyleKamyon (self):
        print("Teker Sayisi:", self.tekerSayisi)
        print("Motor:" ,self.motor)
        print("yakit:",self.yakit)
        print("\n")

objC = kamyon(6,5600,"dizel")
objC.soyleKamyon()

class minibus (karaAraclari):
    def __init__(self, tekerSayisi,motor,kisi):
        super().__init__(tekerSayisi,motor)
        self.kisi = kisi
    def soyleMinibus (self):
        print("Teker Sayisi:", self.tekerSayisi)
        print("Motor:" ,self.motor)
        print("Kisi Sayisi:",self.kisi)
        print("\n")
objD = minibus(4,3000,4)
objD.soyleMinibus()