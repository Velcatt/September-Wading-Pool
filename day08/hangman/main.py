import pygame
import random
from english_words import get_english_words_set
from inputbox import InputBox

# GLOBAL VARIABLES ------------------------------------------------

ENGLISH_WORDS_SET = get_english_words_set(["web2"], lower=True)

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


def step(current):
    result = ""
    for i in current:
        if i == "*":
            result += "_ "
        else:
            result += i + " "
    return result


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


# DISPLAY FUNCTIONS --------------------------------------------------


def win():
    return announcement_font.render("YOU WIN!", False, (0, 255, 0))


def lose():
    return announcement_font.render("YOU LOSE!", False, (255, 0, 0))


def already_used(letter):
    return info_font.render(
        "You already tried '" + letter + "'", False, (255, 255, 255)
    )


def letter_found(letter, occ):
    return info_font.render(
        "Found " + str(len(occ)) + " '" + letter + "'", False, (255, 255, 255)
    )


def letter_not_found(letter):
    return info_font.render("No '" + letter + "' found", False, (255, 255, 255))


def not_a_letter():
    return info_font.render("Not a letter, try again !", False, (255, 255, 255))


def again():
    return info_font.render(
        "Type 'again' to try again, 'quit' to quit", False, (255, 255, 255)
    )


def incorrect():
    return info_font.render("Incorrect guess!", False, (255, 255, 255))


def render_word(current):
    return game_font.render(step(current), False, (255, 255, 255))


# HANGMAN DRAW FUNCTIONS --------------------------------------


def draw_gallows_1():
    pygame.draw.line(window, (0, 0, 0), (150, 430), (150, 40), width=10)


def draw_gallows_2():
    pygame.draw.line(window, (0, 0, 0), (150, 40), (300, 40), width=10)


def draw_gallows_3():
    pygame.draw.line(window, (0, 0, 0), (150, 100), (250, 40), width=10)


def draw_gallows_4():
    pygame.draw.line(window, (0, 0, 0), (300, 40), (300, 100), width=10)


def draw_head():
    pygame.draw.circle(window, (0, 0, 0), (300, 100), 30)


def draw_body():
    pygame.draw.line(window, (0, 0, 0), (300, 130), (300, 250), width=10)


def draw_left_arm():
    pygame.draw.line(window, (0, 0, 0), (300, 130), (250, 210), width=10)


def draw_right_arm():
    pygame.draw.line(window, (0, 0, 0), (300, 130), (350, 210), width=10)


def draw_left_leg():
    pygame.draw.line(window, (0, 0, 0), (300, 250), (250, 330), width=10)


def draw_right_leg():
    pygame.draw.line(window, (0, 0, 0), (300, 250), (350, 330), width=10)


HANGMAN_DRAW_FUNCTIONS = [
    draw_gallows_1,
    draw_gallows_2,
    draw_gallows_3,
    draw_gallows_4,
    draw_head,
    draw_body,
    draw_left_arm,
    draw_right_arm,
    draw_left_leg,
    draw_right_leg,
]

# GAME MAIN FUNCTION -------------------------------------------


def game():
    goal = randomset(ENGLISH_WORDS_SET)
    penalty = 0
    current = initcurrent(goal)
    guess = ""
    guessed_letters = []

    text_surface = render_word(current)
    announcement = announcement_font.render("", False, (0, 0, 0))
    info = info_font.render("", False, (0, 0, 0))
    input_box = InputBox(50, 500, 140, 32)

    running = True
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        window.blit(bg, (0, 0))
        input_box.handle_event(event)
        if guess != input_box.last_input:
            guess = input_box.last_input
            if len(guess) > 1:
                if guess == goal:
                    announcement = win()
                    current = goal
                    info = again()
                else:
                    info = incorrect()
                    penalty += 3
            else:
                if guess in guessed_letters:
                    info = already_used(guess)
                elif guess not in ALPHABET_LIST:
                    info = not_a_letter()
                else:
                    guessed_letters.append(guess)
                    if lettercheck(guess, goal):
                        occ = occurences(guess, goal)
                        info = letter_found(guess, occ)
                        current = replace_in_current(current, occ, guess)
                        if current == goal:
                            announcement = win()
                            info = again()
                    else:
                        info = letter_not_found(guess)
                        penalty += 1

        for i in range(min(penalty, 10)):
            HANGMAN_DRAW_FUNCTIONS[i]()
        if penalty >= 10:
            announcement = lose()
            current = goal
            info = again()
        if current == goal:
            if guess == "again":
                return True
            elif guess == "quit":
                return False
        text_surface = render_word(current)
        window.blit(announcement, (230, 350))
        window.blit(text_surface, (50, 460))
        window.blit(info, (270, 505))
        input_box.update()
        input_box.draw(window)
        pygame.display.update()


# MAIN CODE ----------------------------------------------------

pygame.init()
window = pygame.display.set_mode((600, 600))
bg = pygame.image.load("pixelart.png")

game_font = pygame.font.SysFont(None, 25)
announcement_font = pygame.font.SysFont(None, 40)
info_font = pygame.font.SysFont(None, 25)

playing = True
while playing:
    playing = game()


pygame.display.quit()
pygame.quit()
