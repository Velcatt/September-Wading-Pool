x = int(input("Enter an integer : "))
if x == 42:
    print("a")
elif x <= 21:
    print("b")
elif x % 2 == 0:
    print("c")
elif x / 2 < 21:
    print("d")
elif x >= 45:
    print("e")
else:
    print("f")  # seulement atteint avec x == 43
