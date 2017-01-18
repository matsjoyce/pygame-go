import pygame_quick
import random

background_color = pygame_quick.color.white
block_x = block_y = 50

block = pygame_quick.Surface(10, 10)
block.fill(pygame_quick.color.red)
block2 = pygame_quick.Surface(10, 10)
block2.fill(255, 0, 255)
block3 = pygame_quick.Surface(10, 100)
block3.fill("blue")
block4 = pygame_quick.Surface(10, 100)
block4.fill("tomato")

# Note: screen does not need to be created first
screen = pygame_quick.Screen(600, 400)

while screen.active():
    for type, value in screen.events():
        if type is pygame_quick.mouse_event:
            if value.button is pygame_quick.left_button:
                print("Mouse click at", value.position, "using left button")
            elif value.button is pygame_quick.right_button:
                print("Mouse click at", value.position, "using right button")
            elif value.button is pygame_quick.middle_button:
                print("Mouse click at", value.position, "using middle button")
            else:
                print("Mouse scroll at", value.position, "using direction", value.scroll_direction)

        elif type is pygame_quick.key_event:
            if value == "<Left>":
                block_x -= 1
            elif value == "<Right>":
                block_x += 1
            elif value == "<Up>":
                block_y -= 1
            elif value == "<Down>":
                block_y += 1
            elif value == "b":
                background_color = random.choice(list(pygame_quick.color.all_colors))
            else:
                print("Key", repr(value), "pressed")

    screen.fill(background_color)
    block.draw(screen, block_x, block_y)
    block2.draw_by_center(screen, pygame_quick.mouse_position())
    block3.draw_by_center(screen, screen.center)
    block4.draw(screen, (10, 20))
    screen.update()

