import pygame
from graphics import Graphics
from game import Game

# MAIN CODE ----------------------------------------------------

pygame.init()

newgame = True
playing = True

game = Game()
graphics = Graphics(game)

while newgame:
    if game.current == game.goal:
        game = Game()
        playing = True
        graphics.input_box.reset_last_input()
        graphics.update(game)
    while playing:
        game.last_input = graphics.input_box.last_input
        playing = game.run()
        newgame = game.newgame
        graphics.update(game)
        

pygame.display.quit()
pygame.quit()
