"""
diagram1.png dosyasını dikkate alarak 4 class oluşturalım.
"""

class KaraAraclari:
    def __init__(self,tekerlek_sayisi,motor,yil,model):
        self.tekerlek_sayisi = tekerlek_sayisi
        self.motor = motor
        self.yil = yil
        self.model = model
    def bilgiler(self):
        print(self.tekerlek_sayisi)
        print(self.motor)
        print(self.yil)
        print(self.model)

class Araba(KaraAraclari):
    def __init__(self,tekerlek_sayisi,motor,yil,model,kapi_sayisi):
        KaraAraclari.__init__(self,tekerlek_sayisi,motor,yil,model) 
        self.kapi_sayisi = kapi_sayisi
    def bilgiler_Araba(self):
        KaraAraclari.bilgiler(self)
        print(self.kapi_sayisi)

class Kamyon(KaraAraclari):
    def __init__(self,tekerlek_sayisi,motor,yil,model,tonaj):
        KaraAraclari.__init__(self,tekerlek_sayisi,motor,yil,model) 
        self.tonaj = tonaj
    def bilgiler_Kamyon(self):
        KaraAraclari.bilgiler(self)
        print(self.tonaj) 

class Minibüs(KaraAraclari):
    def __init__(self,tekerlek_sayisi,motor,yil,model,kisi_sayisi):
        KaraAraclari.__init__(self,tekerlek_sayisi,motor,yil,model) 
        self.kisi_sayisi = kisi_sayisi
    def bilgiler_Minibüs(self):
        KaraAraclari.bilgiler(self)
        print(self.kisi_sayisi) 

A=Araba(4,1.6,2024,"A180",4)
B=Kamyon(5,2,2005,"MAN",5)
A.bilgiler_Araba()
B.bilgiler_Kamyon()