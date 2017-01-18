import pygame_quick

bullet = pygame_quick.surface(10, 10)
bullet.draw_circle(position=bullet.center, radius=5, color=pygame_quick.color.red)
bullets = []

window = pygame_quick.window(600, 400)

while window.active():
    window.fill(pygame_quick.color.white)
    window.draw_text(text="Press space to shoot...", position=window.topleft, color=pygame_quick.color.black)

    new_bullets = []
    for x, y in bullets:
        if y > -10:
            new_bullets.append((x, y - 10))
    bullets = new_bullets

    for type, value in window.events():
        if type is pygame_quick.key_down and value == " ":
            bullet_x, _ = pygame_quick.mouse_position()
            bullets.append((bullet_x, window.height))

    for bullet_position in bullets:
        bullet.draw_by_center(window, bullet_position)

    window.update()
