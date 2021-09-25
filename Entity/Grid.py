import random
import numpy


class Grid:

    @staticmethod
    # function to make grid for given size and with given probability
    def make_grid(probability, size):
        grid = numpy.zeros((size, size))
        if probability == 0:
            return grid
        for i in range(0, size - 1):
            for j in range(0, size - 1):
                p0 = random.uniform(0, 1)
                if probability > p0:
                    grid[i][j] = 1

        grid[0][0] = 0
        grid[size - 1][size - 1] = 0
        return grid

