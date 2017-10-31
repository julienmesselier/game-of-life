from unittest import TestCase
from game_of_life import *

class TestGameOfLife(TestCase):
    def test_empty_world_remains_empty_after_iteration(self):
        world = np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])
        np.testing.assert_array_equal(world,iterate(world))