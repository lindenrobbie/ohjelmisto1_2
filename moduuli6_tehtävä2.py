import random
print("")

t = int(input('Syötä tähän nopan tahkojen määrä: '))
print("")
def luku():

    return random.randint(1,t)

while True:
    tulos = luku()
    print(f'Luvun silmäluvuksi tuli: {tulos}')
    if tulos == t:
        print("")
        print("Nice. ")
        break
    else:
        nothing = input('')

