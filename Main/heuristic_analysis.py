
from Main.search import *
import time
import matplotlib.pyplot as plt
import numpy

GRID_SIZE = 101
GRID_COUNT = 50
PROBABILITY = 0.3


def heuristic_tester():
    grids = get_grids(GRID_COUNT, GRID_SIZE, PROBABILITY)
    manhattan_paths, manhattan_time = solve_maze_with_heuristic(grids, get_manhattan)
    euclid_paths, euclid_time = solve_maze_with_heuristic(grids, get_euclidean)
    chebyshev_paths, chebyshev_time = solve_maze_with_heuristic(grids, get_chebyshev)
    print("Manhattan Time", manhattan_time, "Manhattan Paths", manhattan_paths)
    print("Euclid Time", euclid_time, "Euclid Paths", euclid_paths)
    print("Chebyshev Time", chebyshev_time, "Manhattan Paths", chebyshev_paths)
    generate_path_graphs(manhattan_paths, euclid_paths, chebyshev_paths)


def solve_maze_with_heuristic(grids, heuristic_callback):
    paths = []
    start = time.perf_counter()
    for i in range(len(grids)):
        path_length = len(solve_maze(grids[i], GRID_SIZE, heuristic_callback))
        paths.append(path_length)
    total_execution_time = time.perf_counter() - start
    return paths, total_execution_time


def get_grids(grid_count, grid_size, probability):
    grids = []
    for i in range(1, grid_count):
        grids.append(Grid.make_grid(probability, grid_size))

    return grids


def generate_path_graphs(manhattan_paths, euclid_paths, chebyshev_paths):
    x = numpy.arange(1, GRID_COUNT, 1)
    plt.plot(x, manhattan_paths, label="Manhattan")
    plt.plot(x, euclid_paths, label="Euclid")
    plt.plot(x, chebyshev_paths, label="Chebyshev")

    plt.title("Heuristic Path lengths")
    plt.xlabel("Test Count")
    plt.ylabel("Path Length")
    plt.show()


heuristic_tester()
