import pygame
from graphics import Graphics
from game import Game

# MAIN CODE ----------------------------------------------------

pygame.init()

newgame = True


while newgame:
    game = Game()
    graphics = Graphics(game)
    newgame = game.newgame
    graphics.update(game)
    playing = True

    while playing and newgame:
        game.last_input = graphics.input_box.last_input
        playing = game.run()
        graphics.update(game)

pygame.display.quit()
pygame.quit()
