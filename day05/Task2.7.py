liste = [*enumerate([42, 3, 4, 18, 3, 10])]
print(liste)

# enumerate crée un itérable de tuple en associant chaque nombre de la liste à un chiffre
# du style (0, 42) ; (1, 3) etc...
# l'itérable est ensuite unpacked avec l'opérateur * puis remis dans une liste (avec les crochets)
