import time


def power(num, puissance):
    if puissance > 1:
        return num * power(num, puissance - 1)
    else:
        return num


start = time.time()
print(power(42, 84))
print("time : " + str(time.time() - start))

start = time.time()
print(power(42, 168))
print("time : " + str(time.time() - start))
