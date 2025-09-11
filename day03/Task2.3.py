string = "Hello world !"
position = string.find("a") #Il n'y a pas de "a" dans la phrase donc cette ligne va sortir une erreur
print(position) #CORRECTION : en fait lorsque find ne trouve pas de lettre il retourne -1