import os
import shutil
liste=list(filter(lambda x:not x.endswith(".py"),os.listdir("./Egzersizler")))
liste.append("cevaplar")
liste.remove("diagram1.png")
for item in liste:
    if not os.path.exists(f"./Egzersizler/{item}"):
        os.mkdir(f"./Egzersizler/{item}")
    source = "/workspace/DVAPYTHON11_14_082025/Egzersizler/egzersiz2.py"
    destination = f"/workspace/DVAPYTHON11_14_082025/Egzersizler/{item}/egzersiz2_{item}.py"
    shutil.copy(source,destination)