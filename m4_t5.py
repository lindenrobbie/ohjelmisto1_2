print("")

attemps = 0
while attemps < 5:
    username = input("Käyttäjätunnus: ")
    print("")
    password = input("Salasana: ")
    print("")

    if username == "python" and password == "rules":
        break

    attemps += 1
print(f"Kirjautuminen onnistui." if attemps < 5 else "Pääsy evätty.")