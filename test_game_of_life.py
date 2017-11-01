from unittest import TestCase
from game_of_life import *

class TestGameOfLife(TestCase):
    def test_empty_world_remains_empty_after_iteration(self):
        world = np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])
        np.testing.assert_array_equal(world, iterate(world))


    def test_world_borders_remains_empty_after_iteration(self):
        world = np.array([[0, 1, 0],
                         [1, 1, 1],
                         [0, 1, 0]])

        world_iterated = iterate(world)
        north_border = world_iterated[0, :]
        south_border = world_iterated[-1, :]
        east_border = world_iterated[:, 0]
        west_border = world_iterated[:, -1]

        np.testing.assert_array_equal(0, north_border)
        np.testing.assert_array_equal(0, south_border)
        np.testing.assert_array_equal(0, east_border)
        np.testing.assert_array_equal(0, west_border)

    def test_cell_with_exactly_3_neighbors_remains_alive_after_iteration(self):
        world = np.array([[1, 0, 0],
                          [1, 1, 1],
                          [0, 0, 0]])
#        self.assertEqual(1, iterate(world)[1, 1])

    def test_neighbors_computation(self):
        world = np.array([[1, 0, 0],
                          [1, 1, 1],
                          [0, 0, 0]])

        expected_neighbors = np.array([[3]])

        np.testing.assert_array_equal(expected_neighbors, compute_number_of_neighbours(world))
