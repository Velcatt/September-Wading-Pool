import itertools
import time

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


def englishcheck(text):
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
    if " the " in text:
        score -= 5 * text.count(" the ")
    if " of " in text:
        score -= 5 * text.count(" of ")
    if " to " in text:
        score -= 5 * text.count(" to ")
    if " be " in text:
        score -= 5 * text.count(" be ")
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


def allcombinations(probablekeyletters, length):
    combinations = itertools.product(*probablekeyletters)
    return combinations


def blockify(message, keylength):
    result = []
    temp_list = []
    i = 0
    while i < len(message) - 1:
        temp_list.append(message[i])
        if (i + 1) % keylength == 0:
            result.append(temp_list)
            temp_list = []
        i += 1
    if temp_list:
        result.append(temp_list)
    return result


def mostcommonletter(occurence):
    maxkey = ""
    maxvalue = 0
    for key in occurence:
        if occurence[key] > maxvalue:
            maxkey = key
            maxvalue = occurence[key]
    return maxkey


def removeduplicate(liste):
    i = 0
    while i < len(liste):
        if liste.count(liste[i]) > 1:
            liste.pop(i)
        i += 1
    return liste


def keynthletters(blocks, n):
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
    result = []
    for block in blocks:
        if len(block) > n:
            occurence[block[n]] += 1
    most_common_letter = mostcommonletter(occurence)
    result.append(ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 4 + 26) % 26])
    result.append(ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 19 + 26) % 26])
    result.append(ALPHABET_LIST[(VIGENERE_REF[most_common_letter] + 26) % 26])
    result.append(ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 14 + 26) % 26])
    result.append(ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 8 + 26) % 26])
    result.append(ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 13 + 26) % 26])
    result.append(ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 18 + 26) % 26])
    result.append(ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 7 + 26) % 26])
    return removeduplicate(result)


message = (
    input("Enter a message to decrypt : ").lower().replace(".", "").replace(",", "")
)
keylength = int(input("Enter the length of the key : "))

start = time.time()

blocks = blockify(message.replace(" ", ""), keylength)
probablekeyletters = [keynthletters(blocks, i) for i in range(keylength)]
combinations = allcombinations(probablekeyletters, keylength)

results = []
for testkey in combinations:
    decrypted = decrypt(message, testkey)
    results.append([decrypted, testkey, englishcheck(decrypted)])
best = ["", "", 100]
for i in results:
    if i[2] < best[2]:
        best = i
print("the decrypted message is : " + str(best[0]))
print("the key is : " + str(best[1]))
print("time : " + str(time.time() - start))
