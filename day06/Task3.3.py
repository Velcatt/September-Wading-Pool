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
    if isinstance(n, int) and isinstance(s, str) and callable(funct):
        return funct(s, n)
    else:
        return "ERREUR DE TYPE : vérifiez les paramètres de la fonction passcheck"


print(passcheck(funA, 16, "ceciestunmotdepasse"))
print(passcheck(funB, 3, "ceciestunmotdepasse"))
print(passcheck(funC, 1, "ceciestunmotdepasse"))

print(passcheck(funA, 16, "ceciestunmotdepasse%*$3"))
print(passcheck(funB, 3, "ceciestunmotdepasse%*$3"))
print(passcheck(funC, 1, "ceciestunmotdepasse%*$3"))

print(passcheck(2, 1, "ceciestunmotdepasse%*$3"))
print(passcheck(funC, funA, "ceciestunmotdepasse%*$3"))
print(passcheck(funC, 1, 3))
