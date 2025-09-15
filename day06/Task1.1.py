def f1():
    return 42


def f2():
    return 2 * x


print(f1())  # f1 retourne 42 donc ce print affiche 42
print(f2(5) + f1())  # f2 retourne 2*x, ici x==5 donc ce print affiche 10 + 42 = 52
