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

import pygame

from . import image, events
from .shortcuts import with_pygame_inited, extract_size_args


class window(image.image):
    @with_pygame_inited
    def __init__(self, *args, framerate=20, autoquit=True, **kwargs):
        size = extract_size_args(args, kwargs)
        self._surf = pygame.display.set_mode(size)
        self.framerate = framerate
        self._clock = pygame.time.Clock()
        self._active = True
        self._events = []
        self._autoquit = autoquit
        self.framenumber = 0

    def active(self):
        return self._active

    def stop(self):
        self._active = False

    def update(self):
        pygame.display.flip()
        self._clock.tick(self.framerate)
        self.framenumber += 1
        self._preprocess_events()

    def _preprocess_events(self):
        self._events.clear()
        for event in pygame.event.get():
            type, info = events.expand_event(event)
            if type == events.EventType.quit and self._autoquit:
                self.stop()
            elif type is None:
                continue
            else:
                self._events.append((type, info))

    def has_events(self):
        return bool(self._events)

    def next_event(self):
        if self._events:
            return self._events.pop(0)
        raise ValueError("There are no more events")

    def events(self, *types):
        i = 0
        while i < len(self._events):
            type, value = self._events[i]
            if type in types or not types:
                yield self._events.pop(i)
            else:
                i += 1
