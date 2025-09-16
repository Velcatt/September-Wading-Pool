import random
from english_words import get_english_words_set


def lose(penalty, goal):
    if penalty >= 12:
        print("You loose!")
        print("The word was '" + goal + "'")


def win(penalty, goal):
    if penalty <= 1:
        print("correct! - " + str(penalty) + " penalty")
    else:
        print("correct! - " + str(penalty) + " penalties")


def randomset(s):
    return random.sample(sorted(s), 1)


def printunderscores(s):
    for i in range(len(s)):
        print("_ ", end="")


def initcurrent(goal):
    current = ""
    for i in range(len(goal)):
        current += "*"
    return current


def lettercheck(letter, goal):
    return letter in goal


def occurences(letter, goal):
    li = []
    for i in range(len(goal)):
        if goal[i] == letter:
            li.append(i)
    return li


def replaceincurrent(
    current,
    li,
    letter,
):
    newcurrent = ""
    for i in range(len(current)):
        if i in li:
            newcurrent += letter
        else:
            newcurrent += current[i]
    return newcurrent


def step(current, penalty):
    for i in current:
        if i == "*":
            print("_ ", end="")
        else:
            print(i + " ", end="")
    if penalty <= 1:
        print(" / " + str(penalty) + " penalty")
    else:
        print(" / " + str(penalty) + " penalties")


english_words_set = get_english_words_set(["web2"], lower=True)
mode = input("type 'a' to chose a word or 'b' to get a random one : ")
if mode == "a":
    goal = input("Enter the word to guess : ")
elif mode == "b":
    goal = randomset(english_words_set)[0]
else:
    print(
        "ERREUR : veuillez ne choisir que 'a' ou 'b' comme mode. Mode 'b' utilisé par défaut"
    )
    goal = randomset(english_words_set)[0]

current = initcurrent(goal)
penalty = 0
printunderscores(goal)
while current != goal and penalty < 12:
    guess = input("Make a guess : ")
    if len(guess) > 1:
        if guess == goal:
            current = goal
            win(penalty, goal)
        else:
            penalty += 5
            print("incorrect guess - " + str(penalty) + " penalties")
    else:
        if lettercheck(guess, goal):
            occ = occurences(guess, goal)
            print("Found " + str(len(occ)) + " '" + guess + "'")
            current = replaceincurrent(current, occ, guess)
            step(current, penalty)
            if current == goal:
                win(penalty, goal)
        else:
            print("No '" + guess + "' found")
            penalty += 1
            step(current, penalty)
lose(penalty, goal)
