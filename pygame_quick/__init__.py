from .screen import Screen
from .surface import Surface
from .events import EventType, Button, VerticalScrollDirection, HorizontalScrollDirection


def extract_values(enum, suffix, scope):
    for value in enum:
        scope[value.name + suffix] = value


# provide shortcuts to the enum values
extract_values(EventType, "_event", locals())
extract_values(Button, "_button", locals())
extract_values(VerticalScrollDirection, "_scroll", locals())
extract_values(HorizontalScrollDirection, "_scroll", locals())

del extract_values
