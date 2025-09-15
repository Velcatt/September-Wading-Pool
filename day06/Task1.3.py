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


for i in range(4):
    sandwich()
