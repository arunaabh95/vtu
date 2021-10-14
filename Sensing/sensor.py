from Entity.SensedState import SensedState
from Sensing.KnowledgeBase import *
from Main.util import *


def process_state(state, grid):
    sensed_state = SensedState(state.x, state.y, grid)
    compute_sensing_metrics(sensed_state, grid)
    return sensed_state


def compute_sensing_metrics(state, grid):
    neighbors = SensedState.generate_neighbors(state, grid)
    sensed_count = calculate_sensed_blocks(neighbors, grid)
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

    state.set_empty(empty_cell_count)
    state.set_sensed(sensed_count)
    state.set_blocked(blocked_cell_count)
    state.set_uncertain(uncertain_cell_count)
