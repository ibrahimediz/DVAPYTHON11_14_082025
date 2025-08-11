"""
Marka,motor,yıl ve model bilgisinin yer aldığı bir araba sınıf yazalım.
bu sınıf üzerinden 2 araba tanımı yapıp sınıf içerisinde yer alacak olan 
bilgiver fonkisyonunu çalıştırarak arabaya ait olan özellikleri ekrana yazdıralım
"""

#####################class çalışması##########################
class Araba:
    def __init__(self,marka,motor,yil,model):
        self.marka = marka
        self.motor = motor
        self.yil = yil
        self.model = model
    
    def bilgiver(self):
        print("#"*30)
        print("Otomobilin markası: ", self.marka)
        print("Otomobilin motoru: ", self.motor)
        print("Otomobilin yili: ", self.yil)
        print("Otomobilin modeliı: ", self.model)
        
araba1 = Araba("TOGG", "200KW",2024,"T10X")
araba2 = Araba("Alfa Romeo", "200HP",2025, "Stelvio")
araba1.bilgiver()
araba2.bilgiver()

