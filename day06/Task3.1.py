import re


def funA(s, n):
    if len(s) >= n:
        return True
    else:
        return False


def funB(s, n):
    if len(re.findall(r"[!@#$%^&*()_+{}\[\]:;<>,.?\\/-]", s)) >= n:
        return True
    else:
        return False


def funC(s, n):
    if len(re.findall(r"[0123456789]", s)) >= n:
        return True
    else:
        return False


print(funA("ceci est un texte", 3))
print(funA("ceci est un texte", 42))
print(funB("$*+=&", 3))
print(funB("$*+=&", 42))
print(funC("12345", 4))
print(funC("12345", 42))
