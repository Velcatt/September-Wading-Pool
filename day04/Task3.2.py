ref = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
encrypted = input("Enter a caesar encrypted sentence : ")

for key in range(1, 26):
    decrypted = ""
    for chara in encrypted:
        if chara == " ":
            decrypted += " "
        else:
            decrypted += ref[ref.find(chara) - key]
    print(decrypted)
