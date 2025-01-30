print("")

from math import pi

def pizza_value(halkaisija, hinta):
    pinta_ala = (halkaisija / 2) ** 2 * pi
    return (hinta / pinta_ala)


def main():
    pizzas = {}

    for i in range(1, 3):
        halkaisija = int(input(f"Pizza {i}:n halkaisija: "))
        print("")
        hinta = int(input(f"Pizza {i}:n hinta: "))
        print("")

        pizzas[pizza_value(halkaisija, hinta)] = i

    return print(f"Pizza {pizzas[min(pizzas)]} on better bang for ya buck")


main()
