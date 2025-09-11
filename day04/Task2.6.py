n = int(input("Enter an integer : "))
for i in range(2, n // 2 + 1):
    for j in range(n - 1, 0, -1):
        if j % i == 0:
            print(j, end=" ")
    print("")
