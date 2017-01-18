import pygame_quick

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

        elif type is pygame_quick.mouse_motion_event:
            print("Mouse moved from", value.from_position, "to", value.to_position)

        elif type is pygame_quick.key_event:
            print("Key", repr(value), "pressed")
        else:
            print(type)

    screen.update()
