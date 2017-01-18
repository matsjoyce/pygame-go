import pygame_quick

screen = pygame_quick.Screen(600, 400)

block = pygame_quick.Surface(10, 10)
block.fill(pygame_quick.color.red)

while screen.active():
    screen.fill(pygame_quick.color.white)
    block.draw_by_center(screen, pygame_quick.mouse_position())
    screen.update()
