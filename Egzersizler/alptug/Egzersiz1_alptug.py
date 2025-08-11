"""
Marka,motor,yıl ve model bilgisinin yer aldığı bir araba sınıf yazalım.
bu sınıf üzerinden 2 araba tanımı yapıp sınıf içerisinde yer alacak olan 
bilgiver fonkisyonunu çalıştırarak arabaya ait olan özellikleri ekrana yazdıralım
"""
class Araba:
    ozellik = "Araba"
    def __init__(self,marka,motor, yil, model):
        self.marka = marka
        self.motor = motor
        self.yil = yil
        self.model = model

    def bilgiver(self):
        print("#"*30)
        print("Marka: ", self.marka)
        print("Motor: ", self.motor)
        print("Yil:",self.yil)
        print("Model: ",self.model)
        print("#"*30)

    @classmethod
    def sinifMethod(cls):
        return cls.ozellik

araba1 = Araba("Opel", 1.5, 2012, "Astra")
araba1.bilgiver()
araba2 = Araba("Merco", 5.0, 1997, "S500")
araba2.bilgiver()




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
