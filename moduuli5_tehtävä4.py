kaupungit = []
print("")

for n in range (5):
    kaupunki = input(f'Syötä kaupunki {n + 1} nimi: ')
    kaupungit.append(kaupunki)
    n += 1

print("")

for kaupunki in kaupungit:
    print(kaupunki)
