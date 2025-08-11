"""
diagram1.png dosyasını dikkate alarak 4 class oluşturalım.
"""

class KaraAraclari:
    ozellik = "KaraAraclari"
    def __init__(self,marka,motor):
        self.marka = marka
        self.motor = motor

    def bilgiver(self):
        print("#"*30)
        print("Marka: ", self.marka)
        print("Motor: ", self.motor)
        print("#"*30)

    @classmethod
    def sinifMethod(cls):
        return cls.ozellik

class KaraAraclari:
    ozellik = "KaraAraclari"
    def __init__(self,marka,motor):
        self.marka = marka
        self.motor = motor

    def bilgiver(self):
        print("#"*30)
        print("Marka: ", self.marka)
        print("Motor: ", self.motor)
        print("#"*30)

    @classmethod
    def sinifMethod(cls):
        return cls.ozellik
#araba1 = Araba("Opel", 1.5)
#araba1.bilgiver()
#araba2 = Araba("Merco", 5.0)
#araba2.bilgiver()
