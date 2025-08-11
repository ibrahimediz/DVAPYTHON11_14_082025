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


class Arac:
    ozellik = "Arac"
    def __init__(self,marka,motor,yıl,modelBilgisi):
        self.marka = marka
        self.motor=motor
        self.yıl=yıl
        self.modelBilgisi=modelBilgisi

    def bilgiver(self):
        print("#"*30)
        print("Arabanın markası: ", self.marka)
        print("Arabanın motoru: ", self.motor)
        print("Arabanın yıl: ", self.yıl)
        print("Arabanın modelBilgisi: ", self.modelBilgisi)


araba1 = Arac("TOGG","200kW",2024,"T10X")
araba2=Arac("VW","1.0TSI",2021,"Polo")

araba1.bilgiver()
araba2.bilgiver()
