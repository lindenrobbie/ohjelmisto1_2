print()

print("Tässä on ohjelma joka muuntaa keskiaikaiset mitat kilogrammoiksi")
print()
lei = float(input('Monta leiviskää? '))

nau = float(input('Monta naulaa? '))

luo = float(input('Monta luotia= '))
print()

leivisikä = lei * 8500
naula = nau * 4251
luoti = luo * 133

kilograms = int(leivisikä + naula + luoti) // 1000

sum_g = (leivisikä + naula + luoti) % 1000



print(f"Massa nykymittojen mukaan on: {kilograms:}kg ja {sum_g:0.3f} grammaa.")





