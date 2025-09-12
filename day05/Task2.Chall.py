import random
import time


def fast_sort(liste):
    if len(liste) <= 1:
        return liste
    else:
        pivot = liste[0]
        greater = [n for n in liste[1:] if n > pivot]
        lesser = [n for n in liste[1:] if n <= pivot]
        return fast_sort(greater) + [pivot] + fast_sort(lesser)


start = time.time()
liste = []
for i in range(100001):
    liste.append(random.randint(0, 10000000000))

print(fast_sort(liste)[::-1])

print(time.time() - start)
