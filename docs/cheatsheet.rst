Cheatsheet
==========

How do I import pygame-quick?
-----------------------------

Like this::

    import pygame_quick

Alternatively, to have a shorter name, use::

    import pygame_quick as pgq

The rest of this sheet will assume the shorter name.

How do I create a window to draw in?
------------------------------------

You need to decide the width and height of the window. Say you wanted a window with a width of ``600`` and a height of ``400``::

    window = pgq.window(600, 400)

You can also write it like this::

    window = pgq.window(width=600, height=400)

Or::

    WINDOW_SIZE = (600, 400)
    window = pgq.window(WINDOW_SIZE)

Or::

    WINDOW_SIZE = (600, 400)
    window = pgq.window(size=WINDOW_SIZE)

I made a window, but then it vanished again???
----------------------------------------------

You need a main loop like this::

    while window.active():
        window.update()

If you do not need to do any new drawing for each frame, you can write is like this::

    window.loop_forever()

Why is the window always called "pygame-quick"? I want to call it "MY EPIC THING"!
----------------------------------------------------------------------------------

Do this::

    window = pgq.window(size=WINDOW_SIZE, title="MY EPIC THING")

You can also do this::

    window.title = "MY EPIC THING"

If you want to set the icon::

    window = pgq.window(size=WINDOW_SIZE, icon=image)

Or::

    window.icon = image

``image`` can be any image you want.

But how do I draw stuff? That white screen is boring!
-----------------------------------------------------

Well, do some drawing in your main loop::

    while window.active():
        # draw your stuff
        window.update()

To draw various things, look below! Remember, the window acts just like any other image. Anything you can do to an image, you can do to the window and vice-versa.

Eh? What's a image?
-------------------

An image is something you can draw on. You can create images just like you created a window::

    img = pgq.image(40, 30)

That will create an image that has a width of ``40`` and a height of ``30``. A new image will be transparent. You can get the width and height of an image::

    print("image width is", image.width, "and height is", image.height)

Or::

    print("image size is", image.size)


If you want a copy of an image, use ``image.copy``::

    image_copy = image.copy()

What use are images?
--------------------

You can use them to draw on the window! Say you had an image with a face draw on it, and you wanted to draw that face on the window several times. You can do that like this::

    face.draw(window, x=0, y=0)
    face.draw(window, x=100, y=100)

The x and y values specify where to draw the face. If you draw the face with ``x=30, y=40`` the top-left corner of the face image will be drawn at (30, 40).

How do I get an image of a face?
--------------------------------

Well, one way is to have an image of a face, and load it. Say the image is called ``/home/bob/face.jpg``. You could load it like this::

    face = pgq.image("/home/bob/face.jpg")

Wow! What if I want to put the face in the middle of the screen? Or a corner?
-----------------------------------------------------------------------------

To draw it in the center::

    face.draw(window, window.center, align=pgq.center)

Or::

    face.draw(window, window.center, align=face.center)

This says draw face such that the center of ``face`` is at the center of ``window``. If you want to put the top-right corner of face at the center of window, do this::

    face.draw(window, window.center, align=pgq.topright)

For the position to draw to you can pick any of::

    window.center
    window.topleft
    window.topright
    window.bottomleft
    window.bottomright

For the align you can pick from::

    pgq.center
    pgq.topleft
    pgq.topright
    pgq.bottomleft
    pgq.bottomright

Can I make my face bigger?
--------------------------

Just use ``image.scale``. If you want it twice as big::

    face.scale(2)

Or you want it twice as small::

    face.scale(0.5)

You can also rotate it (clockwise)::

    face.rotate(90)

And flip it::

    face.flip(vertical=True, horizontal=True)

``vertical=True`` means that the image is reflected along the x-axis and ``horizontal=True`` means that the image is reflected along the y-axis.

But the white background is still there! I want it green!
---------------------------------------------------------

Well, before drawing your faces, do this::

    window.fill("green")

For specifying colors you can give a name::

    window.fill("tomato")

Or an RGB combination::

    window.fill(255, 127, 0)

If you need to fill an image with a see-though (transparent) color::

    image.fill(255, 0, 0, 127)

That will fill image with red and will be 50% transparent. You can also specify the fill color when creating the image::

    img = pgq.image(40, 30, color="red")

And the same for the window::

    window = pgq.window(size=WINDOW_SIZE, color="green")

Ooo! Do I have to make an image if I want to draw a rectangle? It sounds like a lot of work...
----------------------------------------------------------------------------------------------

No! Say you want to draw a rectangle onto an image. You want the rectangle's top-left corner to be at (10, 20) and you want is to have a width of 50 and a height of 10. You want it filled with blue. Then do::

    image.draw_rect(x=10, y=20, width=50, height=10, color="blue")

You can also write it like::

    image.draw_rect(position=(10, 20), size=(50, 10), color=(0, 0, 255))

But it is less clear that way. You can use ``align`` with ``draw_rect``::

    image.draw_rect(position=(10, 20), size=(50, 10), color="blue", align=pgq.bottomright)

This means that ``position`` will be the bottom-right of the draw rectangle.

A border! I want a blue rectangle with a yellow border!
-------------------------------------------------------

Sure! First draw your blue rectangle::

    image.draw_rect(x=10, y=20, width=50, height=10, color="blue")

Then draw your border::

    image.draw_hollow_rect(x=10, y=20, width=50, height=10, color="blue")

This will draw a border that is 1 pixel thick. Want a wider border? Let's say 5 pixels::

    image.draw_hollow_rect(x=10, y=20, width=50, height=10, color="blue", thickness=5)

Using ``align``::

    image.draw_hollow_rect(x=10, y=20, width=50, height=10, color="blue", thickness=5, align=pgq.bottomright)

Yay! How about a circle? A black one!
-------------------------------------

To draw a circle at (40, 40) with radius 20 you do::

    image.draw_circle(x=40, y=40, radius=20, color="black")

Remember that you can also specify positions like this::

    image.draw_circle(position=image.center, radius=20, color="black")

Can circles have borders too?
-----------------------------

Yup, just like rectangles. Do draw a cyan border of thickness 10 do::

    image.draw_hollow_circle(position=image.center, radius=20, color="cyan", thickness=10)

Eh, thinking up color names is a pain. Is there a list somewhere?
-----------------------------------------------------------------

Yes there is! It is called ``pgq.color_names``. Want a random color? Just this way::

    import random
    random.choice(pgq.color_names)

Cool! I want to write my name. How?
-----------------------------------

Just like this::

    image.draw_text(text="my name", color="black", position=image.topleft)

Make sure your image is big enough!

Make my name bold! And italic!
------------------------------

Just like this::

    image.draw_text(text="my name", color="black", position=image.topleft, italic=True, bold=True)

Note! This may not change anything unless you change the font as well. To use a different font, set it like this::

    image.draw_text(text="my name", color="black", position=image.topleft, italic=True, bold=True, font="dejavusans")

Make my name BIGGER!
--------------------

OK, OK, here's font size 60::

    image.draw_text(text="my name", color="black", position=image.topleft, italic=True, bold=True, font="dejavusans", size=60)

Ha! Show me how to put "YOU DIED!" in the middle of the window!
---------------------------------------------------------------

``draw_text`` accepts the same align arguments as ``draw``, so do it the same way::

    window.draw_text(text="YOU DIED!", position=window.center, color="red", size=60, align=pgq.center)

What if I want to draw a line from A to B?
------------------------------------------

Well, lets say A and B are coordinates, any you want to draw a red line that has a thickness of 3::

    A = 20, 30
    B = 40, 60
    image.draw_line(start=A, end=B, color="red", thickness=3)

My program doesn't do much. How can I check if a key is pressed?
----------------------------------------------------------------

Modify your loop to look like this::

    while window.active():
        for type, value in window.events():
            # handle events here
        # drawing here
        window.update()

To check for a key press, replace ``# handle events here`` with::

    if type is pgq.key_down:
        print("You pressed", value)

I just want to check for the space bar, not everything!
-------------------------------------------------------

Do this::

    if type is pgq.key_down and value == " ":
        print("You pressed the space bar")

You can compare to any string you want. If you want to check for the "a" key, do::

    if type is pgq.key_down and value == "a":
        print("You pressed the a key")

Some special keys:

====================== =============
If you are looking for Test for
====================== =============
Return key             ``"\n"``
Space bar              ``" "``
Shift key              ``"<Shift>"``
Ctrl key               ``"<Ctrl>"``
Meta (windows) key     ``"<Meta>"``
Left arrow             ``"<Left>"``
Right arrow            ``"<Right>"``
Up arrow               ``"<Up>"``
Down arrow             ``"<Down>"``
Escape key             ``<Escape>``
Delete key             ``<Delete>``
Function X key         ``<FX>``
====================== =============

How about if they press the mouse?
----------------------------------

You can check for ``pgq.mouse_down``. If you only want clicks, test like this::

    if type is pgq.mouse_down and value.is_click():
        print("You clicked a mouse button at", value.x, value.y)

What about just the left mouse button?
--------------------------------------

For the left button::

    if type is pgq.mouse_down and value.button is pgq.left_button:
        print("You clicked the left mouse button at", value.position)

Right button::

    if type is pgq.mouse_down and value.button is pgq.right_button:
        print("You clicked the right mouse button at", value.position)

Middle button::

    if type is pgq.mouse_down and value.button is pgq.middle_button:
        print("You clicked the middle mouse button at", value.position)

Scrolling! What about that?
---------------------------

Do this::

    if type is pgq.mouse_down and value.is_scroll():
        print("You scrolled", value.scroll_direction, "at", position)

``value.direction`` will be one of::

    pgq.up_scroll
    pgq.down_scroll
    pgq.left_scroll
    pgq.right_scroll

What about if they move the mouse?
----------------------------------

Test for ``pgq.mouse_motion``::

    if type is pgq.mouse_motion:
        print("You moved the mouse from", value.from_position, "to", value.to_position)

You can also see how much the mouse moved::

    if type is pgq.mouse_motion:
        print("You moved the mouse by", value.moved_by_x, value.moved_by_y)

If you want to see if any buttons were pressed during the movement, test them using ``value.is_pressed``::

    if value.is_pressed(pgq.left_button):
        print("Drag with left button")
    elif value.is_pressed(pgq.right_button):
        print("Drag with right button")
    elif value.is_pressed(pgq.middle_button):
        print("Drag with middle button")

Just tell me where the mouse is now!
------------------------------------

Use ``pgq.mouse_position``::

    print("The mouse is at", pgq.mouse_position())

Can I move where the mouse is?
------------------------------

Use ``pgq.set_mouse_position``::

    pgq.set_mouse_position(window.center)

I made a snake program, and the snake went really fast!
-------------------------------------------------------

When you create your window, you can change how fast it updates::

    window = pgq.window(WINDOW_SIZE, frame_rate=5)

``frame_rate`` is normally 20. You can make it smaller to slow the game down or larger to speed it up.

Can I tell which frame I am on?
-------------------------------

Look at ``window.frame_number``::

    print("You are on frame", window.frame_number)

You can use this like a timer, but it will not be very accurate::

    print("Game playing for", window.frame_number / window.frame_rate)

How can I stop the game when the player looses?
-----------------------------------------------

Call ``window.stop``::

    if player_lost:
        window.stop()


OK, last thing. I want explosion noises!
----------------------------------------

Sure. If you call your sound file ``/home/bob/explosion.wav``, load it like this::

    explosion = pgq.sound("/home/bob/explosion.wav")

Play it using::

    explosion.play()

To set the volume of the sound at 50%::

    explosion.volume = 0.5

If you need the length of the sound::

    print("Explosion is", explosion.length, "seconds long")

Can I make a sound repeat?
--------------------------

Yup. To make it repeat 10 times, use::

    explosion.play(times=10)

Really last thing. How can I make it repeat FOREVER!
----------------------------------------------------

Simply::

    explosion.play(forever=True)

You can make it stop by calling::

    explosion.stop()
