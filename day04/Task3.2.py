ref = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
encrypted = input("Enter a caesar encrypted sentence : ")
key = int(input("Enter the encryption key : "))
decrypted = ""
for chara in encrypted:
    if chara == " ":
        decrypted += " "
    else:
        decrypted += ref[ref.find(chara) - key]
print(decrypted)
