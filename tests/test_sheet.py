from __future__ import absolute_import
from unittest import TestCase, main
import os

import pygame

from pygame_anisprite import anisprite
# this isn't very law of demeter...
from tests.common import compare_surfaces


class MockClock(object):
    def get_time(self):
        # must be enough to advance animation to next frame when called
        return 501


class TestSpriteSheet(TestCase):

    def test_sheet_loading(self):
        testpath = os.path.realpath(__file__)
        path = os.path.abspath(os.path.join(testpath,
                                            "..",
                                            "resources",
                                            "spritesheet.png"))

        # Create our mock clock
        clock = MockClock()

        # Required for convert_alpha in from_sheet method below.
        pygame.init()
        screen = pygame.display.set_mode([32, 32])

        # Create the AnimatedSprite object from the test GIF file
        animsprite = anisprite.AnimatedSprite.from_sheet(path, 16, 16, duration=1000)

        # Test getting the dimensions of the largest frame
        self.assertTupleEqual(animsprite.largest_frame_size(), (16, 16))

        # Create surfaces to compare against
        frameone = pygame.surface.Surface((16, 16))
        frameone.fill((255, 0, 0))
        frametwo = pygame.surface.Surface((16, 16))
        frametwo.fill((0, 255, 0))

        # Blit the AnimatedSprite (which should give us our first frame)
        outputsurface = pygame.surface.Surface((16, 16))
        outputsurface.blit(animsprite.image, (0, 0))

        self.assertTrue(compare_surfaces(outputsurface, frameone))

        timedelta = clock.get_time()
        animsprite.update(timedelta)

        # Blit again, which should give us our second frame
        outputsurface = pygame.surface.Surface((16, 16))
        outputsurface.blit(animsprite.image, (0, 0))

        self.assertTrue(compare_surfaces(outputsurface, frametwo))


if __name__ == '__main__':
    main()
