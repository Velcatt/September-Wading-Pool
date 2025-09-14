import itertools
import time

# VARIABLES GLOBALES -----------------------------------------------------------------------------------------------------------------------------------------------
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

# FONCTIONS -----------------------------------------------------------------------------------------------------------------------------------------------


def englishcheck(
    text,
):  # Fonction qui donne un score à un texte en fonction de s'il ressemble à de l'anglais ou non. Plus le score est bas, plus c'est proche de l'anglais
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
    # Reconnaissance par fréquence -----------------------------------
    for i in range(26):
        occurence[ALPHABET_REF[i]] = text.count(ALPHABET_REF[i])
    for i in range(26):
        frequency[ALPHABET_REF[i]] = occurence[ALPHABET_REF[i]] / len(text) * 100
    for i in range(26):
        score += abs(frequency[ALPHABET_REF[i]] - ENGLISH_LETTER_FREQ[ALPHABET_REF[i]])
    # Reconnaissance par dictionnaire (simple) -----------------------
    if " the " in text:
        score -= 5 * text.count(" the ")
    if " of " in text:
        score -= 5 * text.count(" of ")
    if " to " in text:
        score -= 5 * text.count(" to ")
    if " be " in text:
        score -= 5 * text.count(" be ")
    return score


def decrypt(text, key):  # Fonction decryptant un texte encodé en vigenere, avec la clé
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


def allcombinations(
    probablekeyletters,
):  # Fonction retournant toutes les clés possibles à partir des lettres probables de la clé
    combinations = itertools.product(*probablekeyletters)
    return combinations


def blockify(
    message, keylength
):  # Fonction qui transforme un texte en blocs de même longueur que la clé
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


def mostcommonletter(
    occurence,
):  # Fonction retournant la lettre la plus commune dans un dictionnaire d'occurences
    maxkey = ""
    maxvalue = 0
    for key in occurence:
        if occurence[key] > maxvalue:
            maxkey = key
            maxvalue = occurence[key]
    return maxkey


def keynthletters(
    blocks, n
):  # Fonction retournant les lettres les plus probables pour la nième lettre de la clé, a partir des blocs
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
            occurence[
                block[n]
            ] += 1  # On prend l'occurence de chaque lettre à la nième position de chaques blocs
    most_common_letter = mostcommonletter(
        occurence
    )  # On prend la lettre la plus commune dans occurence
    result.append(
        ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 4 + 26) % 26]
    )  # Lettre de la clé si la lettre la plus commune est un "e"
    result.append(
        ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 19 + 26) % 26]
    )  # Lettre de la clé si la lettre la plus commune est un "t"
    result.append(
        ALPHABET_LIST[(VIGENERE_REF[most_common_letter] + 26) % 26]
    )  # Lettre de la clé si la lettre la plus commune est un "a"
    result.append(
        ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 14 + 26) % 26]
    )  # Lettre de la clé si la lettre la plus commune est un "o"
    result.append(
        ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 8 + 26) % 26]
    )  # Lettre de la clé si la lettre la plus commune est un "i"
    result.append(
        ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 13 + 26) % 26]
    )  # Lettre de la clé si la lettre la plus commune est un "n"
    result.append(
        ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 18 + 26) % 26]
    )  # Lettre de la clé si la lettre la plus commune est un "s"
    result.append(
        ALPHABET_LIST[(VIGENERE_REF[most_common_letter] - 7 + 26) % 26]
    )  # Lettre de la clé si la lettre la plus commune est un "h"
    return result


# MAIN -----------------------------------------------------------------------------------------------------------------------------------------------

message = (
    input("Enter a message to decrypt : ").lower().replace(".", "").replace(",", "")
)
keylength = int(input("Enter the length of the key : "))

start = time.time()

# Attaque par fréquence, on utilise la fréquence des lettres dans des blocs de la taille de la clé pour trouver les lettres probables de la clés
blocks = blockify(message.replace(" ", ""), keylength)
probablekeyletters = [keynthletters(blocks, i) for i in range(keylength)]
combinations = allcombinations(probablekeyletters)

# Attaque par force brute, on test une à une toutes les possibilités de clés avec les lettres probables trouvées précédemment
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
