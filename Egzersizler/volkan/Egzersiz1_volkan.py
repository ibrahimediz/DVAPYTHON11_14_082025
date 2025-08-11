"""
Marka,motor,yıl ve model bilgisinin yer aldığı bir araba sınıf yazalım.
bu sınıf üzerinden 2 araba tanımı yapıp sınıf içerisinde yer alacak olan 
bilgiver fonkisyonunu çalıştırarak arabaya ait olan özellikleri ekrana yazdıralım
"""

"""
import os
import shutil
liste=list(filter(lambda x:not x.endswith(".py") ,os.listdir("./Egzersizler")))
liste.append("cevaplar")
for item in liste:
    if not os.path.exists(f"./Egzersizler/{item}"):
        os.mkdir(f"./Egzersizler/{item}")
    source = "/workspace/DVAPYTHON11_14_082025/Egzersizler/Egzersiz1.py"
    destination = f"/workspace/DVAPYTHON11_14_082025/Egzersizler/Egzersiz1_{item}.py"
    shutil.copy(source,destination)
"""
class Araba:
    def __init__(self, marka, motor, yil, model):
        self.marka = marka
        self.motor = motor
        self.yil = yil
        self.model = model

    def bilgiver(self):
        print(f"Marka: {self.marka}")
        print(f"Motor: {self.motor}")
        print(f"Yıl: {self.yil}")
        print(f"Model: {self.model}")
        print("-" * 20)

araba1 = Araba("Toyota", "1.6 Benzin", 2020, "Corolla")
araba2 = Araba("BMW", "2.0 Dizel", 2022, "320i")

araba1.bilgiver()
araba2.bilgiver()
