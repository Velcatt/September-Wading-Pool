import random
import os
from english_words import get_english_words_set

ENGLISH_WORDS_SET = get_english_words_set(["web2"], lower=True)


def lose(penalty, goal):
    if penalty >= 12:
        print("You loose!")
        print("The word was '" + goal + "'")


def win(penalty):
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
    for i in goal:
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


def game():

    mode = input("type 'a' to chose a word or 'b' to get a random one : ")
    if mode == "a":
        goal = input("Enter the word to guess : ")
    elif mode == "b":
        goal = randomset(ENGLISH_WORDS_SET)[0]
    else:
        print(
            "ERROR : please only chose between 'a' or 'b' for the mode. Mode 'b' choosed by default"
        )
        goal = randomset(ENGLISH_WORDS_SET)[0]

    maxpenalty = int(input("Enter the max number of penalties : "))

    current = initcurrent(goal)
    penalty = 0
    guessedletters = []
    os.system("clear")
    printunderscores(goal)
    while current != goal and penalty < maxpenalty:
        guess = input("Make a guess : ")
        if len(guess) > 1:
            if guess == goal:
                current = goal
                win(penalty)
            else:
                penalty += 5
                os.system("clear")
                print("incorrect guess - " + str(penalty) + " penalties")
                step(current, penalty)
        else:
            if guess in guessedletters:
                os.system("clear")
                print(
                    "You already asked for '" + guess + "', please chose another letter"
                )
                step(current, penalty)
            else:
                guessedletters.append(guess)
                if lettercheck(guess, goal):
                    occ = occurences(guess, goal)
                    os.system("clear")
                    print("Found " + str(len(occ)) + " '" + guess + "'")
                    current = replaceincurrent(current, occ, guess)
                    step(current, penalty)
                    if current == goal:
                        win(penalty)
                else:
                    os.system("clear")
                    print("No '" + guess + "' found")
                    penalty += 1
                    step(current, penalty)
    lose(penalty, goal)


# MAIN

playing = "yes"
while playing == "yes":
    game()
    playing = input("wanna play again ? yes/no : ")
