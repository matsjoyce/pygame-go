"""
pygame-quick - A simplified version of pygame for use in teaching
Copyright (C) 2017 Matthew Joyce (matsjoyce@gmail.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the Lesser GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
Lesser GNU General Public License for more details.

You should have received a copy of the Lesser GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import enum
import pygame

KEY_MAPPING = {pygame.K_RETURN: "\n",
               pygame.K_LSHIFT: "<Shift>",
               pygame.K_RSHIFT: "<Shift>",
               pygame.K_LALT: "<Alt>",
               pygame.K_RALT: "<Alt>",
               pygame.K_LCTRL: "<Ctrl>",
               pygame.K_RCTRL: "<Ctrl>",
               pygame.K_LSUPER: "<Super>",
               pygame.K_RSUPER: "<Super>",
               pygame.K_LMETA: "<Meta>",
               pygame.K_RMETA: "<Meta>",
               pygame.K_LEFT: "<Left>",
               pygame.K_RIGHT: "<Right>",
               pygame.K_UP: "<Up>",
               pygame.K_DOWN: "<Down>",
               pygame.K_ESCAPE: "<Escape>",
               pygame.K_INSERT: "<Insert>",
               pygame.K_PAGEUP: "<PageUp>",
               pygame.K_PAGEDOWN: "<PageDown>",
               pygame.K_DELETE: "<Delete>",
               pygame.K_HOME: "<Home>",
               pygame.K_PRINT: "<PrintScreen>",
               pygame.K_END: "<End>",
               pygame.K_SCROLLOCK: "<ScrollLock>",
               pygame.K_BREAK: "<Break>",
               pygame.K_PAUSE: "<Pause>",
               pygame.K_SYSREQ: "<SysReq>",
               pygame.K_MENU: "<Menu>",
               pygame.K_HELP: "<Help>",
               pygame.K_F1: "<F1>",
               pygame.K_F2: "<F2>",
               pygame.K_F3: "<F3>",
               pygame.K_F4: "<F4>",
               pygame.K_F5: "<F5>",
               pygame.K_F6: "<F6>",
               pygame.K_F7: "<F7>",
               pygame.K_F8: "<F8>",
               pygame.K_F9: "<F9>",
               pygame.K_F10: "<F10>",
               pygame.K_F11: "<F11>",
               pygame.K_F12: "<F12>",
               }


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
        self.end = pos
        self.end_x, self.end_y = pos
        self.moved_by = rel
        self.moved_by_x, self.moved_by_y = rel
        self.start_x = self.end_x - self.moved_by_x
        self.start_y = self.end_y - self.moved_by_y
        self.start = self.start_x, self.start_y
        self.buttons = buttons

    def is_pressed(self, button=None):
        if button is None:
            return bool(self.buttons)
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


FUNCTION_KEYS = []


def expand_event(event):
    if event.type == pygame.QUIT:
        return EventType.quit, None

    elif event.type == pygame.KEYDOWN:
        if event.key in KEY_MAPPING:
            key_value = KEY_MAPPING[event.key]
        elif event.unicode:
            key_value = event.unicode
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
