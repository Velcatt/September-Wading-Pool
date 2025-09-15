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


def preparesandwich(n):
    for i in range(n):
        sandwich()


preparesandwich(2)
