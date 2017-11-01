import numpy as np

def compute_number_of_neighbours(world):
    return (world[0:-2, 0:-2] + world[0:-2, 1:-1] + world[0:-2, 2:] +
            world[1:-1, 0:-2]                     + world[1:-1, 2:] +
            world[2:  , 0:-2] + world[2:, 1:-1]   + world[2:, 2:])

def iterate(world):
    neighbours = compute_number_of_neighbours(world)
    death = ((neighbours < 2) | (neighbours > 3)) & (world[1:-1, 1:-1] == 1)
    birth = (neighbours == 3) & (world[1:-1, 1:-1] == 0)
    world[1:-1, 1:-1][death] = 0
    world[1:-1, 1:-1][birth] = 1
    world[0, :] = world[-1, :] = world[:, 0] = world[:, -1] = 0