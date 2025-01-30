from random import randint

print('')
dice = int(input("Syötä noppien määrä numeroina: "))
print('')
sum = 0

for i in range(dice):
    sum += randint(1, 6)

print(f"Noppien summa on: {sum}. ")
print('')



