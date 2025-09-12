import random

liste = []
for i in range(1000001):
    liste.append(random.randint(0, 10000000000))
liste.sort()
print(liste)
