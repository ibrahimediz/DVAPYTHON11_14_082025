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
    def __init__(self, marka, motor ,yıl, model):
        self.__marka=marka
        self.__motor=motor
        self.__yıl=yıl
        self.__model=model

    def yazdır(self):
        print(self.__marka, self.__model, self.__motor, self.__yıl)

a=Car("audi", "a4", 2.0,2023)

a.yazdır()


class araba:
    def __init__(self, marka, model ,yil, motor ):
        self.__marka=marka
        self.__motor=motor
        self.__yil=yil
        self.__model=model

    def bilgiver(self):
        print("*"*30)
        print(self.__marka, self.__model, self.__motor, self.__yil)
        print("*"*30)

araba1=araba("AUDI", "A4", 2.0,2023)
araba2= araba("SEAT", "IBIZA", 1.2, 2015)
araba1.bilgiver()
araba2.bilgiver()