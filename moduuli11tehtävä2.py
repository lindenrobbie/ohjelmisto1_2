import random

class Car:

    def __init__(self, name, plate, mspeed, speed, ometer):
        self.name = name
        self.plate = plate
        self.mspeed = mspeed
        self.speed = speed
        self.ometer = ometer

    def accelerate(self, added_speed):
        self.speed += added_speed
        if self.speed > self.mspeed:
            self.speed = self.mspeed
        if self.speed < 0:
            self.speed = 0

    def travel(self, hours):  # tämä on kulje metodi
        self.ometer += self.speed * hours

    def __str__(self): #tämä on funktio joka tulostaa kaikki auton tiedot, nyt updated että taulukko ei anna turhia tietoja
        return f"{self.name} {self.plate}\nKuljettu matka: {self.ometer} km\n"



class electricCar(Car):
    def __init__(self, name, plate, mspeed, speed, ometer, battery):
        super().__init__(name, plate, mspeed, speed, ometer)
        self.battery = battery

class gasCar(Car):
    def __init__(self, name, plate, mspeed, speed, ometer, fuel):
        super().__init__(name, plate, mspeed, speed, ometer)
        self.fuel = fuel



cars = []

alepabot = electricCar('Alepa Kuljetusrobootti', 'ABC-123', 180, 120, 0, 52.5)
vauhtisampyla = gasCar('Vauhtisämpylä', 'ACD-124', 165, 30, 0, 32.3)

cars.append(alepabot)
cars.append(vauhtisampyla)


alepabot.travel(3)
vauhtisampyla.travel(3)

for i in cars:
    print(i)

