print("Enter a sentence :")
x = input()
result = ""
li = x.split()
for i in li:
    result += i[0]
print(result)