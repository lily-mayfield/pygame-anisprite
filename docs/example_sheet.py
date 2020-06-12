"""
Example code loading and animating sprites from a .png sheet.
"""
import pygame
import os

from pygame_anisprite import anisprite

print(__debug__)
sheet = "sheet.png"
image_path = os.path.abspath(sheet)

pygame.init()
screen = pygame.display.set_mode([700, 500])
clock = pygame.time.Clock()
done = False

# Create the AnimatedSprite object from the test GIF file.
# Total animation duration is 1 second.
animsprite = anisprite.AnimatedSprite.from_sheet(image_path, 16, 16, duration=1000)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(animsprite.image, (10, 10))
    animsprite.update(clock.get_time())
    pygame.display.flip()
    # run at 60 FPS
    clock.tick(60)

pygame.quit()
