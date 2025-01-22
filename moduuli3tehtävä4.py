print("")
print("Tässä on ohjelma joka katsoo, jos vuosi on karkausvuosi")
print("")

year = int(input('Syötä vuosiluku: '))
print("")

if year % 4 == 0:
    print("Vuosi on karkausvuosi.")
else: print("Vuosi ei ole karkausvuosi.")
print("")