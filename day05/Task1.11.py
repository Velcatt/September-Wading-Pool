my_first_list = [4, 5, 6]
my_second_list = [1, 2, 3]
my_first_list.extend(my_second_list)

print(my_first_list)

# Ajoute les élément de my_second_list à la fin de la première liste
# my_first_list serait donc [4, 5, 6, 1, 2, 3]

my_first_list = [7, 8, 9]
my_second_list = [4, 5, 6]
my_first_list = [*my_first_list, *my_second_list]

print(my_first_list)

# Idem, mais en utilisant l'opérateur *list qui unpack les listes et la virgule qui les concatène
# my_first_list serait donc [7, 8, 9, 4, 5, 6]
