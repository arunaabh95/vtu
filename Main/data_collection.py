# call solve_maze and pass field_view = 1
import csv
import pandas as pd
import numpy as np
from Entity.Grid import Grid
from Main.Search import *
from Main.voyage import get_default_states

PROBABILITIES = [0.06, 0.12, 0.18, 0.24, 0.3, 0.36, 0.42, 0.45, 0.48]
TEST_COUNT = GLOBAL_TEST_COUNT
GRID_SIZE = GLOBAL_BIG_MAZE_SIZE
# for q6 we allow field of view and for q7 we restrict it
FIELD_OF_VIEW = ALLOW_FIELD_OF_VIEW

np.set_printoptions(threshold=np.inf)


def initialize_test_variables(probability, field_of_view):
    grid = Grid.make_grid(probability, GRID_SIZE)
    start_state, goal_state = get_default_states(grid)
    # for q6 and q7 we have used the default algorithm that is a_star,
    # for q9 we have repeated this by passing search type param as BFS
    search = Search(grid, start_state, goal_state, field_of_view)
    return grid, start_state, goal_state, search


# Initialize search class to run test on given set of probabilities and find all the metrics in q6
def conduct_tests(field_of_view):
    for probability in PROBABILITIES:
        for test_index in range(TEST_COUNT):
            grid, start_state, goal_state, search = initialize_test_variables(probability, field_of_view)
            search.solve_maze()
            write_to_file(search.get_movement_data())
            print("Done test ", test_index, "for probability ", probability)
            # data = pd.read_csv('../Data/data.csv')
            # print(data)


def write_to_file(data):
    data = np.array(data)
    file = open(r'../Data/data.csv', 'a')
    with file:
        write = csv.writer(file, delimiter=',')
        write.writerows(data)
    file.close()


def run_performance_tests(field_of_view):

    conduct_tests(field_of_view)


run_performance_tests(FIELD_OF_VIEW)

'''
test maze

    grid = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
            [1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
            [1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

'''
