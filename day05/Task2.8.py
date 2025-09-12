first_names = [" Jackie ", " Chuck ", " Arnold ", " Sylvester "]
last_names = [" Stallone ", " Schwarzenegger ", " Norris ", " Chan "]
magic = [
    *zip(first_names, last_names[::-1])
]  # Fait un iterable de tuples, en partant du début pour les first name et de la fin pour les last name.
# L'iterable est ensuite unpacké en dans une liste avec l'opérateur * et les crochets
print(magic[0])  # print le premier tuple
print(magic[3])  # print le 4eme tuple
print(magic[1][0])  # print le premier élément du 2eme tuple
print(magic[0][1])  # print le deuxième élément du 1er tuple
print(magic[2])  # print de 3eme tuple
