"""
Marka,motor,yıl ve model bilgisinin yer aldığı bir araba sınıf yazalım.
bu sınıf üzerinden 2 araba tanımı yapıp sınıf içerisinde yer alacak olan 
bilgiver fonkisyonunu çalıştırarak arabaya ait olan özellikleri ekrana yazdıralım
"""

class araba:
    def __init__(self,brand,model,type,engine,hp):
        self.brand= brand
        self.model=model
        self.type=type
        self.engine=engine
        self.hp=hp

        
    def bilgiverirmisin():

