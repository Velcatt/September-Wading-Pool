import pygame
import clock


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


pygame.init()
window = pygame.display.set_mode((600, 600))
bg = pygame.image.load("pixelart.png")

running = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    window.blit(bg, (0, 0))
    draw_head()
    draw_body()
    draw_left_arm()
    draw_right_arm()
    draw_left_leg()
    draw_right_leg()
    pygame.display.update()


pygame.display.quit()
pygame.quit()
