VIGENERE_REF = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
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


text = (
    input("Enter a text : ").lower().replace(".", "").replace(",", "").replace("'", "")
)
key = input("Enter the encryption key : ")
key = key.replace(" ", "")
choice = input('type "a" to encrypt or "b" to decrypt : ')

if choice == "a":
    print(encrypt(text, key))
elif choice == "b":
    print(decrypt(text, key))
else:
    print('Wrong choice ! Please only type "a" or "b" in the choice field')
