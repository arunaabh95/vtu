from Entity.State import State
from Entity.Grid import Grid
from Constants.environment_constants import *
from Main.Search import Search
from Main.util import print_path


# this file is a single instance of vanilla flavoured implementation mainly for testing purposes

# This function defines the default start and goal state for all questions
def get_default_states(complete_grid):
    grid_size = len(complete_grid)
    goal = State(grid_size - 1, grid_size - 1, complete_grid[grid_size - 1][grid_size - 1], 0, 0)
    start = State(0, 0, complete_grid[0][0], 0, grid_size + grid_size - 2)
    return start, goal


def voyage(probability=GLOBAL_PROBABILITY, grid_size=GLOBAL_BIG_MAZE_SIZE):
    grid = Grid.make_grid(probability, grid_size)
    # print(grid)
    start_state, goal_state = get_default_states(grid)
    search1 = Search(grid, start_state, goal_state, restrict_field_of_view=ALLOW_BASIC_SENSING)
    search1.solve_maze()
    path = search1.get_final_path()
    # print_path(path)
    print("Agent 3 ", search1.get_bump_count(), " ", search1.get_path_length())
    search2 = Search(grid, start_state, goal_state, restrict_field_of_view=ALLOW_FIELD_OF_VIEW)
    search2.solve_maze()
    path = search2.get_final_path()
    # print_path(path)
    print("Agent 1 ", search2.get_bump_count(), " ", search2.get_path_length())
    search3 = Search(grid, start_state, goal_state, restrict_field_of_view=RESTRICT_FIELD_OF_VIEW)
    search3.solve_maze()
    path = search3.get_final_path()
    # print_path(path)
    print("Agent 2 ", search3.get_bump_count(), " ", search3.get_path_length())
    # print("Success yaya!")


'''
def voyage(probability=GLOBAL_PROBABILITY, grid_size=GLOBAL_SMALL_MAZE_SIZE):
    grid = Grid.make_grid(probability, grid_size)
    print(grid)
    start_state, goal_state = get_default_states(grid)
    search1 = Search(grid, start_state, goal_state, restrict_field_of_view=ALLOW_BASIC_SENSING)
    search1.solve_maze()
    path = search1.get_final_path()
    path = search1.get_final_path()
    print_path(path)
    print("Agent 3 ", search1.get_bump_count(), " ", search1.get_path_length())
'''

def voyage_on_grid(probability, grid):
    #  voyage(probability, len(grid))
    pass


for i in range(10):
    print("test ", i)
    voyage()

'''
[[0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [1. 1. 0. 1. 1. 1. 1. 1. 1. 1. 1. 0. 0. 1. 0. 1. 0. 0. 1. 0.]
 [1. 1. 0. 1. 0. 1. 1. 0. 1. 0. 1. 1. 0. 0. 1. 0. 1. 1. 0. 0.]
 [1. 0. 1. 0. 0. 1. 1. 0. 0. 1. 1. 0. 1. 0. 1. 0. 1. 0. 0. 0.]
 [1. 0. 0. 0. 1. 0. 0. 1. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 1. 0.]
 [1. 1. 0. 0. 0. 1. 0. 0. 0. 0. 1. 1. 0. 1. 0. 0. 0. 1. 0. 0.]
 [1. 0. 0. 0. 0. 0. 0. 1. 0. 1. 0. 0. 0. 0. 0. 1. 1. 1. 0. 0.]
 [0. 0. 1. 0. 0. 1. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 0. 0. 1. 0.]
 [0. 0. 0. 1. 0. 1. 1. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 1. 0. 0.]
 [0. 1. 0. 0. 0. 1. 1. 0. 0. 1. 0. 0. 0. 1. 1. 0. 0. 0. 0. 0.]
 [0. 0. 1. 0. 0. 1. 0. 1. 0. 1. 0. 0. 1. 0. 0. 0. 1. 0. 0. 0.]
 [0. 1. 1. 0. 0. 1. 1. 1. 0. 0. 0. 0. 1. 1. 0. 0. 1. 1. 1. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 0. 0. 1. 0. 1. 0.]
 [1. 1. 0. 1. 0. 0. 0. 1. 1. 0. 0. 1. 0. 1. 0. 1. 0. 1. 1. 0.]
 [1. 1. 0. 0. 1. 1. 1. 0. 1. 0. 0. 0. 1. 1. 0. 0. 1. 1. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 1. 0. 0. 1. 1. 0. 0. 1. 1. 1. 0. 0.]
 [1. 0. 1. 0. 1. 0. 1. 0. 1. 0. 0. 0. 1. 1. 0. 0. 1. 1. 0. 0.]
 [0. 0. 0. 1. 1. 0. 1. 1. 0. 0. 1. 1. 0. 1. 0. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 1. 0. 0. 1. 1. 0. 1. 0. 0. 0. 1. 0. 1. 0. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
'''