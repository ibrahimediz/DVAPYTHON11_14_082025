"""
Marka,motor,yıl ve model bilgisinin yer aldığı bir araba sınıf yazalım.
bu sınıf üzerinden 2 araba tanımı yapıp sınıf içerisinde yer alacak olan 
bilgiver fonkisyonunu çalıştırarak arabaya ait olan özellikleri ekrana yazdıralım
"""

class arac:

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
arac1 = arac("Ford","1.5 TDCI","2018","Focus")
arac2 = arac("VW","1.5 TSI","2022","Golf")
arac1.bilgiver()
arac2.bilgiver()

