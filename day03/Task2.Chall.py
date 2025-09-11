print("Ecrivez une phrase")
x = input()
x = x.lower()
n = 0
for i in range(len(x)-1):
    if x[i:i+3] == "cat":
        n += 1
    if x[i:i+4] == "mice":
        n += 1
    if x[i:i+6] == "garden":
        n += 1
    if x[-i:-i-3:-1] == "cat":
        n += 1
    if x[-i:-i-4:-1] == "mice":
        n += 1
    if x[-i:-i-6:-1] == "garden":
        n += 1
print(n)