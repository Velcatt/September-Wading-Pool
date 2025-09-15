def bread():
    print("<//////////>")


def lettuce():
    print("~~~~~~~~~~~~")


def tomato():
    print("O O O O O O")


def ham():
    print("============")


def sandwich():
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()


def vegsandwich():
    bread()
    lettuce()
    lettuce()
    tomato()
    tomato()
    bread()


def preparesandwich(n, veg=False):
    if veg == False:
        for i in range(n):
            sandwich()
    elif veg == True:
        for i in range(n):
            vegsandwich()
    else:
        print("please chose only True or False for the vegetarian option")


preparesandwich(2, True)
preparesandwich(3)
preparesandwich(3, 2)
