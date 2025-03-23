class Car:
    def __init__(self, name, plate, mspeed, speed=0, ometer=0):
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

    def travel(self, hours):
        self.ometer += self.speed * hours

    def __str__(self):
        return f"Rekkari: {self.plate}\nKuljettu matka: {self.ometer}\n"


import random

cars = [Car("Auto", f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]


class Kilpailu:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def tunti_kuluu(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.travel(1)

    def tulosta_tilanne(self):
        print(f"\nKilpailu: {self.name}\nPituus: {self.distance} km\n")
        print(f"{'Rekkari':<12} {'Matka':<8}")
        for car in self.cars:
            print(f"{car.plate:<12} {car.ometer:<8}")

    def kilpailu_ohi(self):
        return any(car.ometer >= self.distance for car in self.cars)


kilpailu = Kilpailu("Suuri romuralli", 8000, cars)

tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()