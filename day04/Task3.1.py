sentence = input("Enter a message to encrpyt : ")
key = int(input("Enter the encryption key (an int between 1 and 25) : "))
ref = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
encrypted = ""

for i in sentence:
    if i == " ":
        encrypted += " "
    else:
        encrypted += ref[ref.find(i) + key]
print(encrypted)
