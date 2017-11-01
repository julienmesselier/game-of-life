from unittest import TestCase
from game_of_life import *

class TestGameOfLife(TestCase):
    def test_empty_world_remains_empty_after_iteration(self):
        world = np.array([[0, 0, 0],
                         [0, 0, 0],
                         [0, 0, 0]])
        iterate(world)
        np.testing.assert_array_equal(0, world)


    def test_world_borders_remains_empty_after_iteration(self):
        world = np.array([[0, 1, 0],
                         [1, 1, 1],
                         [0, 1, 0]])

        iterate(world)
        north_border = world[0, :]
        south_border = world[-1, :]
        east_border = world[:, 0]
        west_border = world[:, -1]

        np.testing.assert_array_equal(0, north_border)
        np.testing.assert_array_equal(0, south_border)
        np.testing.assert_array_equal(0, east_border)
        np.testing.assert_array_equal(0, west_border)

    def test_neighbors_computation(self):
        world = np.array([[0, 0, 0, 0, 0, 0],
                          [0, 1, 0, 1, 1, 0],
                          [0, 0, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0]])

        expected_neighbors = np.array([[1, 4, 4, 3],
                                       [2, 3, 4, 3]])

        np.testing.assert_array_equal(expected_neighbors, compute_number_of_neighbours(world))

    def test_cell_with_exactly_3_neighbors_alive_remains_alive_after_iteration(self):
        world = np.array([[0, 0, 0, 0, 0, 0],
                          [0, 1, 0, 1, 1, 0],
                          [0, 0, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0]])
        iterate(world)

        self.assertEqual(1, world[1, 4])
        self.assertEqual(1, world[2, 4])


    def test_cell_with_exactly_2_neighbors_alive_keeps_its_state_unchanged(self):
            world = np.array([[0, 0, 0, 0, 0, 0],
                              [0, 1, 0, 1, 1, 0],
                              [0, 0, 1, 1, 1, 0],
                              [0, 0, 0, 0, 0, 0]])
            iterate(world)

            self.assertEqual(0, world[2, 1])

    def test_cell_with_strictly_more_than_3_neighbors_alive_dies(self):
                world = np.array([[0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 1, 1, 0],
                                  [0, 0, 1, 1, 1, 0],
                                  [0, 0, 0, 0, 0, 0]])
                iterate(world)

                self.assertEqual(0, world[1, 1])


    def test_cell_with_less_than_2_neighbors_alive_dies(self):
                world = np.array([[0, 0, 0, 0, 0, 0],
                                  [0, 1, 0, 1, 1, 0],
                                  [0, 0, 1, 1, 1, 0],
                                  [0, 0, 0, 0, 0, 0]])
                iterate(world)

                self.assertEqual(0, world[1, 3])
                self.assertEqual(0, world[2, 3])
                self.assertEqual(0, world[3, 3])


    def test_space_ship_glider_pattern_1(self):
                world = np.array([[0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 1, 0, 0],
                                 [0, 1, 0, 1, 0, 0],
                                 [0, 0, 1, 1, 0, 0],
                                 [0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0]])
                for i in range(4): iterate(world)

                expected_result =    np.array([[0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 1, 0],
                                               [0, 0, 1, 0, 1, 0],
                                               [0, 0, 0, 1, 1, 0],
                                               [0, 0, 0, 0, 0, 0]])

                np.testing.assert_array_equal(expected_result, world)



    def test_space_ship_glider_pattern_2(self):
                world = np.array([[0, 0, 0, 0, 0, 0],
                                 [0, 1, 0, 1, 0, 0],
                                 [0, 0, 1, 1, 0, 0],
                                 [0, 0, 1, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 0]])
                for i in range(4): iterate(world)

                expected_result =    np.array([[0, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0],
                                               [0, 0, 1, 0, 1, 0],
                                               [0, 0, 0, 1, 1, 0],
                                               [0, 0, 0, 1, 0, 0],
                                               [0, 0, 0, 0, 0, 0]])

                np.testing.assert_array_equal(expected_result, world)


    def test_oscillator_beacon_pattern(self):
                world = np.array([[0, 0, 0, 0, 0, 0],
                                 [0, 1, 1, 0, 0, 0],
                                 [0, 1, 1, 0, 0, 0],
                                 [0, 0, 0, 1, 1, 0],
                                 [0, 0, 0, 1, 1, 0],
                                 [0, 0, 0, 0, 0, 0]])
                for i in range(2): iterate(world)

                expected_result =    np.array([[0, 0, 0, 0, 0, 0],
                                 [0, 1, 1, 0, 0, 0],
                                 [0, 1, 1, 0, 0, 0],
                                 [0, 0, 0, 1, 1, 0],
                                 [0, 0, 0, 1, 1, 0],
                                 [0, 0, 0, 0, 0, 0]])

                np.testing.assert_array_equal(expected_result, world)
