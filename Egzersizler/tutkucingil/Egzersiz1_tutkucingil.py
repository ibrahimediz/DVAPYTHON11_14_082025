"""
Marka,motor,yıl ve model bilgisinin yer aldığı bir araba sınıf yazalım.
bu sınıf üzerinden 2 araba tanımı yapıp sınıf içerisinde yer alacak olan 
bilgiver fonkisyonunu çalıştırarak arabaya ait olan özellikleri ekrana yazdıralım
"""

class Araba:
    ozellik = "Otomobil"
    def __init__(self, marka, motor, yil, model):
        self.marka = marka
        self.motor = motor
        self.yil = yil
        self.model = model
        
    def bilgiver(self):
        print("Arabanın markası: ", self.marka)
        print("Arabanın motoru: ", self.motor)
        print("Arabanın üretim yılı: ", self.yil)
        print("Arabanın modeli: ", self.model)
        
    @classmethod
    def sinifMethod(cls):
        return cls.ozellik
    
arac1= Araba("Renault", 1299, 2024, "Megane")
arac2 = Araba ("Audi", 2000, 2027, "A6")

arac1.bilgiver()
