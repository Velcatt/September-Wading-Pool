import pygame
import random
import datetime
from english_words import get_english_words_set

from inputbox import InputBox

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


class Game:

    def __init__(self):
        self.goal = self.randomset(EASY_ENGLISH_WORDS_SET)
        self.penalty = 0
        self.attempts = 0
        self.best_score = []
        self.current = self.initcurrent(self.goal)
        self.guess = ""
        self.guessed_letters = []
        self.announcement = ""
        self.info = ""
        self.score = ""
        self.last_input = ""
        self.event = pygame.event.Event(pygame.USEREVENT)
        self.newgame = True

    def randomset(self, s):
        return random.sample(sorted(s), 1)[0]

    def initcurrent(self, goal):
        current = ""
        for i in goal:
            current += "*"
        return current

    def lettercheck(self, letter, goal):
        return letter in goal

    def occurences(self, letter, goal):
        li = []
        for i in range(len(goal)):
            if goal[i] == letter:
                li.append(i)
        return li

    def replace_in_current(self, current, li, letter):
        newcurrent = ""
        for i in range(len(current)):
            if i in li:
                newcurrent += letter
            else:
                newcurrent += current[i]
        return newcurrent

    def run(self):
        self.event = pygame.event.poll()
        if self.event.type == pygame.QUIT:
            self.newgame = False
            return False
        if self.current == self.goal:
            if self.guess == "again":
                self.newgame = True
                return False
            elif self.guess == "quit":
                self.newgame = False
                return False
        if self.guess != self.last_input:
            self.guess = self.last_input
            if len(self.guess) > 1:
                self.attempts += 1
                if self.guess == self.goal:
                    self.announcement = "YOU WIN!"
                    self.score = "Score : " + str(self.attempts)
                    self.best_score.append(datetime.date.today().isoformat())
                    self.best_score.append(str(self.attempts))
                    print(self.best_score)
                    self.current = self.goal
                    self.info = "Type 'again' to try again, 'quit' to quit"
                else:
                    self.info = "Incorrect guess!"
                    self.penalty += 3
            else:
                if self.guess in self.guessed_letters:
                    self.info = "You already tried '" + self.guess + "'"
                elif self.guess not in ALPHABET_LIST:
                    self.info = "Not a lowercase letter, try again !"
                else:
                    self.attempts += 1
                    self.guessed_letters.append(self.guess)
                    if self.lettercheck(self.guess, self.goal):
                        occ = self.occurences(self.guess, self.goal)
                        self.info = "Found " + str(len(occ)) + " '" + self.guess + "'"
                        self.current = self.replace_in_current(
                            self.current, occ, self.guess
                        )
                        if self.current == self.goal:
                            self.announcement = "YOU WIN!"
                            self.score = "Score : " + str(self.attempts)
                            self.best_score.append(datetime.date.today().isoformat())
                            self.best_score.append(str(self.attempts))
                            print(self.best_score)
                            self.info = "Type 'again' to try again, 'quit' to quit"
                    else:
                        self.info = "No '" + self.guess + "' found"
                        self.penalty += 1
        if self.penalty >= 10:
            self.announcement = "YOU LOSE!"
            self.current = self.goal
            self.info = "Type 'again' to try again, 'quit' to quit"
        return True
