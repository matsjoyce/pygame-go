import pygame_quick

window = pygame_quick.window(600, 400)

block = pygame_quick.surface(10, 10)
block.fill(pygame_quick.color.red)

while window.active():
    window.fill(pygame_quick.color.white)
    block.draw_by_center(window, pygame_quick.mouse_position())
    window.update()
