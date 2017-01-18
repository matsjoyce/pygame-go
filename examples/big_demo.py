import pygame_quick
import random

background_color = pygame_quick.color.white
block_x = block_y = 50

block = pygame_quick.surface(10, 10)
block.fill(pygame_quick.color.red)
block2 = pygame_quick.surface(10, 10)
block2.fill(255, 0, 255)
block3 = pygame_quick.surface(10, 100)
block3.fill("blue")
block4 = pygame_quick.surface(10, 100)
block4.fill("tomato")

# Note: window does not need to be created first
window = pygame_quick.window(600, 400)

while window.active():
    for type, value in window.events():
        if type is pygame_quick.mouse_down:
            if value.button is pygame_quick.left_button:
                print("Mouse click at", value.position, "using left button")
            elif value.button is pygame_quick.right_button:
                print("Mouse click at", value.position, "using right button")
            elif value.button is pygame_quick.middle_button:
                print("Mouse click at", value.position, "using middle button")
            elif value.is_scroll():
                print("Mouse scroll at", value.position, "using direction", value.scroll_direction)

        elif type is pygame_quick.key_down:
            if value == "<Left>":
                block_x -= 1
            elif value == "<Right>":
                block_x += 1
            elif value == "<Up>":
                block_y -= 1
            elif value == "<Down>":
                block_y += 1
            elif value == "b":
                background_color = random.choice(list(pygame_quick.color.colors))
            else:
                print("Key", repr(value), "pressed")

    window.fill(background_color)
    window.draw_rectangle(color="blue", x=100, y=100, width=100, height=100)
    window.draw_circle(color="green", x=500, y=300, radius=100)

    window.draw_line(start=window.topleft, end=window.bottomright, color="brown")
    window.draw_hollow_rectangle(color="red", x=100, y=100, width=100, height=100, thickness=10)
    window.draw_hollow_circle(color="red", x=500, y=300, radius=100, thickness=10)

    block.draw(window, block_x, block_y)
    block2.draw_by_center(window, pygame_quick.mouse_position())
    block3.draw_by_center(window, window.center)
    block4.draw(window, (10, 20))
    block4.draw_by_bottomright(window, window.bottomright)

    window.update()

