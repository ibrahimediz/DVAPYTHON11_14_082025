"""
Marka,motor,yıl ve model bilgisinin yer aldığı bir araba sınıf yazalım.
bu sınıf üzerinden 2 araba tanımı yapıp sınıf içerisinde yer alacak olan 
bilgiver fonkisyonunu çalıştırarak arabaya ait olan özellikleri ekrana yazdıralım
"""


class Araba:
    def __init__(self,marka,motor,yıl,model):
        self.marka=marka
        self.motor=motor
        self.yıl=yıl
        self.model=model
    def bilgiver(self):
        print("*" * 30)
        print(f"Marka: {self.marka}")
        print(f"Motor: {self.motor}")
        print(f"Yıl: {self.yıl}")
        print(f"Model: {self.model}")
        print("*" * 30)
car1 = Araba("TOGG","160kW","2024","T10X")
car2 = Araba("Toyota", "1.6L Benzinli", 2020, "Corolla")
car1.bilgiver()
car2.bilgiver()
