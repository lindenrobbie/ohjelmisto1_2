class Car:
    pass
    def __init__(self, name, plate, mspeed, speed, ometer):
        self.name = name
        self.plate = plate
        self.mspeed = mspeed
        self.speed = speed
        self.ometer = ometer

    def __str__(self):
        return f"\nAuton nimi: {self.name}\nRekkari: {self.plate}\nMaksiminopeus: {self.mspeed}\nTän hetkinen nopeus: {self.speed}\nKuljettu matka: {self.ometer}"

mersu = Car('Mercedes-Benz C 2025', 'ABC-123', 142, 0,0)



print(mersu)



