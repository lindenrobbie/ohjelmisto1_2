print("")

def main():

    airports = {}

    while True:
        print("")
        request_type = input('Haluatko syöttää vai hakea tietoa lentokentästä? S/H: ')

        if request_type == 'H':
            print("")
            icao = input('Syötä tähän hakuun ICAO tunnus: ')
            if icao in airports:
                print("")
                print(f"Syöttämäsi tunnus {icao} kuuluu {airports[icao]} nimiselle lentokentälle. ")
            else:
                print("")
                print("Syöttämäsi tunnus on invaliidi tai ei ole olemassa. ")

        elif request_type == 'S':

            print("")
            icao = input('Tallenna tähän lentokentän ICAO tunnus: ')

            if icao in airports:
                print("")
                print("Lentokentän tunnus on jo käytössä. ")

            else:

                name = input('Tallenna tähän lentokentän nimi: ')

                if name in airports:
                    print("")
                    print("Lentokentän tunnus on jo käytössä. ")

                else:
                    print("")
                    airports[icao] = name
                    print(f'Lentokenttä {name} on nyt tallennettu koodilla {icao}')


        elif request_type == '':
            break

main()





