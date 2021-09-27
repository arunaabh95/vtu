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


def voyage(probability=GLOBAL_PROBABILITY, grid_size=GLOBAL_SMALL_MAZE_SIZE):
    grid = Grid.make_grid(0, grid_size)
    print(grid)
    start_state, goal_state = get_default_states(grid)
    search = Search(grid, start_state, goal_state, search_type=BFS)
    search.solve_maze()
    path = search.get_final_path()
    print_path(path)
    print(search.get_search_time())
    print("Success yaya!")


def voyage_on_grid(probability, grid):
    voyage(probability, len(grid))


# voyage()
