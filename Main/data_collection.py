# call solve_maze and pass field_view = 1
import pickle
import pandas as pd
import numpy as np

from Entity.Grid import Grid
from Main.Search import *
from Main.voyage import get_default_states

PROBABILITIES = [0.3]
pickle.HIGHEST_PROTOCOL = 4
TEST_COUNT = GLOBAL_TEST_COUNT
GRID_SIZE = GLOBAL_BIG_MAZE_SIZE
# for q6 we allow field of view and for q7 we restrict it
FIELD_OF_VIEW = ALLOW_BASIC_SENSING

def initialize_test_variables(probability, field_of_view):
    grid = Grid.make_grid(probability, GRID_SIZE)
    start_state, goal_state = get_default_states(grid)
    # for q6 and q7 we have used the default algorithm that is a_star,
    # for q9 we have repeated this by passing search type param as BFS
    search = Search(grid, start_state, goal_state, restrict_field_of_view=field_of_view)
    return grid, start_state, goal_state, search


# Initialize search class to run test on given set of probabilities and find all the metrics in q6
def conduct_tests(field_of_view):
    data = pd.DataFrame()
    for probability in PROBABILITIES:
        for test_index in range(TEST_COUNT):
            grid, start_state, goal_state, search = initialize_test_variables(probability, field_of_view)
            search.solve_maze()
            if len(search.final_path) == 0:
                continue
            temp = preprocess(search.get_movement_data())
            print(temp.shape)
            if test_index == 0:
                data = temp
            else:
                data = pd.concat([data, temp], axis=0)
            print("Done test ", test_index, "for probability ", probability)
    write_to_file(data)


def preprocess(data):
    i = 0
    while i < len(data):
        g = Grid.make_grid(0, GLOBAL_BIG_MAZE_SIZE)
        idxs = data[i][0]
        g[idxs[0]][idxs[1]] = 1
        data[i][0] = g
        data[i][2] = map_direction(data[i][2])
        i += 1
    return pd.DataFrame(data)


def write_to_file(data):
    data.to_hdf('../Data/train-3.h5', key='df', mode='a')


def map_direction(inp):
    if inp[0] == 0 and inp[1] == 0:
        return "stay"
    if inp[1] == 1:
        return "right"
    if inp[1] == -1:
        return "left"
    if inp[0] == 1:
        return "up"
    if inp[0] == -1:
        return "down"


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
