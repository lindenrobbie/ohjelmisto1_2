print("")

def main():

    talvi = (12,1,2)
    kevat = (3,4,5)
    kesa = (6,7,8)
    syksy = (9,10,11)

    while True:

        kuukausi = input('Syötä tähän kuukausi: ')

        if kuukausi == '':
            break

        kuukausi = int(kuukausi)

        if kuukausi in talvi:
            print("Kuukausi kuuluu talveen. ")
        elif kuukausi in kevat:
            print("Kuukausi kuuluu kevääseen. ")
        elif kuukausi in kesa:
            print("Kuukausi kuuluu kesään. ")
        elif kuukausi in syksy:
            print("Kuukausi kuuluu syksyyn. ")

main()
