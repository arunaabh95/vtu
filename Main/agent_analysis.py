from Entity.Grid import Grid
from Main.Search import Search
from Main.util import *
from Constants.environment_constants import *
from Main.voyage import get_default_states

PROBABILITIES = [0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4]
TEST_COUNT = GLOBAL_TEST_COUNT
GRID_SIZE = GLOBAL_BIG_MAZE_SIZE
# TODO: arunaabh95 add 4th agent in the array
AGENTS = [ALLOW_FIELD_OF_VIEW, RESTRICT_FIELD_OF_VIEW, ALLOW_BASIC_SENSING]

# Metrics to calculate
# total trajectory_len = path length - from performance_analysis.py
# bump count - calculated from search
# time - calculated from search
# final path length in discovered grid world = path_length - backtracks - do not know answer to this


def agent_analysis():
    avg_bumps, avg_time, avg_trajectory_length, avg_final_path_length = conduct_tests()
    generate_graphs(avg_bumps, avg_time, avg_trajectory_length, avg_final_path_length)


def initialize_test_variables(probability):
    grid = Grid.make_grid(probability, GRID_SIZE)
    start_state, goal_state = get_default_states(grid)
    return grid, start_state, goal_state


def get_final_path_length(search, start_state, goal_state):
    explored_grid = search.get_explored_grid()
    final_path = set([(str(state.x) + "_" + str(state.y)) for state in search.get_final_path()])
    for i in range(len(explored_grid)):
        for j in range(len(explored_grid)):
            if (str(i) + "_" + str(j)) in final_path:
                explored_grid[i][j] = 0
            else:
                explored_grid[i][j] = 1
    return len(Search.generic_a_star(explored_grid, start_state, goal_state, search.get_heuristic_function()))


def conduct_tests():
    average_bumps = []
    average_trajectory_length = []
    average_final_path_length = []
    average_time = []

    for probability in PROBABILITIES:
        avg_bumps_for_probability = []
        avg_trajectory_length_for_probability = []
        avg_time_for_probability = []
        avg_final_path_length_for_probability = []  # ambiguous
        total_bumps = []
        total_time = []
        total_trajectory_length = []
        total_final_path_length = []
        test_count = [TEST_COUNT] * 3
        # if the test_index = 0 does not have a solution then we need this variable to store the first record per agent
        # so we increase it to agent length so we have added one metric for each agent and then break
        first_record = 0
        for test_index in range(TEST_COUNT):
            i = 0
            grid, start_state, goal_state = initialize_test_variables(probability)
            while i < len(AGENTS):
                search = Search(grid, start_state, goal_state, restrict_field_of_view=AGENTS[i])
                search.solve_maze()
                if search.get_path_length() == 0:
                    test_count[i] -= 1     
                final_path_length = get_final_path_length(search, start_state, goal_state)
                print("Agent ", i, search.get_planning_time(), search.get_bump_count(), search.get_path_length())
                if first_record < len(AGENTS):
                    total_bumps.append(search.get_bump_count())
                    total_time.append(search.get_planning_time())
                    total_trajectory_length.append(search.get_path_length())
                    total_final_path_length.append(final_path_length)
                    first_record += 1
                else:
                    total_bumps[i] += search.get_bump_count()
                    total_trajectory_length[i] += search.get_path_length()
                    total_time[i] += search.get_planning_time()
                    total_final_path_length[i] += final_path_length
                i += 1

        i = 0
        while i < len(AGENTS):
            avg_bumps_for_probability.append(total_bumps[i]/test_count[i])
            avg_time_for_probability.append(total_time[i]/test_count[i])
            avg_trajectory_length_for_probability.append(total_trajectory_length[i]/test_count[i])
            avg_final_path_length_for_probability.append(total_final_path_length[i]/test_count[i])
            i += 1

        average_bumps.append(avg_bumps_for_probability)
        average_time.append(avg_time_for_probability)
        average_trajectory_length.append(avg_trajectory_length_for_probability)
        average_final_path_length.append(avg_final_path_length_for_probability)

    return transpose(average_bumps), transpose(average_time), transpose(average_trajectory_length), transpose(average_final_path_length)


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def generate_graphs(avg_bump_count, avg_time, avg_trajectory_length, avg_final_path_length):
    print(avg_bump_count)
    print(avg_trajectory_length)
    print(avg_final_path_length)
    print(avg_time)
    generate_graph(PROBABILITIES, avg_bump_count,
                   "Average Bumps Analysis", "Probability", "Bump Counts",
                   ["Full View Agent", "No View Agent", "Basic Sensing Agent"])
    generate_graph(PROBABILITIES, avg_time,
                   "Average Time Analysis", "Probability", "Avg Time",
                   ["Full View Agent", "No View Agent", "Basic Sensing Agent"])
    generate_graph(PROBABILITIES, avg_trajectory_length,
                   "Average Trajectory Length", "Probability", "Avg Trajectory Length",
                   ["Full View Agent", "No View Agent", "Basic Sensing Agent"])
    generate_graph(PROBABILITIES, avg_final_path_length,
                   "Average Full Path Length", "Probability", "Avg Final Path Length",
                    ["Full View Agent", "No View Agent", "Basic Sensing Agent"])


agent_analysis()
