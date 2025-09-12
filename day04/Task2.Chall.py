entier = int(input("Enter an integer : "))
chaine = input("Enter a string : ")
vowels = ["a", "e", "i", "o", "u", "y"]
liste = [i in chaine for i in vowels]
if entier == 0:
    quit()
elif any(liste):
    print(entier)
elif entier >= 42:
    print(entier)
else:
    print(chaine)
