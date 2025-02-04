print("")

def main():

    namelist = set()

    while True:
        print("")
        useri = input('Syötä tähän nimi: ')
        print("")

        if useri == '':
            for useri in namelist:
                print(useri)
            break
        elif useri in namelist:
            print(f"Nimi {useri} on jo listassa. ")
        else:
            namelist.add(useri)
            print(f"Nimi {useri} lisätty listaan! ")


main()
