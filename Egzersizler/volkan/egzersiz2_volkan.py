"""
diagram1.png dosyasını dikkate alarak 4 class oluşturalım.
"""

class KaraAraci:
    def __init__(self,marka,model):
        self.marka = marka
        self.model = model
    def tanim(self):
        print(f"Bu bir kara aracıdır: {self.marka} {self.model} ")

class Araba(KaraAraci):
    def __init__(self,marka,model,motor_hacmi):
        super().__init__(marka,model)
        self.motor_hacmi = motor_hacmi
    def tanim(self):
        print(f"Bu bir araba tipi kara aracidir Araba : {self.marka} {self.model} , Motor Hacmi : {self.motor_hacmi} cc")
        print("-"*20)
class Kamyon(KaraAraci):
     def __init__(self,marka,model,kasa_hacmi):
        super().__init__(marka,model)
        self.kasa_hacmi = kasa_hacmi
     def tanim(self):
        print(f"Bu bir kamyon tipi kara aracidir Kamyon : {self.marka} {self.model} , Kasa Hacmi : {self.kasa_hacmi} Litre")
        print("-"*20)
class Minibus(KaraAraci):
     def __init__(self,marka,model,kapi_sayisi):
        super().__init__(marka,model)
        self.kapi_sayisi = kapi_sayisi
     def tanim(self):
        print(f"Bu bir minibus tipi kara aracidir Minibüs : {self.marka} {self.model} , Kapı Sayısı : {self.kapi_sayisi} Kapılıdır")
        print("-"*20)
araba1 = Araba("BMW",2016,120)
kamyon1 = Kamyon("Mercedes",2022,6000)
minibus1 = Minibus("Wolkswagen",2007,2)

araba1.tanim()
kamyon1.tanim()
minibus1.tanim()