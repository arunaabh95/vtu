# call solve_maze and pass field_view = 1
from Entity.Grid import Grid
from Main.Search import *
from Main.voyage import get_default_states

PROBABILITIES = [0.06, 0.12, 0.18, 0.24, 0.3, 0.36]
TEST_COUNT = GLOBAL_TEST_COUNT
GRID_SIZE = GLOBAL_SMALL_MAZE_SIZE
# for q6 we allow field of view and for q7 we restrict it
FIELD_OF_VIEW = ALLOW_BASIC_SENSING


def initialize_test_variables(probability, field_of_view):
    grid = Grid.make_grid(probability, GRID_SIZE)
    start_state, goal_state = get_default_states(grid)
    # for q6 and q7 we have used the default algorithm that is a_star,
    # for q9 we have repeated this by passing search type param as BFS
    search = Search(grid, start_state, goal_state, field_of_view)
    return grid, start_state, goal_state, search


def get_traversed_path_len(search):
    return len(search.get_final_path())


# Calculate Trajectory len/Shortest Grid length of final grid
def get_trajectory_len_to_shortest_grid_len(search, shortest_path_in_discovered_grid):
    trajectory_len = len(search.get_final_path())
    shortest_traversed_path_to_explored_grid_len = 0
    if len(shortest_path_in_discovered_grid) != 0:
        shortest_traversed_path_to_explored_grid_len = trajectory_len / len(shortest_path_in_discovered_grid)
    return shortest_traversed_path_to_explored_grid_len


# Calculate (shortest path in final grid/ shortest path in full grid)
def get_final_grid_len_to_shortest_full_grid_len(shortest_path_in_discovered_grid, shortest_path_in_complete_grid):
    shortest_final_grid_len_to_shortest_full_grid_len = 0
    if len(shortest_path_in_complete_grid) != 0:
        shortest_final_grid_len_to_shortest_full_grid_len = len(shortest_path_in_discovered_grid) / \
                                                            len(shortest_path_in_complete_grid)
    return shortest_final_grid_len_to_shortest_full_grid_len


# run a-star on explored grid to find the shortest path in the final grid
def compute_explored_grid_path(search, start_state, goal_state):
    explored_grid = search.get_explored_grid()
    return Search.generic_a_star(explored_grid, start_state, goal_state, search.get_heuristic_function())


# run a-star on the complete grid
def compute_full_grid_path(search, grid, start_state, goal_state):
    return Search.generic_a_star(grid, start_state, goal_state, search.get_heuristic_function())


# Initialize search class to run test on given set of probabilities and find all the metrics in q6
def conduct_tests(field_of_view):
    avg_trajectory_len = []
    avg_of_trajectory_to_shortest_explored_grid_len = []
    avg_of_shortest_final_grid_len_to_shortest_full_grid_len = []
    avg_of_cells_processed = []
    for probability in PROBABILITIES:
        total_traversed_path_len = 0  # total length of actual  path
        total_trajectory_to_shortest_explored_grid_len = 0  # total length of shortest path in final grid world
        total_shortest_final_grid_len_to_shortest_full_grid_len = 0  # total length of shortest path in complete grid world
        total_cells_processed = 0
        solvability = 0
        for test_index in range(TEST_COUNT):
            grid, start_state, goal_state, search = initialize_test_variables(probability, field_of_view)
            search.solve_maze()

            # We want to collect metrics only for solved tests except in the case of cells processed
            if search.is_maze_solved():
                solvability += 1
            shortest_path_in_explored_grid = compute_explored_grid_path(search, start_state, goal_state)
            shortest_path_in_complete_grid = compute_full_grid_path(search, grid, start_state, goal_state)

            total_traversed_path_len += get_traversed_path_len(search)
            total_trajectory_to_shortest_explored_grid_len += \
                get_trajectory_len_to_shortest_grid_len(search, shortest_path_in_explored_grid)
            total_shortest_final_grid_len_to_shortest_full_grid_len += \
                get_final_grid_len_to_shortest_full_grid_len(shortest_path_in_explored_grid, shortest_path_in_complete_grid)
            total_cells_processed += search.get_cells_processed()

        # metrics to measure
        # 1 total trajectory len
        # 2 total explored grid len/ total complete grid len
        # 3 total trajectory len/ total explored grid len
        # 4 total cells processed
        avg_trajectory_len.append(total_traversed_path_len / solvability)
        avg_of_trajectory_to_shortest_explored_grid_len.append(
            total_trajectory_to_shortest_explored_grid_len / solvability)
        avg_of_shortest_final_grid_len_to_shortest_full_grid_len.append(
            total_shortest_final_grid_len_to_shortest_full_grid_len / solvability)
        avg_of_cells_processed.append(total_cells_processed / TEST_COUNT)

    return avg_trajectory_len, avg_of_trajectory_to_shortest_explored_grid_len, \
        avg_of_shortest_final_grid_len_to_shortest_full_grid_len, avg_of_cells_processed


def generate_graphs(x, y1, y2, y3, y4):
    print(x, y1, y2, y3, y4)
    generate_graph(x, y1, "Density vs Average Trajectory Length", "Density", "Average of trajectory length", "")
    generate_graph(x, y2, "Density vs Avg (Trajectory Path/ Shortest Path on Final Grid",
                   "Density", "Avg (Trajectory Path/ Shortest Path on Final Grid")
    generate_graph(x, y3, "Density vs Avg (Shortest Path of Final grid/ Shortest path in Full grid)",
                   "Density", "Avg (Shortest Path of Final grid/ Shortest path in Full grid)")
    generate_graph(x, y4, "Density vs Avg Cells Processed", "Density", "Avg Cells Processed")


# metrics are in the order as given in q6
def run_performance_tests(field_of_view):
    metric1, metric2, metric3, metric4 = conduct_tests(field_of_view)
    generate_graphs(PROBABILITIES, metric1, metric2, metric3, metric4)


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
