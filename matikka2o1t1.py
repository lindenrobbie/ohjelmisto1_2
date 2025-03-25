import numpy as np

#tehtävä 1.1a ja 1.1b

print("\nTehtävä 1.1a ja 1.1b")
print(np.degrees(2.493))
print(np.degrees(0.911))

#tehtävä 1.2a ja 1.2b

print("\nTehtävä 1.2a ja 1.2b")
print(np.radians(137.7))
print(np.radians(62.3))

#tehtävä 1.3
print("\nTehtävä 1.3")
A = np.array([0, 30, 60, 90, 120, 135, 150, 180, 270, 360])

for i in A:
    print(f"{i} astetta: {np.radians(i)}")

#tehtävä 2.1

print("\nTehtävä 2.1")
print(f"{np.sqrt(1.6**2 + 2.3**2)} metriä.")
print()

#tehtävä 2.3

print("\nTehtävä 2.3")

c = 6.4

sa = 3
sb = 2

x = np.sqrt(c**2 / (sa**2 + sb**2))

a = sa * x
b = sb * x

print(f"Sivujen pituudet ovat {a:.2f} ja {b:.2f}")
