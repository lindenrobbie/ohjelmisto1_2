print("")
print("Tässä on ohjelma joka muuntaa tuumat sentimetreiksi.")
print("")

while True:
    tuuma = float(input("Kirjoita tuumien määrä: "))

    if tuuma < 0:
        break
    print("")
    print(f"{tuuma} tuumaa on {tuuma * 2.56:.3f} senttimetriä")
    print("")