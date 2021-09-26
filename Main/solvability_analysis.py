# this file calculates density vs solvability graph
from Entity.Search import *
from Main.util import *
from Main.voyage import get_default_states
from Entity.Grid import Grid
from Constants.environment_constants import *


GRID_SIZE = GLOBAL_BIG_MAZE_SIZE
TEST_COUNT = GLOBAL_TEST_COUNT


def test_main():
    probabilities = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]
    solvability_list = []
    for probability in probabilities:
        solvability_list.append(run_tests(probability, TEST_COUNT) / TEST_COUNT * 100)
    plot_graph(probabilities, solvability_list)


def run_tests(probability, test_counts):
    solvability = 0
    for test_count in range(test_counts):
        grid = Grid.make_grid(probability, GRID_SIZE)
        start_state, goal_state = get_default_states(grid)
        search = Search(grid, start_state, goal_state)
        search.solve_maze()
        path = search.get_final_path()
        if len(path) > 0:
            solvability += 1
    return solvability


def plot_graph(probabilities, solvability_list):
    print(solvability_list)
    generate_graph(probabilities, solvability_list, "Density vs Solvability", "Density", "Solvability")


test_main()
