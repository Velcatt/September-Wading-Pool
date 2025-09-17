import turtle  # Importe la library turtle

toto = turtle.Screen()  # Initialize l'écran turtle dans la variable toto
toto.bgcolor("black")  # Set la couleur du background à noir
titi = turtle.Turtle()  # Initialize la turtle dans la variable titi
titi.color("red")  # Set la couleur de la turtle titi en rouge
for i in range(3):  # Boucle for qui s'effectuera 3 fois
    titi.right(90)  # Tourne la turtle à 90° vers la droite
    titi.circle(42)  # Dit à la turtle de dessiner un cercle de rayon 42
toto.exitonclick()  # Le screen toto reste actif jusqu'à ce que l'on clique dessus

# Ce code va donc dessiner 3 cercles imbriqués, espacés de 90°, rouge sur fond noir
