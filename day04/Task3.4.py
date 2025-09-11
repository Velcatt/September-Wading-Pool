import itertools

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

ALPHABET_LIST = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

ENGLISH_LETTER_FREQ = {
    "e": 12.7,
    "t": 9.1,
    "a": 8.2,
    "o": 7.5,
    "i": 7.0,
    "n": 6.7,
    "s": 6.3,
    "h": 6.1,
    "r": 6.0,
    "d": 4.3,
    "l": 4.0,
    "c": 2.8,
    "u": 2.8,
    "m": 2.4,
    "w": 2.4,
    "f": 2.2,
    "g": 2.0,
    "y": 2.0,
    "p": 1.9,
    "b": 1.5,
    "v": 1.0,
    "k": 0.8,
    "j": 0.2,
    "x": 0.2,
    "q": 0.1,
    "z": 0.1,
}


def english_check(text):
    occurence = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    frequency = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    score = 0
    for i in range(26):
        occurence[ALPHABET_REF[i]] = text.count(ALPHABET_REF[i])
    for i in range(26):
        frequency[ALPHABET_REF[i]] = occurence[ALPHABET_REF[i]] / len(text) * 100
    for i in range(26):
        score += abs(frequency[ALPHABET_REF[i]] - ENGLISH_LETTER_FREQ[ALPHABET_REF[i]])
    return score


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


def allcombinations(length):
    combinations = itertools.product(ALPHABET_LIST, repeat=length)
    return combinations


message = input("Enter a message to decrypt : ").lower()
keylength = int(input("Enter the length of the key : "))
combinations = allcombinations(keylength)
results = []
for testkey in combinations:
    decrypted = decrypt(message, testkey)
    results.append([decrypted, testkey, english_check(decrypted)])
best = ["", "", 100]
for i in results:
    if i[2] < best[2]:
        best = i
print("the decrypted message is : " + str(best[0]))
print("the key is : " + str(best[1]))
