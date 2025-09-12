liste = ["a", 2, "a", 2, "A"]
i = 0
while i < len(liste):
    if liste.count(liste[i]) > 1:
        liste.pop(i)
    i += 1

print(liste)
