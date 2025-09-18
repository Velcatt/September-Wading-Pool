import pygame
import random
import datetime
from english_words import get_english_words_set

from inputbox import InputBox
from graphics import Graphics

# GLOBAL VARIABLES ------------------------------------------------

ENGLISH_WORDS_SET = get_english_words_set(["web2"], lower=True)

EASY_ENGLISH_WORDS_SET = set(
    line.strip().lower() for line in open("word_list_easy.txt")
)

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

# BACK-END FUNCTIONS --------------------------------------


def underscores(s):
    result = ""
    for i in range(len(s)):
        result += "_ "
    return result


def randomset(s):
    return random.sample(sorted(s), 1)[0]


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


def replace_in_current(
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


# GAME MAIN FUNCTIONS -------------------------------------------


def game():
    # goal = randomset(EASY_ENGLISH_WORDS_SET)
    goal = "apple"
    penalty = 0
    attempts = 0
    best_score = []
    current = initcurrent(goal)
    guess = ""
    guessed_letters = []

    announcement = ""
    info = ""
    score = ""

    graphics = Graphics(current)

    running = True
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        if guess != graphics.input_box.last_input:
            guess = graphics.input_box.last_input
            if len(guess) > 1:
                attempts += 1
                if guess == goal:
                    announcement = "YOU WIN!"
                    score = "Score : " + str(attempts)
                    best_score.append(datetime.date.today().isoformat())
                    best_score.append(str(attempts))
                    print(best_score)
                    current = goal
                    info = "Type 'again' to try again, 'quit' to quit"
                else:
                    info = "Incorrect guess!"
                    penalty += 3
            else:
                if guess in guessed_letters:
                    info = "You already tried '" + guess + "'"
                elif guess not in ALPHABET_LIST:
                    info = "Not a lowercase letter, try again !"
                else:
                    attempts += 1
                    guessed_letters.append(guess)
                    if lettercheck(guess, goal):
                        occ = occurences(guess, goal)
                        info = "Found " + str(len(occ)) + " '" + guess + "'"
                        current = replace_in_current(current, occ, guess)
                        if current == goal:
                            announcement = "YOU WIN!"
                            score = "Score : " + str(attempts)
                            best_score.append(datetime.date.today().isoformat())
                            best_score.append(str(attempts))
                            print(best_score)
                            info = "Type 'again' to try again, 'quit' to quit"
                    else:
                        info = "No '" + guess + "' found"
                        penalty += 1
        if penalty >= 10:
            announcement = "YOU LOSE!"
            current = goal
            info = "Type 'again' to try again, 'quit' to quit"
        if current == goal:
            if guess == "again":
                return True
            elif guess == "quit":
                return False
        graphics.update(current, penalty, event, info, announcement, score)


# MAIN CODE ----------------------------------------------------

pygame.init()


playing = True
while playing:
    playing = game()


pygame.display.quit()
pygame.quit()
