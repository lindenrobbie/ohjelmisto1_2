print("")
gender =input('Mikä on teidän biologinen sukupuoli? (M / N) ')
print("")
hemoglobine = int(input('Mikä on teidän hemoglobiiniarvo? (g/l) '))
print("")

if gender == "N" and 117<=hemoglobine<=175:
    print("Teillä on normaali hemoglobiiniarvo. Woohoo!")
elif gender == "M" and 134<=hemoglobine<=195:
    print("Teillä on normaali hemoglobiiniarvo. Woohoo!")
else:
    print("Suosittelemme että käytte lääkärillä.")

print("")