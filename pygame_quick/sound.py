import pathlib
import pygame
import os

from .shortcuts import with_pygame_inited


class sound:
    @with_pygame_inited
    def __init__(self, fname):
        path = pathlib.Path(os.path.expanduser(fname)).resolve()
        if not path.exists():
            raise FileNotFoundError("The file '{}' does not exist, maybe you spelt the name wrong?".format(path))
        try:
            self._sound = pygame.mixer.Sound(str(path))
        except pygame.error:
            raise IOError("Could not load '{}', are you sure it's an sound file (.ogg or .wav)?".format(path))

    def play(self, times=1, forever=False):
        if forever:
            self._sound.play(-1)
        else:
            self._sound.play(times - 1)

    def stop(self):
        self._sound.stop()

    @property
    def volume(self):
        return self._sound.get_volume()

    @volume.setter
    def volume(self, value):
        self._sound.set_volume(value)

    @property
    def length(self):
        return self._sound.get_length()
