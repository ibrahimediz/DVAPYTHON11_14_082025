"""
diagram1.png dosyasını dikkate alarak 4 class oluşturalım.
"""

class karaAraclari:
    def __init__(self, isim, yakittipi, tekerleksayisi, motor):
        self.isim = isim
        self.yakittipi = yakittipi
        self.tekerleksayisi = tekerleksayisi
        self.motor = motor

    def yakitAl(self):
        self.yakitDurum = True if not self.yakitDurum else False
        print(self.isim,"Yakıt Aldı")

    def bilgiver(self):
        print(self.isim)
        """
        diğerleri yazılabilir
        """

class Araba(karaAraclari):
    def __init__(self, isim, yakittipi, tekerleksayisi, motor, kapisayisi):
        super().__init__(isim, yakittipi, tekerleksayisi, motor)
        self.kapi_sayisi = kapi_sayisi

    def bilgiver(self):
        super().bilgiver()
        print(self.kapi_sayisi)

class Kamyon(karaAraclari):
    def __init__(self, isim, yakittipi, tekerleksayisi, motor, tonaj):
        super().__init__(isim, yakittipi, tekerleksayisi, motor)
        self.tonaj = tonaj

    def bilgiver(self):
        super().bilgiver()
        print(self.tonaj)
