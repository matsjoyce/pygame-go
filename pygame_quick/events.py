import enum
import pygame


class EventType(enum.Enum):
    quit = "quit"
    key_down = "keypress"
    mouse_down = "mouse"
    mouse_motion = "mouse_motion"


class Button(enum.Enum):
    left = "left"
    middle = "middle"
    right = "right"
    vertical_scroll = "vertical_scroll"
    horizontal_scroll = "horizontal_scroll"


class VerticalScrollDirection(enum.Enum):
    up = "up"
    down = "down"


class HorizontalScrollDirection(enum.Enum):
    left = "left"
    right = "right"


class MouseEvent:
    def __init__(self, pos, button, scroll_direction=None):
        self.position = pos
        self.x, self.y = pos
        self.button = button
        self.scroll_direction = scroll_direction

    def is_scroll(self):
        return self.scroll_direction is not None

    def is_click(self):
        return not self.is_scroll()


class MouseMotionEvent:
    def __init__(self, pos, rel, buttons):
        self.to_position = pos
        self.to_x, self.to_y = pos
        self.moved_by = rel
        self.moved_by_x, self.moved_by_y = rel
        self.from_x = self.to_x - self.moved_by_x
        self.from_y = self.to_y - self.moved_by_y
        self.from_position = self.from_x, self.from_y
        self.buttons = buttons

    def is_pressed(self, button):
        return button in self.buttons


def translate_button(button):
    if button == 1:
        return Button.left, None
    elif button == 2:
        return Button.middle, None
    elif button == 3:
        return Button.right, None
    elif button == 4:
        return Button.vertical_scroll, VerticalScrollDirection.up
    elif button == 5:
        return Button.vertical_scroll, VerticalScrollDirection.down
    elif button == 6:
        return Button.horizontal_scroll, HorizontalScrollDirection.left
    elif button == 7:
        return Button.horizontal_scroll, HorizontalScrollDirection.right


def expand_event(event):
    if event.type == pygame.QUIT:
        return EventType.quit, None

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            key_value = "\n"  # pygame uses "\r", which is less pythonic
        elif event.unicode:
            key_value = event.unicode
        elif event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
            key_value = "<Shift>"
        elif event.key in (pygame.K_LALT, pygame.K_RALT):
            key_value = "<Alt>"
        elif event.key in (pygame.K_LCTRL, pygame.K_RCTRL):
            key_value = "<Ctrl>"
        elif event.key in (pygame.K_LSUPER, pygame.K_RSUPER):
            key_value = "<Super>"
        elif event.key in (pygame.K_LMETA, pygame.K_RMETA):
            key_value = "<Meta>"
        elif event.key == pygame.K_LEFT:
            key_value = "<Left>"
        elif event.key == pygame.K_RIGHT:
            key_value = "<Right>"
        elif event.key == pygame.K_UP:
            key_value = "<Up>"
        elif event.key == pygame.K_DOWN:
            key_value = "<Down>"
        else:
            return None, None
        return EventType.key_down, key_value

    elif event.type == pygame.MOUSEMOTION:
        l, m, r = event.buttons
        buttons = set()
        if l:
            buttons.add(Button.left)
        if m:
            buttons.add(Button.middle)
        if r:
            buttons.add(Button.right)
        return EventType.mouse_motion, MouseMotionEvent(event.pos, event.rel, buttons)

    elif event.type == pygame.MOUSEBUTTONDOWN:
        return EventType.mouse_down, MouseEvent(event.pos, *translate_button(event.button))

    elif event.type in (pygame.ACTIVEEVENT, pygame.KEYUP,
                        pygame.MOUSEBUTTONUP, pygame.JOYAXISMOTION,
                        pygame.JOYBALLMOTION, pygame.JOYHATMOTION,
                        pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN,
                        pygame.VIDEORESIZE, pygame.VIDEOEXPOSE,
                        pygame.USEREVENT):
        return None, None  # not handled
    else:
        raise ValueError("Unknown event type")
    return None, None
