from os import listdir, getenv
from os.path import isfile, isdir, join


def lsr(location):
    files = listdir(location)
    for element in files:
        if isfile(join(location, element)) and element[0] != ".":
            print(str(element.encode("utf-8", "ignore"))[1::], end="")
        elif isdir(join(location, element)) and element[0] != ".":
            print("")
            print(str(join(location, element)) + ":")
            lsr(join(location, element))
            print("")


lsr(getenv("HOME"))
