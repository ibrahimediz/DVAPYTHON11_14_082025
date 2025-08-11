"""
Marka,motor,yıl ve model bilgisinin yer aldığı bir araba sınıf yazalım.
bu sınıf üzerinden 2 araba tanımı yapıp sınıf içerisinde yer alacak olan 
bilgiver fonkisyonunu çalıştırarak arabaya ait olan özellikleri ekrana yazdıralım
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
