import random

print()

# 3 digit codelock random value generator
v1 = random.randint(0, 9)
v2 = random.randint(0, 9)
v3 = random.randint(0, 9)

# 4 digit codelock random value generator

v4 = random.randint(1, 6)
v5 = random.randint(1, 6)
v6 = random.randint(1, 6)
v7 = random.randint(1, 6)

print(f"Random numerolukon koodit ovat:")
print()

print(f"Kolme lukuinen koodi: {v1}{v2}{v3}")
print(f"Neljä lukuinen koodi: {v4}{v5}{v6}{v7}")