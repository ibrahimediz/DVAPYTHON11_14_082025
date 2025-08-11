"""
Marka,motor,yıl ve model bilgisinin yer aldığı bir araba sınıf yazalım.
bu sınıf üzerinden 2 araba tanımı yapıp sınıf içerisinde yer alacak olan 
bilgiver fonkisyonunu çalıştırarak arabaya ait olan özellikleri ekrana yazdıralım
"""


# import os
# import shutil
# liste=list(filter(lambda x:not x.endswith(".py") ,os.listdir("./Egzersizler")))
# liste.append("cevaplar")
# for item in liste:
#     if not os.path.exists(f"./Egzersizler/{item}"):
#         os.mkdir(f"./Egzersizler/{item}")
#     source = "/workspace/DVAPYTHON11_14_082025/Egzersizler/Egzersiz1.py"
#     destination = f"/workspace/DVAPYTHON11_14_082025/Egzersizler/Egzersiz1_{item}.py"
#     shutil.copy(source,destination)


class Car:
    def __init__(self, marka, motor, yıl, model):
        self.marka = marka
        self.motor = motor
        self.yıl = yıl
        self.model = model

    def bilgiver(self):
        print(self.marka)
        print(self.motor)
        print(self.yil)
        print(self.model)

car1 = Car("BMW","2.0","2024","520i")
car2 = Araba("Mercedes","1.6","2020","A180")
car1.bilgiver()
car2.bilgiver()

