"""
diagram1.png dosyasını dikkate alarak 4 class oluşturalım.
"""

class KaraAraci:
    def __init__(self,marka,model,yil):
        self.marka=marka
        self.model=model
        self.yil=yil

def bilgilergoster(self):
    print("Kara aracı marka:", self.marka)
    print("Kara aracı model:",self.model),
    print("KAra aracı yil:",self.yil)

class Araba(KaraAraci):
    def __init__(self,marka,model,yil,kapi_sayisi):
        super().__init__(marka,model,yil)
        self.kapi_sayisi=kapi_sayisi
    def bilgi_goster(self):
        print(f"Arabanın markası:{self.marka}, modeli:{self.model},yılı:{self.yil},kapı sayısı:{self.kapi_sayisi}")

class Kamyonn(KaraAraci):
    def __init__(self,marka,model,yil,hacim):
        super().__init__(marka,model,yil)
        self.hacim=hacim
    def bilgi_goster(self):
        print(f"KAmyonun markası:{self.marka}, modeli:{self.model},yılı:{self.yil},hacmi:{self.hacim}")

class minübüs(KaraAraci):
    def __init__(self,marka,model,yil,kapasite):
        super().__init__(marka,model,yil)
        self.kapasite=kapasite
    def bilgi_goster(self):
         print(f"minübüs markası:{self.marka}, modeli:{self.model},yılı:{self.yil},hacmi:{self.kapasite}")


araba=Araba("kia","3434","2025",5)
araba.bilgi_goster()

kamyon=Kamyonn("xx","model a","2012","buyuk hacim")
kamyon.bilgi_goster()

minu=minübüs(" zz","model x", "2222", "kapasite full")
minu.bilgi_goster()