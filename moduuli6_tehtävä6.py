print("")

from math import pi

def pizza_value(diameter, price):
    area = (diameter / 2) ** 2 * pi
    return (price / area)


def main():
    pizzas = {}

    for i in range(1, 3):
        diameter = int(input(f"Pizza {i}:n halkaisija: "))
        print("")
        price = int(input(f"Pizza {i}:n hinta: "))
        print("")

        pizzas[pizza_value(diameter, price)] = i

    return print(f"Pizza {pizzas[min(pizzas)]} on better bang for ya buck")


main()
