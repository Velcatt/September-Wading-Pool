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


def passcheck(funct, n, s):
    if funct(s, n):
        return True
    else:
        return False


print(passcheck(funA, 16, "ceciestunmotdepasse"))
print(passcheck(funB, 3, "ceciestunmotdepasse"))
print(passcheck(funC, 1, "ceciestunmotdepasse"))

print(passcheck(funA, 16, "ceciestunmotdepasse%*$3"))
print(passcheck(funB, 3, "ceciestunmotdepasse%*$3"))
print(passcheck(funC, 1, "ceciestunmotdepasse%*$3"))
