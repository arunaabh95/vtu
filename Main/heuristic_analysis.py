
from Main.Search import *
from Main.voyage import get_default_states
from Constants.environment_constants import *
from Entity.Grid import Grid
from Main.util import *
import time
import numpy

GRID_SIZE = GLOBAL_BIG_MAZE_SIZE
GRID_COUNT = GLOBAL_TEST_COUNT
PROBABILITY = GLOBAL_PROBABILITY


def heuristic_tester():
    grids = get_grids(GRID_COUNT, GRID_SIZE, PROBABILITY)
    manhattan_paths, manhattan_time = solve_maze_with_heuristic(grids, MANHATTAN_HEURISTICS)
    euclid_paths, euclid_time = solve_maze_with_heuristic(grids, EUCLIDEAN_HEURISTICS)
    chebyshev_paths, chebyshev_time = solve_maze_with_heuristic(grids, CHEBYSHEV_HEURISTICS)
    print("Manhattan Time", manhattan_time, "Manhattan Paths", manhattan_paths)
    print("Euclid Time", euclid_time, "Euclid Paths", euclid_paths)
    print("Chebyshev Time", chebyshev_time, "Chebyshev Paths", chebyshev_paths)
    generate_path_graphs(manhattan_paths, euclid_paths, chebyshev_paths)


# function to optimize existing heuristics by increasing weights
def heuristic_optimization():
    grids = get_grids(GRID_COUNT, GRID_SIZE, PROBABILITY)
    manhattan_paths, manhattan_time = solve_maze_with_heuristic(grids, MANHATTAN_HEURISTICS)
    manhattan_paths_10, manhattan_time_10 = solve_maze_with_heuristic(grids, MANHATTAN_HEURISTICS, 10)
    manhattan_paths_20, manhattan_time_20 = solve_maze_with_heuristic(grids, MANHATTAN_HEURISTICS, 20)
    manhattan_paths_30, manhattan_time_30 = solve_maze_with_heuristic(grids, MANHATTAN_HEURISTICS, 30)
    combined_heuristic_path, combined_heuristic_time = solve_maze_with_heuristic(grids, COMBINED_HEURISTICS)

    print("Manhattan Time 1", manhattan_time, "Manhattan Paths with weight 1", manhattan_paths)
    print("Manhattan Time 10", manhattan_time_10, "Manhattan Paths with weight 10", manhattan_paths_10)
    print("Manhattan Time 20", manhattan_time_20, "Manhattan Paths with weight 20", manhattan_paths_20)
    print("Manhattan Time 30", manhattan_time_30, "Manhattan Paths with weight 30", manhattan_paths_30)
    print("Combined Heuristics Time", combined_heuristic_time, "Combined Heuristics Path", combined_heuristic_path)

    generate_path_graphs_2(manhattan_paths, manhattan_paths_10, manhattan_paths_20,
                           manhattan_paths_30, combined_heuristic_path)


def solve_maze_with_heuristic(grids, heuristic_flag, weight=1):
    paths = []
    start = time.perf_counter()
    for i in range(len(grids)):
        start_state, goal_state = get_default_states(grids[i])
        search = Search(grids[i], start_state, goal_state, heuristics_flag=heuristic_flag, heuristic_weight=weight)
        search.solve_maze()
        path_length = search.get_path_length()
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
    generate_graph(x, [manhattan_paths, euclid_paths, chebyshev_paths],
                   "Density vs Path length", "Density", "Path Length",
                   ["Manhattan", "Euclid", "Chebyshev"])


def generate_path_graphs_2(manhattan_paths, manhattan_paths_10, manhattan_paths_20,
                           manhattan_paths_30, combined_heuristics_path):
    x = numpy.arange(1, GRID_COUNT, 1)
    generate_graph(x, [manhattan_paths, manhattan_paths_10, manhattan_paths_20,
                       manhattan_paths_30, combined_heuristics_path],
                   "Density vs Path length", "Density", "Path Length",
                   ["Manhattan 1", "Manhattan 10", "Manhattan 20", "Manhattan 30", "Combined Heuristics"])


# heuristic_tester()
heuristic_optimization()
