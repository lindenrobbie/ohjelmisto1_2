print("")

def bensa():

    galloona = 3.785
    return galloona

while True:

    liters = float(input('Syötä galloonamäärä: '))

    if liters < 0:
        break

    else:

        print("")

        print(f"{liters} galloonaa on {liters * bensa()} ")

        print("")


