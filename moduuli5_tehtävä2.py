print("")
print("Tässä on ohjelma joka kysyy käyttäjältä lukuja. Kun haluat että ohjelma palauttaa 5 suurinta arvoa niin syötä tyhjä kenttä """)

digits = []

while True:

    user_digit = input('Syötä tähän luku: ')

    if user_digit == '':
        break

    else:
        user_digit = int(user_digit)
        digits.append(user_digit)

digits.sort(reverse=True)

highest = digits[:5]

print("")
print(f"Tässä on 5 suurinta lukua: {highest} ")


