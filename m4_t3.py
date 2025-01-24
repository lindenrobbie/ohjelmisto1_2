list = []
print("")
while True:
    luku = input("Anna luku: ")

    if luku == "":
        print("")
        print(f"Antamasi luvuista suurin luku on {max(list)} ja pienin luku on {min(list)}.")
        break

    if int(luku):
        list.append(luku)