"""
diagram1.png dosyasını dikkate alarak 4 class oluşturalım.
"""


class karaAraclari:
    def __init__(self,marka,tekerlekSayisi):
        self.marka = marka
        self.tekerlekSayisi = tekerlekSayisi

class Araba(karaAraclari):
    def __init__(self,marka,tekerlekSayisi,yil):
        super().__init__(marka,tekerlekSayisi)
        self.yil = yil
    


class Kamyon(karaAraclari):
    def __init__(self,marka,tekerlekSayisi,tasimaKapasitesi):
        super().__init__(marka,tekerlekSayisi)
        self.tasimaKapasitesi = tasimaKapasitesi


class Minibus(karaAraclari):
    def __init__(self,marka,tekerlekSayisi,yolcuKapasitesi):
        super().__init__(marka,tekerlekSayisi)
        self.yolcuKapasitesi = yolcuKapasitesi




