from math import sqrt
from Entity.State import State
import heapq as heap


def get_manhattan(x, y, goal):
    return abs(x-goal.x) + abs(y - goal.y)


def get_euclidean(x, y, state2):
    return sqrt(pow(abs(state2.x - x), 2) + pow(abs(state2.y - y), 2))


def get_chebyshev(x, y, state2):
    return max(abs(state2.x - x), abs(y - state2.y))


def get_children(parent, goal, grid, heuristic):
    children = []

    x = parent.x
    y = parent.y
    if y > 0 and grid[x][y - 1] == 0:
        upper_child = State(x, y - 1, grid[x][y - 1], parent.gx + 1,
                            heuristic(x, y - 1, goal), parent)
        children.append(upper_child)

    if y < len(grid) - 1 and grid[x][y + 1] == 0:
        lower_child = State(x, y + 1, grid[x][y + 1], parent.gx + 1,
                            heuristic(x, y + 1, goal), parent)
        children.append(lower_child)

    if x > 0 and grid[x - 1][y] == 0:
        left_child = State(x - 1, y, grid[x - 1][y], parent.gx + 1,
                           heuristic(x - 1, y, goal), parent)
        children.append(left_child)

    if x < len(grid) - 1 and grid[x + 1][y] == 0:
        right_child = State(x + 1, y, grid[x + 1][y], parent.gx + 1,
                            heuristic(x + 1, y, goal), parent)
        children.append(right_child)

    return children


def get_element_from_list(input_list, element):
    for i in input_list:
        if i == element:
            return i
    return None


def closer_from_start(old_state, new_state):
    return new_state.gx < old_state.gx


def update_with_child(input_list, key, new_key):
    i = 0
    while i < len(input_list):
        element = input_list[i]
        if element == key:
            input_list[i] = input_list[-1]
            input_list.pop()
            heap.heapify(input_list)
            heap.heappush(input_list, new_key)
            break
        i += 1


def find_path(start_state, end_state):
    path = []
    temp_state = end_state
    while temp_state != start_state:
        path.insert(0, temp_state)
        temp_state = temp_state.parent_state
    return path


def add_to_final_path(final_path, start_state, final_state):
    final_path += find_path(start_state, final_state)


def print_path(path):
    print("x  y gx  hx  fx")
    for state in path:
        print(state.x, "  ", state.y, " ", state.gx, "  ", state.hx, "  ", state.get_fx())


def print_list(input_list):
    for element in input_list:
        print(element.x, "   ", element.y)
'''

0    0   0    19    19
0    1   1    17    18
0    1   1    17    18
1    1   2    16    18
2    1   3    15    18
2    2   4    14    18
3    2   5    13    18
3    3   6    12    18
4    3   7    11    18
5    3   8    10    18
5    3   8    10    18
6    3   9    9    18
7    3   10    8    18
7    4   11    7    18
7    4   11    7    18
7    5   12    6    18
7    5   12    6    18
7    4   13    7    20
7    3   14    8    22
7    2   15    9    24
8    2   16    8    24
9    2   17    7    24
9    3   18    6    24
9    4   19    5    24
9    5   20    4    24
9    6   21    3    24
9    7   22    2    24
9    8   23    1    24
9    9   24    0    24

[[0. 0. 1. 0. 1. 0. 0. 1. 0. 0.]
 [0. 0. 1. 1. 1. 0. 1. 1. 0. 0.]
 [1. 0. 0. 1. 1. 0. 0. 0. 1. 0.]
 [1. 1. 0. 0. 1. 1. 0. 0. 1. 0.]
 [1. 1. 0. 0. 1. 0. 0. 1. 0. 0.]
 [1. 1. 1. 0. 1. 1. 0. 1. 0. 0.]
 [0. 0. 0. 0. 1. 1. 1. 1. 0. 0.]
 [1. 0. 0. 0. 0. 0. 1. 0. 0. 0.]
 [0. 0. 0. 1. 1. 1. 1. 1. 1. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
'''
