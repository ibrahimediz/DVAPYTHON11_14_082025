"""
diagram1.png dosyasını dikkate alarak 4 class oluşturalım.
"""

class KaraAraclari:
    def __init__(self,marka,motor,yil,model):
        self.marka = marka
        self.motor = motor
        self.yil = yil
        self.model = model


    def bilgiver(self):
        print("Marka: " ,self.marka)
        print("Model: " ,self.model)
        print("Motor: " ,self.motor)
        print("Yıl: " ,self.yil)

class Araba(KaraAraclari):


class Kamyon(KaraAraclari):


class Minibus(KaraAraclari):
