print("")

cabin = input("Mikä on laivan hyttiluokka? LUX, A, B, C: ")

print("")
if cabin == "LUX": 
    print("LUX on parvekkeellinen hytti yläkannella.")
elif cabin == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif cabin == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif cabin == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Ole hyvä ja syötä valiidi hyttiluokka. ")
print("")
