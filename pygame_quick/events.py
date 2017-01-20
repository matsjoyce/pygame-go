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
        self.end_position = pos
        self.end_x, self.end_y = pos
        self.moved_by = rel
        self.moved_by_x, self.moved_by_y = rel
        self.start_x = self.end_x - self.moved_by_x
        self.start_y = self.end_y - self.moved_by_y
        self.start_position = self.start_x, self.start_y
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


FUNCTION_KEYS = [pygame.K_F1, pygame.K_F2, pygame.K_F3,
                 pygame.K_F4, pygame.K_F5, pygame.K_F6,
                 pygame.K_F7, pygame.K_F8, pygame.K_F9,
                 pygame.K_F10, pygame.K_F11, pygame.K_F12]


def expand_event(event):
    if event.type == pygame.QUIT:
        return EventType.quit, None

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            key_value = "\n"  # pygame uses "\r", which is less pythonic
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
        elif event.key == pygame.K_ESCAPE:
            key_value = "<Escape>"
        elif event.key == pygame.K_INSERT:
            key_value = "<Insert>"
        elif event.key == pygame.K_PAGEUP:
            key_value = "<PageUp>"
        elif event.key == pygame.K_PAGEDOWN:
            key_value = "<PageDown>"
        elif event.key == pygame.K_DELETE:
            key_value = "<Delete>"
        elif event.key == pygame.K_HOME:
            key_value = "<Home>"
        elif event.key == pygame.K_PRINT:
            key_value = "<PrintScreen>"
        elif event.key == pygame.K_END:
            key_value = "<End>"
        elif event.key == pygame.K_SCROLLOCK:
            key_value = "<ScrollLock>"
        elif event.key == pygame.K_BREAK:
            key_value = "<Break>"
        elif event.key == pygame.K_PAUSE:
            key_value = "<Pause>"
        elif event.key == pygame.K_SYSREQ:
            key_value = "<SysReq>"
        elif event.key == pygame.K_MENU:
            key_value = "<Menu>"
        elif event.key == pygame.K_HELP:
            key_value = "<Help>"
        elif event.key in FUNCTION_KEYS:
            key_value = "<F{}>".format(FUNCTION_KEYS.index(event.key) + 1)
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
