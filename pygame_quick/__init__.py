from .window import window
from .surface import surface
from .events import EventType, Button, VerticalScrollDirection, HorizontalScrollDirection
from .input import mouse_position, set_mouse_position
from .color import color


def extract_values(enum, suffix, scope):
    for value in enum:
        scope[value.name + suffix] = value


# provide shortcuts to the enum values
extract_values(EventType, "", locals())
extract_values(Button, "_button", locals())
extract_values(VerticalScrollDirection, "_scroll", locals())
extract_values(HorizontalScrollDirection, "_scroll", locals())

del extract_values
