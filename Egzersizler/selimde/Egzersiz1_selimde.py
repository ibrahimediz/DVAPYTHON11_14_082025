"""
Marka,motor,yıl ve model bilgisinin yer aldığı bir araba sınıf yazalım.
bu sınıf üzerinden 2 araba tanımı yapıp sınıf içerisinde yer alacak olan 
bilgiver fonkisyonunu çalıştırarak arabaya ait olan özellikleri ekrana yazdıralım
"""
#araba class'ı oluşturma
class araba:
    def __init__(self,marka,model,yil,motor): 
        self.marka= marka
        self.model=model
        self.yil=yil
        self.motor=motor
        
    def bilgiverirmisin(self):  #bilgi alma fonksiyonu
        print("marka=", self.marka,"model=",self.model,"yıl=", self.yil,"motor=",self.motor)

araba1=araba("mercedes","e220d",2020,"OM654")
araba2=araba("mercedes","Actros","2012","OM501")

araba1.bilgiverirmisin()


