"""
diagram1.png dosyasını dikkate alarak 4 class oluşturalım.
"""

class KaraAraclari:
    ozellik = "KaraAraclari"
    def __init__(self,yakittipi,tekerleksayisi,motor):
        self.yakittipi = yakittipi
        self.tekerleksayisi = tekerleksayisi
        self.motor = motor
        self.isim = isim
        self.yakitDurum = True

    def yakitAl(self):
        self.yakitDurum = True if not self.yakitDurum else False
        print(self.isim, "Yakit aldı")
    def bilgiver(self):
        print(self.isim)
        """
        diğerleri yazılabilir.
        """
class Araba(KaraAraclari):
    def __init__(self, isim,yakittipi, tekerleksayisi, motor, kapisayisi):
        super().__init__(isim,yakittipi,tekerleksayisi,motor)
        self.kapisayisi = kapisayisi
    def bilgiver(self):
        super().bilgiver()
        print(self.kapisayisi)