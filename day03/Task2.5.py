p = "abcdefghij"
print (p[::-2][:5][::-1][3:])

#Le premier bracket donne "jhfdb" (un step de -2 fait que l'on pars de la fin et on garde un caractère sur 2)
#Le deuxième bracket donne "jhfdb" puisqu'il y a 5 caractères
#Le troisième bracket donne "bdfhj" (un step de -1 fait qu l'on prend la même string mais à l'envers)
#Le quatrième bracket donne "hj" puisqu'on ne prend du caractère en 3ème position jusqu'à la fin de la string