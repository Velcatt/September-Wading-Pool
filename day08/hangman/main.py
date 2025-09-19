import pygame
from graphics import Graphics
from game import Game, Menu

# MAIN CODE ----------------------------------------------------

pygame.init()

isMenu = True
newgame = True
playing = True
event = pygame.event.Event(pygame.USEREVENT)
game_event = ""
menu_route = ""
name = ""

menu = Menu()

graphics = Graphics(menu)


while newgame:
    while isMenu:
        pygame_event = pygame.event.poll()
        if pygame_event.type == pygame.QUIT:
            game_event = "quit"
        quit_event = menu.quit_menu(game_event)
        newgame = quit_event
        name = graphics.name_input.text
        menu_route = graphics.menu_update(pygame_event) if quit_event else "Quit"
        isMenu = quit_event and (True if menu_route == "" else False)

    playing = False if menu_route == "Quit" else True

    if menu_route == "Scoreboard":
        scoreboard = Scoreboard()
    else:
        game = Game(menu_route, name)

    if game.current == game.goal:
        game = Game(menu_route, name)
        playing = True
        graphics.input_box.reset_last_input()
    while playing:
        pygame_event = pygame.event.poll()
        if pygame_event.type == pygame.QUIT:
            game_event = "quit"
        game.last_input = graphics.input_box.last_input
        playing = game.run(game_event)
        newgame = game.newgame
        graphics.update(game, pygame_event)


pygame.display.quit()
pygame.quit()
