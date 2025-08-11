class Araba:
    def __init__(self,marka,motor,yıl,model):
        self.marka=marka
        self.motor=motor
        self.yıl=yıl
        self.model=model
    def bilgiver(self):
        print("*" * 30)
        print(f"Marka: {self.marka}")
        print(f"Motor: {self.motor}")
        print(f"Yıl: {self.yil}")
        print(f"Model: {self.model}")
        print("*" * 30)
car1 = Araba()