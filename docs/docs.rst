Documentation
=============

A note on notation
------------------

In the following documentation, the following syntax is used for method signatures::

    func(a, <size>, *, <align>, b, [thickness=0, <color="white">])

This means that:

 - ``a`` is a non-optional argument that can be given positionally.
 - ``<size>`` means a size-like (more on that later) argument, which can be given positionally.
 - Any arguments after ``*`` have to be given using keyword arguments.
 - ``<align>`` means an align-like argument that must be given using keyword arguments.
 - ``b`` is a keyword-only argument that must be given.
 - If a parameter is inside square brackets, it is optional and a default used if you do not pass it. If an argument is not inside square brackets it must be given, regardless of whether it is keyword-only or not.
 - ``thickness`` is a keyword-only argument that is optional, and has default ``0``.
 - ``<color>`` is a color-like argument that is optional, and has default ``"white"``.

``<x>``-like arguments:

 - ``<position>``
     - Can be given as either ``x`` and ``y`` or ``position``.
     - ``x`` and ``y`` must be ``int``\ s or ``float``\ s.
     - ``position`` must be a 2-``tuple`` of ``int``\ s or ``float``\ s.
 - ``<size>``
     - Can be given as either ``width`` and ``height`` or ``size``.
     - ``width`` and ``height`` must be ``int``\ s or ``float``\ s.
     - ``size`` must be a 2-``tuple`` of ``int``\ s or ``float``\ s.
 - ``<align>``
     - Can be given as either ``align`` or ``align_x`` and ``align_y``.
     - ``align`` can be a position or one of :data:`topleft`, :data:`topright`, :data:`bottomleft`, :data:`bottomright` or :data:`center`.
     - ``align_x`` and ``align_y`` must be ``int``\ s or ``float``\ s.
 - ``<color>``
     - Can be given as either ``color`` or ``r``, ``g``, ``b`` and optionally ``a``
     - ``color`` must either be a ``color``, a ``str`` or a 3-``tuple`` of of ``int``\ s or ``float``\ s.
     - If ``color`` is a ``str`` the name is looked up in ``color.colors`` and an error raised if it is not found.
     - ``r``, ``g``, ``b`` and optionally ``a`` must be ``int``\ s or ``float``\ s in the range 0-255. ``a`` is the transparency.

Constants
---------

.. data:: left_button
          middle_button
          right_button

    Enumeration representing buttons, used in :class:`ClickEvent` and :func:`is_mouse_pressed`.

.. data:: up_scroll
          down_scroll
          left_scroll
          right_scroll

    Enumeration representing scroll directions, used in :class:`ScrollEvent`.

.. data:: topleft
          topright
          bottomleft
          bottomright
          center

    Enumeration representing alignment, use for ``<align>`` parameters.

.. data:: color_names

    List of all the color names recognised.

.. data:: color.colors

    A dictionary of color names to :class:`color`\ s.


Classes
-------

.. class:: image

    .. method:: __init__(fname)

        :param fname: Path to image file.
        :type fname: str or pathlib.Path

        Load an image from a file.

        .. warning:: A window must be created before this function is called! A :class:`RuntimeError` will be raised otherwise.

    .. method:: __init__(<size>, *, [<color="transparent">])

        Create a new image of size ``<size>``. If ``<color>`` is given, it will be filled with that color, otherwise it will be transparent.

    .. attribute:: size

        Type: 2-tuple of :class:`int`

        The width and height of the image. This attribute is not settable.

    .. attribute:: width

        Type: :class:`int`

        The width of the image. This attribute is not settable.

    .. attribute:: height

        Type: :class:`int`

        The height of the image. This attribute is not settable.

    .. attribute:: center

        Type: 2-tuple of :class:`int`

        The position at the center of the image. This attribute can be used as a ``<position>`` or ``<align>``. This attribute is not settable.

    .. attribute:: topleft

        Type: 2-tuple of :class:`int`

        The position at the top-left of the image. This attribute can be used as a ``<position>`` or ``<align>``. This attribute is not settable.

    .. attribute:: topright

        Type: 2-tuple of :class:`int`

        The position at the top-right of the image. This attribute can be used as a ``<position>`` or ``<align>``. This attribute is not settable.

    .. attribute:: bottomleft

        Type: 2-tuple of :class:`int`

        The position at the bottom-left of the image. This attribute can be used as a ``<position>`` or ``<align>``. This attribute is not settable.

    .. attribute:: bottomright

        Type: 2-tuple of :class:`int`

        The position at the bottom-right of the image. This attribute can be used as a ``<position>`` or ``<align>``. This attribute is not settable.

    .. method:: copy()

        :rtype: image

        Returns a copy of the image. Changes to the image will not affect the copy.

    .. method:: fill(<color>)

        :rtype: None

        The entire image is set to ``<color>``.

    .. method:: draw_image(source, <position>, *, [<align=topleft>])

        :rtype: None

        Draw ``source`` onto this image such that the point on the ``source`` indicated by ``<align>`` is at ``<position>``. E.g.::

            image.draw_image(other, image.bottomright, align=bottomright)

        Will draw ``other`` onto ``image`` such that the bottom-right of ``other`` is at the bottom-right of ``image``.

    .. method:: draw_rect(*, <position>, <size>, <color>, [<align=topleft>])

        :rtype: None

        Draw a rectangle of color ``<color>`` and size ``<size>`` such that ``<align>`` is at ``<position>``. The ``<align>`` works the same as for :func:`draw_image`.

    .. method:: draw_hollow_rect(*, <position>, <size>, <color>, [thickness=1, <align=topleft>])

        :rtype: None

        Draw a border of thickness ``thickness`` and color ``<color>`` in the rectangle defined by ``<size>``, ``<position>`` and ``<align>``. The rectangle is defined in the same way as for :func:`draw_rect`.

    .. method:: draw_circle(*, <position>, <color>, radius)

        :rtype: None

        Draw a circle of color ``<color>`` with radius ``radius`` with its center at ``<position>``.

    .. method:: draw_hollow_circle(*, <position>, <color>, radius, [thickness=1])

        :rtype: None

        Draw a circular border of color ``<color>`` with radius ``radius`` and thickness ``thickness`` with its center at ``<position>``.


    .. method:: draw_ellipse(*, <position>, <color>, <size>)

        :rtype: None

        Draw a ellipse of color ``<color>`` with radius ``radius`` with its center at ``<position>``. Its width and height is taken from ``<size>``.


    .. method:: draw_hollow_ellipse(*, <position>, <color>, <size>, [thickness=1])

        :rtype: None

        Draw a ellipse-shaped border of color ``<color>`` with radius ``radius`` and thickness ``thickness`` with its center at ``<position>``. Its width and height is taken from ``<size>``.


    .. method:: draw_line(*, <start>, <end>, <color>, [thickness=1])

        :rtype: None

        Draw a line from ``<start>`` to ``<end>`` with color ``<color>`` and thickness ``thickness``. For ``<start>``, provide ``start`` or ``start_x`` and ``start_y``. For ``<end>``, provide ``end`` or ``end_x`` and ``end_y``. ``<start>`` and ``<end>`` work the same as ``<position>`` in every other way.

    .. method:: draw_text(*, text, <position>, <color>, [text, size=30, font=None, bold=False, italic=False, <align=topleft>])

        :rtype: None

        Draw text ``text`` in color ``<color>`` at ``<position>``. ``<align>`` works the same as for :func:`draw_rect`. ``size`` is the height of the font. If ``font`` is ``None``, the default font will be used. Otherwise a font called ``font`` will be searched for and a :class:`ValueError` raised if it cannot be found. ``bold`` and ``italic`` set the function to use the bold and italic variants of the font.

        .. note:: ``bold`` and ``italic`` may not work on all fonts, especially the default font. If you cannot see any change when using ``bold`` or ``italic``, try changing to a different font.

    .. method:: flip([vertical=False, horizontal=False])

        :rtype: None

        Flip the image vertically if ``vertical`` is ``True`` and horizontally if ``horizontal`` is ``True``.

    .. method:: rotate(angle)

        :rtype: None

        Rotate the image by ``angle`` degrees clockwise.

    .. method:: scale(times)

        :rtype: None

        Enlarge the image by factor ``times``. The image will then have a width of ``times * old_width`` and a height of ``times * old_height``.

    .. method:: color_at(<position>)

        :rtype: color

        Returns the color of the pixel at ``<position>``


.. class:: window

    Bases: :class:`image`

    .. method:: __init__(<size>, *, [<color="white">, frame_rate=20, autoquit=True, title="pygame-go", icon=None])

        Create the window with the size ``<size>``. If ``<color>`` is given, the window will be filled with that color, otherwise it is filled with white. ``frame_rate`` is the number of updates per second, which is controlled during the :func:`update` method call. If ``autoquit`` is ``True``, then quit events will be processed automatically and :func:`active` will return ``False`` without any event processing by the user. If ``autoquit`` is ``False``, the quit events will be accessible though :func:`events`. ``title`` will be used to set the window title, see :attr:`title`. ``icon`` will be used to set the window icon, see :attr:`icon`.

    .. method:: active()

        :rtype: bool

        Returns whether the window has quit or not. This should be used in your main loop so that your program exits when the user presses the quit button.

    .. method:: stop()

        :rtype: None

        Makes :func:`active` return ``False``, stopping the program.

    .. method:: update()

        :rtype: None

        Updates the window, showing the graphics on the window to the user. This function will then delay by the correct amount of time to maintain the correct frame rate.

    .. method:: loop_forever()

        :rtype: None

        Keep updating the window until the user quits. As no event handling can be done in this function, only use it if you only want to show a static image.

    .. method:: has_events()

        :rtype: bool

        Returns ``True`` if there are unprocessed events.

    .. method:: next_event()

        :rtype: Event

        Returns the next event to be processed. Raises a :class:`ValueError` if there are no more events.

    .. method:: events()

        :rtype: Iterable[Event]

        Returns an iterator that yields events in the queue until the queue is empty. This is the preferable way to access events.

    .. attribute:: title

        Type: :class:`str`

        The title of the window. This attribute is settable, and setting a new value will change the window title.

    .. attribute:: icon

        Type: :class:`image`

        The icon of the window, used in the task bar. This attribute is settable, and setting a new value will change the window icon.

        .. note:: May not work with all DEs


.. class:: sound

    .. method:: __init__(fname)

        :param fname: Path to sound file.
        :type fname: str or pathlib.Path

        Load an sound from a file.

        .. note:: Only ``.ogg`` and ``.wav`` files can be loaded. This may change in future releases.

    .. method:: play([times=1, forever=False])

        :rtype: None

        Play the sound, repeating it ``times`` times. If ``forever`` is ``True``, the sound will repeat until :func:`stop` is called.

    .. method:: stop()

        :rtype: None

        Stop the sound. This will also unpause the sound.

    .. method:: pause()

        :rtype: None

        Pause the sound if it is not already paused. It can be resumed with :func:`unpause`.

    .. method:: unpause()

        :rtype: None

        If the sound has been paused, unpause it.

    .. method:: is_playing()

        :rtype: bool

        Returns whether the sound is currently playing.

    .. method:: is_paused()

        :rtype: bool

        Returns whether the sound is currently paused.

    .. attribute:: length

        Type: :class:`float`

        The length of the sound in seconds. This attribute is not settable.

    .. attribute:: volume

        Type: :class:`float`

        The volume of the sound. This attribute can be set in order to change the volume it is played at.



.. class:: color

    .. method:: __init__(<color>)

        Create a new color.

    .. classmethod:: fromhex(value)

        Create a color from a HTML-style color.

    .. attribute:: r

        Type: :class:`int`

        The red component of the color. It will be in the range 0-255. This attribute is settable.

    .. attribute:: g

        Type: :class:`int`

        The green component of the color. It will be in the range 0-255. This attribute is settable.
    .. attribute:: b

        Type: :class:`int`

        The blue component of the color. It will be in the range 0-255. This attribute is settable.

    .. attribute:: transparency

        Type: :class:`int`

        The transparency component of the color. It will be in the range 0-255. This attribute is settable.

    .. attribute:: hex

        Type: :class:`str`

        The HTML-style hex representation of this color.  This attribute is not settable.


.. class:: Event

    .. note:: This type should not be created. Rather, use :meth:`window.events`.

    .. method:: is_mouse_press()

        :rtype: bool

        Returns whether this event is a :class:`ClickEvent`.

    .. method:: is_mouse_scroll()

        :rtype: bool

        Returns whether this event is a :class:`ScrollEvent`.

    .. method:: is_quit()

        :rtype: bool

        Returns whether this event is a :class:`QuitEvent`.

    .. method:: is_mouse_motion()

        :rtype: bool

        Returns whether this event is a :class:`MotionEvent`.

    .. method:: is_key()

        :rtype: bool

        Returns whether this event is a :class:`KeyEvent`.


.. class:: ClickEvent

    Bases: :class:`Event`

    .. note:: This type should not be created. Rather, use :meth:`window.events`.

    .. attribute:: position

        Type: 2-tuple of :class:`int`

        The position of the click.

    .. attribute:: x

        Type: :class:`int`

        The x-coordinate of the click.

    .. attribute:: y

        Type: :class:`int`

        The y-coordinate of the click.

    .. attribute:: button

        Type: One of :data:`left_button`, :data:`right_button` or :data:`middle_button`

        The button that was pressed down.


.. class:: ScrollEvent

    Bases: :class:`Event`

    .. note:: This type should not be created. Rather, use :meth:`window.events`.

    .. attribute:: position

        Type: 2-tuple of :class:`int`

        The position of the scroll.

    .. attribute:: x

        Type: :class:`int`

        The x-coordinate of the scroll.

    .. attribute:: y

        Type: :class:`int`

        The y-coordinate of the scroll.

    .. attribute:: direction

        Type: One of :data:`up_scroll`, :data:`down_scroll`, :data:`left_scroll` or :data:`right_scroll`

        The direction of the scroll.


.. class:: MotionEvent

    Bases: :class:`Event`

    .. note:: This type should not be created. Rather, use :meth:`window.events`.

    .. attribute:: start

        Type: 2-tuple of :class:`int`

        The position the mouse started moving from.

    .. attribute:: start_x

        Type: :class:`int`

        The x-coordinate of :attr:`start`.

    .. attribute:: start_y

        Type: :class:`int`

        The y-coordinate of :attr:`start`.

    .. attribute:: end

        Type: 2-tuple of :class:`int`

        The position the mouse moved to.

    .. attribute:: end_x

        Type: :class:`int`

        The x-coordinate of :attr:`end`.

    .. attribute:: end_y

        Type: :class:`int`

        The y-coordinate of :attr:`end`.

    .. attribute:: moved_by

        Type: 2-tuple of :class:`int`

        The amount of movement in the x and y direction

    .. attribute:: moved_by_x

        Type: :class:`int`

        The amount of movement in the x direction.

    .. attribute:: moved_by_y

        Type: :class:`int`

        The amount of movement in the y direction.

    .. attribute:: buttons

        Type: :class:`set` containing some of :data:`left_button`, :data:`right_button` and :data:`middle_button`

        The buttons that were pressed during the motion. See :func:`is_pressed`.

    .. method:: is_pressed([button=None)

        :rtype: bool

        If ``button`` is one of :data:`left_button`, :data:`right_button` or :data:`middle_button`, returns ``True`` if that button was pressed during the motion. If ``button`` is ``None``, return ``True`` if any buttons were pressed during the motion.


.. class:: KeyEvent

    Bases: :class:`Event`

    .. note:: This type should not be created. Rather, use :meth:`window.events`.

    .. attribute:: key

        Type: :class:`str`

        The key that was pressed. It can either be a single ASCII character or a modifier / non-printable key like ``<Shift>`` or ``<Ctrl>``. See ``pygame_go/events.py`` for the full listing.

.. class:: QuitEvent

    Bases: :class:`Event`

    .. note:: This type should not be created. Rather, use :meth:`window.events`.


Other functions
---------------

.. function:: mouse_position()

    :rtype: 2-tuple of int

    Returns the current mouse position.

.. function:: set_mouse_position(<position>)

    :rtype: None

    Sets the current mouse position.

.. function:: is_key_pressed(key)

    :rtype: bool

    Returns whether the key ``key`` is currently pressed. ``key`` should be in the same form as for :class:`KeyEvent`.

.. function:: is_button_pressed(button)

    :rtype: bool

    Returns whether the button ``button`` is currently pressed. ``button`` should be one of :data:`left_button`, :data:`right_button` or :data:`middle_button`.
