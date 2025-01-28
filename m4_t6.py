from random import uniform

pistemaara = int(input("Arvottavien pisteiden määrä: "))

ympyran_sisalla = 0

for i in range(pistemaara):
    x = uniform(-1, 1)
    y = uniform(-1, 1)

    if (x**2) + (y**2) < 1:
        ympyran_sisalla += 1

likiarvo = 4*  ympyran_sisalla / pistemaara

print(likiarvo)