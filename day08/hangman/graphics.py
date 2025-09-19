import pygame
from inputbox import InputBox
from button import Button


class Graphics:

    def __init__(self, menu):
        self.easy = Button(200, 250, 200, 32, "Easy")
        self.hard = Button(200, 300, 200, 32, "Hard")
        self.quit = Button(200, 350, 200, 32, "Quit")
        self.title_font = pygame.font.SysFont(None, 40)
        self.title = self.title_font.render("HANGMAN", False, (0, 0, 0))
        self.name_font = pygame.font.SysFont(None, 25)
        self.name = self.name_font.render("Enter your name : ", False, (255, 255, 255))
        self.name_input = InputBox(200, 500, 200, 32)

        self.window = pygame.display.set_mode((600, 600))
        self.bg = pygame.image.load("pixelart.png")
        self.game_font = pygame.font.SysFont(None, 25)
        self.announcement_font = pygame.font.SysFont(None, 40)
        self.info_font = pygame.font.SysFont(None, 25)
        self.score_font = pygame.font.SysFont(None, 32)
        self.announcement = self.announcement_font.render("", False, (0, 0, 0))
        self.info = self.info_font.render("", False, (0, 0, 0))
        self.score = self.score_font.render("", False, (0, 0, 0))
        self.input_box = InputBox(50, 500, 140, 32)
        self.initialized = True

    def update(self, game, event):
        self.text_surface = self.render_word(game.current)
        self.info = self.info_font.render(game.info, False, (255, 255, 255))
        self.announcement = self.announcement_font.render(
            game.announcement, False, (0, 0, 0)
        )
        self.score = self.score_font.render(game.score, False, (0, 0, 0))

        self.window.blit(self.bg, (0, 0))
        self.window.blit(self.announcement, (230, 350))
        self.window.blit(self.text_surface, (50, 460))
        self.window.blit(self.info, (270, 505))
        self.window.blit(self.score, (230, 375))

        self.input_box.update()
        self.input_box.handle_event(event)
        self.input_box.draw(self.window)

        self.hangman_draw(game.penalty)

        pygame.display.update()

    def menu_update(self, event):
        if self.easy.is_pressed(event):
            return "Easy"
        elif self.hard.is_pressed(event):
            return "Hard"
        elif self.quit.is_pressed(event):
            return "Quit"
        self.window.blit(self.bg, (0, 0))
        self.window.blit(self.title, (200, 200))
        self.window.blit(self.name, (200, 450))
        self.easy.draw(self.window)
        self.hard.draw(self.window)
        self.quit.draw(self.window)
        self.name_input.update()
        self.name_input.handle_event(event)
        self.name_input.draw(self.window)
        pygame.display.update()
        return ""

    def render_word(self, current):
        return self.game_font.render(self.step(current), False, (255, 255, 255))

    def step(self, current):
        result = ""
        for i in current:
            if i == "*":
                result += "_ "
            else:
                result += i + " "
        return result

    # HANGMAN DRAW FUNCTIONS ------------------------------------

    def draw_gallows_1(self):
        pygame.draw.line(self.window, (0, 0, 0), (150, 430), (150, 40), width=10)

    def draw_gallows_2(self):
        pygame.draw.line(self.window, (0, 0, 0), (150, 40), (300, 40), width=10)

    def draw_gallows_3(self):
        pygame.draw.line(self.window, (0, 0, 0), (150, 100), (250, 40), width=10)

    def draw_gallows_4(self):
        pygame.draw.line(self.window, (0, 0, 0), (300, 40), (300, 100), width=10)

    def draw_head(self):
        pygame.draw.circle(self.window, (0, 0, 0), (300, 100), 30)

    def draw_body(self):
        pygame.draw.line(self.window, (0, 0, 0), (300, 130), (300, 250), width=10)

    def draw_left_arm(self):
        pygame.draw.line(self.window, (0, 0, 0), (300, 130), (250, 210), width=10)

    def draw_right_arm(self):
        pygame.draw.line(self.window, (0, 0, 0), (300, 130), (350, 210), width=10)

    def draw_left_leg(self):
        pygame.draw.line(self.window, (0, 0, 0), (300, 250), (250, 330), width=10)

    def draw_right_leg(self):
        pygame.draw.line(self.window, (0, 0, 0), (300, 250), (350, 330), width=10)

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

    def hangman_draw(self, penalty):
        for i in range(min(penalty, 10)):

            self.HANGMAN_DRAW_FUNCTIONS[i](self)
