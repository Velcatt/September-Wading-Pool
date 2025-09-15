def recursum(n):
    if n > 1:
        return n + recursum(n - 1)
    else:
        return 1


print(recursum(42))
