import unittest

import pygame

from Player import Player


class TestPlayer(unittest.TestCase):
    size = (1520, 980)
    screen = pygame.display.set_mode(size)
    p = Player(testing=True)

    # move_helper test cases
    def test_move_helper0(self):
        dest = (10, 10)
        vel = 5
        self.assertEqual(self.p.move_helper(dest, vel), [vel, vel])

    def test_move_helper1(self):
        dest = (10, 0)
        vel = 5
        self.assertEqual(self.p.move_helper(dest, vel), [vel, 0])

    def test_move_helper2(self):
        dest = (0, 10)
        vel = 5
        self.assertEqual(self.p.move_helper(dest, vel), [0, vel])

    def test_move_helper3(self):
        dest = (0, 0)
        vel = 5
        self.assertEqual(self.p.move_helper(dest, vel), [0, 0])

    def test_move_helper4(self):
        dest = (10, 10)
        vel = 5
        self.p.x = 20
        self.assertEqual(self.p.move_helper(dest, vel), [-vel, vel])


    # ----- test cases


if __name__ == '__main__':
    unittest.main()
