from random import randint
print("")
print("Tässä on arvauspeli.")
luku = randint(1, 10)
print("")

while True:
    arvaus = int(input('Arvaa luku väliltä 1 - 10: '))
    print("")

    if arvaus < luku:
        print("Liian pieni arvaus")
        print("")
    elif arvaus > luku:
        print("Liian suuri arvaus")
        print("")
    else:
        print("Arvaus oli oikein. Woohoo!")
        break