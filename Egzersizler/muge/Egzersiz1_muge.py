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


class Araba:
    def __init__(self,marka,model,motor,yil):
        self.marka = marka
        self.model = model
        self.motor = motor
        self.yil = yil
    
    def bilgi_ver(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Motor: {self.motor}")
        print(f"Yil: {self.yil}")

araba1 = Araba("Opel","Corsa","1.4","2000")
araba2 = Araba("","","","")

araba1.bilgi_ver()
araba2.bilgi_ver()