print("input a number :")
x = int(input())
n = 0
while x%10 != x :
    n += x%10
    x = x//10
n+=x
print(n)