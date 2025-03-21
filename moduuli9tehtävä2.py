class Car:
    pass
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

    def __str__(self):
        return f"\nAuton nimi: {self.name}\nRekkari: {self.plate}\nMaksiminopeus: {self.mspeed}\nTän hetkinen nopeus: {self.speed}\nKuljettu matka: {self.ometer}"

mersu = Car('Mercedes-Benz C 2025', 'ABC-123', 142, 0,0)


def display_speed():
    print(f"{mersu.name}: {mersu.speed}km/h")

display_speed()

mersu.accelerate(30)

display_speed()

mersu.accelerate(70)

display_speed()

mersu.accelerate(50)

display_speed()

mersu.accelerate(-200)

display_speed()
