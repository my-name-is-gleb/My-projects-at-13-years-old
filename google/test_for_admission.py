from itertools import product


available_letters = "АКЛОШ"
b = 0
for word in product(available_letters, repeat=6):
    if "А" in word or "О" in word:
        b += 1
print(b)