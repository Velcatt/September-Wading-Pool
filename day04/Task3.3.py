VIGENERE_REF = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

ALPHABET_REF = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"


def encrypt(text, key):
    final = ""
    n = 0
    for character in text:
        if character == " ":
            final += " "
        else:
            final += ALPHABET_REF[ALPHABET_REF.find(character) + VIGENERE_REF[key[n]]]
            if n == len(key) - 1:
                n = 0
            else:
                n += 1
    return final


def decrypt(text, key):
    final = ""
    n = 0
    for character in text:
        if character == " ":
            final += " "
        else:
            final += ALPHABET_REF[ALPHABET_REF.find(character) - VIGENERE_REF[key[n]]]
            if n == len(key) - 1:
                n = 0
            else:
                n += 1
    return final


text = input("Enter a text : ").lower().replace(".", "")
key = input("Enter the encryption key : ")
key = key.replace(" ", "")
choice = input('type "a" to encrypt or "b" to decrypt : ')

if choice == "a":
    print(encrypt(text, key))
elif choice == "b":
    print(decrypt(text, key))
else:
    print('Wrong choice ! Please only type "a" or "b" in the choice field')
