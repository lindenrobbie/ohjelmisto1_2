import random

def roulette(color, money):

    black = (0,48.5)
    red = (48.5,97)
    green = (97,100)

    odds = float(random.randint(0,100))


    if black[0] <= odds < black[1]:
        return "black"

    elif red[0] <= odds < red[1]:
        return "red"

    elif green[0] <= odds < green[1]:
        return "green"

def main():
    print("")

    money = float(input("Syötä opintolainan määrä: "))

    while True:

        if money == '':
            print("Peli sulkeutuu...")
            break

        else:
            print("")
            userluck = input('Valitse väri (Kirjoita green/red/black tai syötä tyhjä kenttä sulkeaksi): ')
            color = ''
            color = roulette(color, money)

            if userluck == '':
                print(f"Voitit {money}")
                break

            elif userluck != color:
                print('Womp womp... Hävisit :D')
                break

            else:
                money = money * 2
                print(f'Winner winner, rahaa on nyt {money}€. Nice')



main()

