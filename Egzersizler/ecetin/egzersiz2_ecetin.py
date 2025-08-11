"""
diagram1.png dosyasını dikkate alarak 4 class oluşturalım.
"""

class KaraAraclari:
    def __init__(self, sinif, aks, maksHiz, marka):
        self.sinif = sinif
        self.aks = aks
        self.maksHiz = maksHiz
        self.marka = marka
    def bilgiler(self):
        print(self.sinif)
        print(self.aks)
        print(self.maksHiz)
        print(self.marka)

class Araba(KaraAraclari):
    def __init__(self, sinif, aks, maksHiz, marka, model, kasaTipi):
        KaraAraclari.__init__(self, sinif, aks, maksHiz, marka)
        self.model = model
        self.kasaTipi = kasaTipi
    def bilgilerAraba(self):
        KaraAraclari.bilgiler(self)
        print(self.model)
        print(self.kasaTipi)
class Kamyon(KaraAraclari):
    def __init__(self, sinif, aks, maksHiz, marka, kasaAgirlik):
        KaraAraclari.__init__(self, sinif, aks, maksHiz, marka)
        self.kasaAgirlik = kasaAgirlik
    def bilgilerKamyon(self):
        KaraAraclari.bilgiler(self)
        print(self.kasaAgirlik)

a = Araba(1,4,150,"mercedes","a200", "hatchback")
a.bilgilerAraba()
b = Kamyon(1,2,100,"Mercedes", 100000)
b.bilgilerKamyon()
