import pygame_quick

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

        elif type is pygame_quick.mouse_motion:
            print("Mouse moved from", value.from_position, "to", value.to_position)

        elif type is pygame_quick.key_down:
            print("Key", repr(value), "pressed")

    window.update()
