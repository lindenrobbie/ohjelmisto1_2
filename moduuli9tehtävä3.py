class Car:
    pass
    def __init__(self, name, plate, mspeed, speed = 0, ometer = 0): #olio määrittely
        self.name = name
        self.plate = plate
        self.mspeed = mspeed
        self.speed = speed
        self.ometer = ometer

    def accelerate(self, added_speed): #kiihdytä metodi
        self.speed += added_speed
        if self.speed > self.mspeed:
            self.speed = self.mspeed
        if self.speed < 0:
            self.speed = 0

    def travel(self, hours): #tämä on kulje metodi
        self.ometer += self.speed * hours

    def __str__(self): #tämä on funktio joka tulostaa kaikki auton tiedot, nyt updated että taulukko ei anna turhia tietoja
        return f"Rekkari: {self.plate}\nKuljettu matka: {self.ometer}\n"

import random

cars = [Car("Auto", f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]

while all(car.ometer < 10000 for car in cars):
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.travel(1)

sorted_cars = sorted(cars, key=lambda car: car.ometer, reverse=True)

for i in sorted_cars:
    print(i)












