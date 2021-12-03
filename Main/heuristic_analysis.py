
from Main.Search import *
from Main.voyage import get_default_states
from Constants.environment_constants import *
from Entity.Grid import Grid
from Main.util import *
import time

GRID_SIZE = GLOBAL_BIG_MAZE_SIZE
GRID_COUNT = GLOBAL_TEST_COUNT
PROBABILITY = GLOBAL_PROBABILITY


# function to compare manhattan, euclidean and chebyshev heuristics
def heuristic_tester():
    grids = get_grids(GRID_COUNT, GRID_SIZE, PROBABILITY)
    manhattan_paths, manhattan_time = solve_maze_with_heuristic(grids, MANHATTAN_HEURISTICS)
    euclid_paths, euclid_time = solve_maze_with_heuristic(grids, EUCLIDEAN_HEURISTICS)
    chebyshev_paths, chebyshev_time = solve_maze_with_heuristic(grids, CHEBYSHEV_HEURISTICS)
    print("Manhattan Time", manhattan_time, "Avg Manhattan Path", (sum(manhattan_paths)/GRID_COUNT))
    print("Euclid Time", euclid_time, "Avg Euclid Paths", (sum(euclid_paths)/GRID_COUNT))
    print("Chebyshev Time", chebyshev_time, "Avg Chebyshev Paths", (sum(chebyshev_paths)/GRID_COUNT))
    generate_path_graphs(manhattan_paths, euclid_paths, chebyshev_paths)


# function to compare heuristic function with different weights
def heuristic_optimization():
    grids = get_grids(GRID_COUNT, GRID_SIZE, PROBABILITY)
    manhattan_paths, manhattan_time = solve_maze_with_heuristic(grids, MANHATTAN_HEURISTICS)
    manhattan_paths_10, manhattan_time_10 = solve_maze_with_heuristic(grids, MANHATTAN_HEURISTICS, 10)
    manhattan_paths_20, manhattan_time_20 = solve_maze_with_heuristic(grids, MANHATTAN_HEURISTICS, 20)
    manhattan_paths_30, manhattan_time_30 = solve_maze_with_heuristic(grids, MANHATTAN_HEURISTICS, 30)
    combined_heuristic_path, combined_heuristic_time = solve_maze_with_heuristic(grids, COMBINED_HEURISTICS)

    print("Manhattan Time 1", manhattan_time,
          "Avg of Manhattan Path with weight 1", sum(manhattan_paths)/ GRID_COUNT)
    print("Manhattan Time 10", manhattan_time_10,
          "Avg of Manhattan Path with weight 10", sum(manhattan_paths_10)/ GRID_COUNT)
    print("Manhattan Time 20", manhattan_time_20,
          "Avg of Manhattan Path with weight 20", sum(manhattan_paths_20)/ GRID_COUNT)
    print("Manhattan Time 30", manhattan_time_30,
          "Avg of Manhattan Path with weight 30", sum(manhattan_paths_30)/ GRID_COUNT)
    print("Combined Heuristics Time", combined_heuristic_time,
          "Avg of Combined Heuristics Path", sum(combined_heuristic_path)/ GRID_COUNT)

    generate_path_graphs_2(manhattan_paths, manhattan_paths_10, manhattan_paths_20,
                           manhattan_paths_30, combined_heuristic_path)


# run heuristic on plenty of mazes
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


# generate a list of grids that will be used to test our heuristic functions
def get_grids(grid_count, grid_size, probability):
    grids = []
    for i in range(1, grid_count):
        grids.append(Grid.make_grid(probability, grid_size))

    return grids


# function to print graphs
def generate_path_graphs(manhattan_paths, euclid_paths, chebyshev_paths):
    x = numpy.arange(1, GRID_COUNT, 1)
    generate_graph(x, [manhattan_paths, euclid_paths, chebyshev_paths],
                   "Density vs Path length", "Density", "Path Length",
                   ["Manhattan", "Euclid", "Chebyshev"])


# function to print graphs
# this is redundant function could have refactored to merge with the first one
def generate_path_graphs_2(manhattan_paths, manhattan_paths_10, manhattan_paths_20,
                           manhattan_paths_30, combined_heuristics_path):
    x = numpy.arange(1, GRID_COUNT, 1)
    generate_graph(x, [manhattan_paths, manhattan_paths_10, manhattan_paths_20,
                       manhattan_paths_30, combined_heuristics_path],
                   "Density vs Path length", "Density", "Path Length",
                   ["Manhattan 1", "Manhattan 10", "Manhattan 20", "Manhattan 30", "Combined Heuristics"])


# function to solve q5
heuristic_tester()

# function to solve q9
# heuristic_optimization()
