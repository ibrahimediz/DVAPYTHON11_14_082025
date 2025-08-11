"""
Marka,motor,yıl ve model bilgisinin yer aldığı bir araba sınıf yazalım.
bu sınıf üzerinden 2 araba tanımı yapıp sınıf içerisinde yer alacak olan 
bilgiver fonkisyonunu çalıştırarak arabaya ait olan özellikleri ekrana yazdıralım
"""

class Araba:
    def __init__(self,marka,motor,yil,model):
        self.marka = marka
        self.motor = motor
        self.yil = yil
        self.model = model

    def bilgiver(self):
        print("#"*30)
        print(self.marka)
        print(self.motor)
        print(self.yil)
        print(self.model)
        print("#"*30)

Araba1 = Araba("TOGG","200kW",2024,"T10X")
Araba2 = Araba("Mercedes","1.6","2024","A180")
Araba1.bilgiver()
Araba2.bilgiver()

