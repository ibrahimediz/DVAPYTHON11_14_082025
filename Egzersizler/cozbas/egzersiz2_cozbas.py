"""
diagram1.png dosyasını dikkate alarak 4 class oluşturalım.
"""

from abc import ABC, abstractmethod

class KaraAraci(ABC):
    @abstractmethod
    def bilgi(self):
        pass
class Motor:
    def __init__(self, hp):
        self.hp = hp

class Araba(KaraAraci):
    def __init__(self, motor,model):
        self.motor = motor
        self.model = model
    def bilgi(self):
        print(30*'#')
        print(f"Araba - Motor {self.motor.hp} HP \nModel {self.model} ")
        
class Kamyon(KaraAraci):
    def __init__(self, motor):
        self.motor = motor
    def bilgi(self):
        print(30*'#')
        print(f"Kamyon - Motor {self.motor.hp} HP")
class Minibus(KaraAraci):
    def __init__(self, motor):
        self.motor = motor
    def bilgi(self):
        print(30*'#')
        print(f"Minibüs - Motor {self.motor.hp} HP")
motor1_6 = Motor(150)
motorKamyon = Motor(400)
motorBus = Motor(220)

car = Araba(motor1_6,"Toyota Corolla")
mini = Minibus(motorBus)
truck = Kamyon(motorKamyon)

for vehicle in [car,mini,truck]:
    vehicle.bilgi()