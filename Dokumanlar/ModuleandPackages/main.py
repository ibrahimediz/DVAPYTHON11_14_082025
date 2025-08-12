"""
main dosyası
"""

# print(__name__) #__main__

###########################
# import os
# print(os.getcwd())
# # import pandas as pd
# from os import getcwd,sep,path
# print(getcwd())
# print(sep)
#######################
# liste = ["Egzersizler","Cevaplar"]
# import os
# print(os.sep.join(liste))
#########################3
# from pathlib import Path
# yol = Path("Egzersizler")
# yol = yol / "cevaplar"
# print(yol)

# print(__doc__)



# import sys
# print(*sys.path,sep="\n")

import paket1

# import paket1.modul1 
from paket1 import modul1 as md1
from paket1.modul1 import modulFonk as mf1,ModulClass as mdC1
