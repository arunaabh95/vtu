from Entity.SensedState import SensedState
from Sensing.KnowledgeBase import *
from Main.util import *


def process_state(state, grid):
    if is_in_sensed_grid(state.x, state.y):
        sensed_state = get_element_from_sensed_grid(state.x, state.y)
    else:
        sensed_state = SensedState(state.x, state.y, grid)
    compute_sensing_metrics(sensed_state, grid)
    return sensed_state


def compute_sensing_metrics(state, grid):
    neighbors = SensedState.generate_neighbors(state, grid)
    state.set_neighbors(neighbors)
    sensed_count = calculate_sensed_blocks(neighbors, grid)
    if is_in_sensed_grid(state.x, state.y):
        empty_cell_count, blocked_cell_count, uncertain_cell_count = parameterize_existing_state(state, neighbors)
    else:
        empty_cell_count, blocked_cell_count, uncertain_cell_count = parameterize_new_state(neighbors)
    state.set_empty(empty_cell_count)
    state.set_sensed(sensed_count)
    state.set_blocked(blocked_cell_count)
    state.set_uncertain(uncertain_cell_count)
    # print("The boss")
    # print_state(state)


def parameterize_new_state(neighbors):
    empty_cell_count = 0
    blocked_cell_count = 0
    uncertain_cell_count = 0
    for neighbor in neighbors:
        if is_empty(neighbor):
            empty_cell_count += 1
        elif is_blocked(neighbor):
            blocked_cell_count += 1
        else:
            uncertain_cell_count += 1
    return empty_cell_count, blocked_cell_count, uncertain_cell_count


def parameterize_existing_state(state, neighbors):
    empty_cell_count = state.get_empty()
    blocked_cell_count = state.get_blocked()
    uncertain_cell_count = len(neighbors) - empty_cell_count - blocked_cell_count

    return empty_cell_count, blocked_cell_count, uncertain_cell_count
