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
import warnings


KEY_MAPPING = {pygame.K_BACKSPACE: "\b",
               pygame.K_TAB: "\t",
               pygame.K_CLEAR: "<Clear>",
               pygame.K_RETURN: "\n",
               pygame.K_PAUSE: "<Pause>",
               pygame.K_ESCAPE: "<Escape>",
               pygame.K_SPACE: " ",
               pygame.K_EXCLAIM: "!",
               pygame.K_QUOTEDBL: "\"",
               pygame.K_HASH: "#",
               pygame.K_DOLLAR: "$",
               pygame.K_AMPERSAND: "&",
               pygame.K_QUOTE: "'",
               pygame.K_LEFTPAREN: "(",
               pygame.K_RIGHTPAREN: ")",
               pygame.K_ASTERISK: "*",
               pygame.K_PLUS: "+",
               pygame.K_COMMA: ",",
               pygame.K_MINUS: "-",
               pygame.K_PERIOD: ".",
               pygame.K_SLASH: "/",
               pygame.K_0: "0",
               pygame.K_1: "1",
               pygame.K_2: "2",
               pygame.K_3: "3",
               pygame.K_4: "4",
               pygame.K_5: "5",
               pygame.K_6: "6",
               pygame.K_7: "7",
               pygame.K_8: "8",
               pygame.K_9: "9",
               pygame.K_COLON: ":",
               pygame.K_SEMICOLON: ";",
               pygame.K_LESS: "<",
               pygame.K_EQUALS: "=",
               pygame.K_GREATER: ">",
               pygame.K_QUESTION: "?",
               pygame.K_AT: "@",
               pygame.K_LEFTBRACKET: "[",
               pygame.K_BACKSLASH: "\\",
               pygame.K_RIGHTBRACKET: "]",
               pygame.K_CARET: "^",
               pygame.K_UNDERSCORE: "_",
               pygame.K_BACKQUOTE: "`",
               pygame.K_a: "a",
               pygame.K_b: "b",
               pygame.K_c: "c",
               pygame.K_d: "d",
               pygame.K_e: "e",
               pygame.K_f: "f",
               pygame.K_g: "g",
               pygame.K_h: "h",
               pygame.K_i: "i",
               pygame.K_j: "j",
               pygame.K_k: "k",
               pygame.K_l: "l",
               pygame.K_m: "m",
               pygame.K_n: "n",
               pygame.K_o: "o",
               pygame.K_p: "p",
               pygame.K_q: "q",
               pygame.K_r: "r",
               pygame.K_s: "s",
               pygame.K_t: "t",
               pygame.K_u: "u",
               pygame.K_v: "v",
               pygame.K_w: "w",
               pygame.K_x: "x",
               pygame.K_y: "y",
               pygame.K_z: "z",
               pygame.K_DELETE: "<Delete>",
               pygame.K_KP0: "0",
               pygame.K_KP1: "1",
               pygame.K_KP2: "2",
               pygame.K_KP3: "3",
               pygame.K_KP4: "4",
               pygame.K_KP5: "5",
               pygame.K_KP6: "6",
               pygame.K_KP7: "7",
               pygame.K_KP8: "8",
               pygame.K_KP9: "9",
               pygame.K_KP_PERIOD: ".",
               pygame.K_KP_DIVIDE: "/",
               pygame.K_KP_MULTIPLY: "*",
               pygame.K_KP_MINUS: "-",
               pygame.K_KP_PLUS: "+",
               pygame.K_KP_ENTER: "\n",
               pygame.K_KP_EQUALS: "=",
               pygame.K_UP: "<Up>",
               pygame.K_DOWN: "<Down>",
               pygame.K_RIGHT: "<Right>",
               pygame.K_LEFT: "<Left>",
               pygame.K_INSERT: "<Insert>",
               pygame.K_HOME: "<Home>",
               pygame.K_END: "<End>",
               pygame.K_PAGEUP: "<PageUp>",
               pygame.K_PAGEDOWN: "<PageDown>",
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
               pygame.K_F13: "<F13>",
               pygame.K_F14: "<F14>",
               pygame.K_F15: "<F15>",
               pygame.K_NUMLOCK: "<NumLock>",
               pygame.K_CAPSLOCK: "<CapsLock>",
               pygame.K_SCROLLOCK: "<ScrollLock>",
               pygame.K_RSHIFT: "<Shift>",
               pygame.K_LSHIFT: "<Shift>",
               pygame.K_RCTRL: "<Ctrl>",
               pygame.K_LCTRL: "<Ctrl>",
               pygame.K_RALT: "<Alt>",
               pygame.K_LALT: "<Alt>",
               pygame.K_RMETA: "<Meta>",
               pygame.K_LMETA: "<Meta>",
               pygame.K_LSUPER: "<Super>",
               pygame.K_RSUPER: "<Super>",
               pygame.K_MODE: "<Mode>",
               pygame.K_HELP: "<Help>",
               pygame.K_PRINT: "<Print>",
               pygame.K_SYSREQ: "<SysReq>",
               pygame.K_BREAK: "<Break>",
               pygame.K_MENU: "<Menu>",
               pygame.K_POWER: "<Power>",
               pygame.K_EURO: "<Euro>"
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


class ScrollDirection(enum.Enum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"


class Event:
    def is_mouse_press(self):
        return False

    def is_mouse_scroll(self):
        return False

    def is_quit(self):
        return False

    def is_mouse_motion(self):
        return False

    def is_key(self):
        return False


class ClickEvent(Event):
    def __init__(self, pos, button):
        self.position = pos
        self.x, self.y = pos
        self.button = button

    def __repr__(self):
        return "<Mouse click at {} with {} button>".format(self.position, self.button.name)

    def is_mouse_press(self):
        return True


class ScrollEvent(Event):
    def __init__(self, pos, direction):
        self.position = pos
        self.x, self.y = pos
        self.direction = direction

    def __repr__(self):
        return "<Scroll {} at {}>".format(self.direction.name, self.position)

    def is_mouse_scroll(self):
        return True


class MotionEvent(Event):
    def __init__(self, pos, rel, buttons):
        self.end = pos
        self.end_x, self.end_y = pos
        self.moved_by = rel
        self.moved_by_x, self.moved_by_y = rel
        self.start_x = self.end_x - self.moved_by_x
        self.start_y = self.end_y - self.moved_by_y
        self.start = self.start_x, self.start_y
        self.buttons = buttons

    def __repr__(self):
        return "<Mouse motion from {} to {}>".format(self.start, self.end)

    def is_pressed(self, button=None):
        if button is None:
            return bool(self.buttons)
        return button in self.buttons

    def is_mouse_motion(self):
        return True


class MagicKeyWrapper:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if type(other) is not str:
            return False
        if other.startswith("<") and other.endswith(">"):
            if other not in set(KEY_MAPPING.values()):
                warnings.warn("Key {} does not appear to exist, maybe a typo?".format(other))
        elif len(other) > 1:
            warnings.warn("Key {} does not seem to be generatable, maybe a typo?".format(other))
        return self.value == other

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)

    def __len__(self):
        return len(self.value)

    def __contains__(self, item):
        return item in self.value

    def __getitem__(self, key):
        return self.value[key]


class KeyEvent(Event):
    def __init__(self, key):
        self._key = key

    def __repr__(self):
        return "<Key {!r} pressed>".format(self.key)

    @property
    def key(self):
        return MagicKeyWrapper(self._key)

    def is_key(self):
        return True


class QuitEvent(Event):
    def is_quit(self):
        return True

    def __repr__(self):
        return "<Quit>"


def translate_button(button):
    if button == 1:
        return Button.left
    elif button == 2:
        return Button.middle
    elif button == 3:
        return Button.right
    elif button == 4:
        return ScrollDirection.up
    elif button == 5:
        return ScrollDirection.down
    elif button == 6:
        return ScrollDirection.left
    elif button == 7:
        return ScrollDirection.right


def expand_event(event):
    if event.type == pygame.QUIT:
        return QuitEvent()

    elif event.type == pygame.KEYDOWN:
        if event.unicode and event.unicode.isprintable():
            key_value = event.unicode
        elif event.key in KEY_MAPPING:
            key_value = KEY_MAPPING[event.key]
        else:
            warnings.warn("Unknown key {}".format(event.key))
            return None
        return KeyEvent(key_value)

    elif event.type == pygame.MOUSEMOTION:
        l, m, r = event.buttons
        buttons = set()
        if l:
            buttons.add(Button.left)
        if m:
            buttons.add(Button.middle)
        if r:
            buttons.add(Button.right)
        return MotionEvent(event.pos, event.rel, buttons)

    elif event.type == pygame.MOUSEBUTTONDOWN:
        button = translate_button(event.button)
        if button in Button:
            return ClickEvent(event.pos, button)
        return ScrollEvent(event.pos, button)

    elif event.type in (pygame.ACTIVEEVENT, pygame.KEYUP,
                        pygame.MOUSEBUTTONUP, pygame.JOYAXISMOTION,
                        pygame.JOYBALLMOTION, pygame.JOYHATMOTION,
                        pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN,
                        pygame.VIDEORESIZE, pygame.VIDEOEXPOSE,
                        pygame.USEREVENT):
        return None  # not handled
    else:
        raise ValueError("Unknown event type")
    return None
