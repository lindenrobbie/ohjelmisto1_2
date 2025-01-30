import random
print("")
def luku():

    return random.randint(1,6)

while True:
    tulos = luku()
    print(f'Luvun silmäluvuksi tuli: {tulos}')
    if tulos == 6:
        print("")
        print("Nice. ")
        break
    else:
        nothing = input('')

