import random
import numpy


def make_grid(p, size):
    grid = numpy.zeros((size, size))
    for i in range(0, size - 1):
        for j in range(0, size - 1):
            p0 = random.uniform(0, 1)
            if p > p0:
                grid[i][j] = 1

    grid[0][0] = 0
    grid[size - 1][size - 1] = 0
    print(grid)


make_grid(0.4, 5)

