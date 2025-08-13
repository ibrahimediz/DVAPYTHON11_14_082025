import os
import shutil
liste=list(filter(lambda x:not x.endswith(".py"),os.listdir("./Egzersizler")))
liste.append("cevaplar")
liste.remove("diagram1.png")
liste.remove("datasets")
liste.remove("EgzersizPandas.ipynb")
for item in liste:
    if not os.path.exists(f"./Egzersizler/{item}"):
        os.mkdir(f"./Egzersizler/{item}")
    source = "/workspace/DVAPYTHON11_14_082025/Egzersizler/EgzersizPandas.ipynb"
    destination = f"/workspace/DVAPYTHON11_14_082025/Egzersizler/{item}/EgzersizPandas_{item}.ipynb"
    if not os.path.exists(f"/workspace/DVAPYTHON11_14_082025/Egzersizler/{item}/EgzersizPandas_{item}.ipynb"):
        shutil.copy(source,destination)