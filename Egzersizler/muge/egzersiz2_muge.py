"""
diagram1.png dosyasını dikkate alarak 4 class oluşturalım.
"""
class kara_araclari:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil
    def bilgi_ver(self):
        print(f"Marka:{self.marka}, Model:{self.model}, Yil:{self.yil}")

class Araba(kara_araclari):
    def __init__(self, marka, model, yil):
        super().__init__(marka, model, yil)
        self.motor = motor
    def bilgi_ver(self):
        super().bilgi_ver
        print(f"Motor:{self.motor}")
class Otobus(kara_araclari):
    def __init__(self, marka, model, yil):
        super().__init__(marka, model, yil)
        self.motor = motor
    def bilgi_ver(self):
        super().bilgi_ver
        print(f"Motor:{self.motor}")
class Minibus(kara_araclari):
    def __init__(self, marka, model, yil):
        super().__init__(marka, model, yil)
        self.motor = motor
    def bilgi_ver(self):
        super().bilgi_ver
        print(f"Motor:{self.motor}")