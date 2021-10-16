from Entity.SensedState import SensedState
from Sensing.KnowledgeBase import *
from Constants.environment_constants import *
from Main.util import *


class InferenceEngine:

    def __init__(self, complete_grid):
        self.complete_grid = complete_grid
        self.path = None
        initialize_sensed_grid(complete_grid)

    @staticmethod
    def infer(state, explored_grid):
        if is_visited(state) or state.get_uncertain() == 0:
            return
        InferenceEngine.apply_rules(state, explored_grid)
        mark_visited(state)

    @staticmethod
    def apply_rules(state, explored_grid):
        neighbors = state.get_neighbors()
        if state.get_sensed() == state.get_blocked():
            state.set_empty(state.get_empty() + state.get_uncertain())
            state.set_uncertain(0)
            InferenceEngine.mark_all_uncertain_cells_empty(neighbors)
        if len(neighbors) - state.get_sensed() == state.get_empty():
            state.set_blocked(state.get_blocked() + state.get_uncertain())
            state.set_uncertain(0)
            InferenceEngine.mark_all_uncertain_cells_blocked(explored_grid, neighbors)
        InferenceEngine.update_current_state(state, explored_grid)

    @staticmethod
    def mark_all_uncertain_cells_empty(cells):
        for cell in cells:
            if is_uncertain(cell):
                remove_uncertain(cell)
                mark_empty(cell)
                add_to_sensed_grid(cell)

    @staticmethod
    def mark_all_uncertain_cells_blocked(explored_grid, cells):
        for cell in cells:
            if is_uncertain(cell):
                remove_uncertain(cell)
                mark_blocked(cell)
                explored_grid[cell.x][cell.y] = 1
                add_to_sensed_grid(cell)

    @staticmethod
    def update_neighbors(cell, cell_state):
        neighbors = cell.get_neighbors()
        for neighbor in neighbors:
            if is_visited(neighbor):
                continue
            if cell_state == BLOCKED_STATE:
                neighbor.set_blocked(neighbor.get_blocked() + 1)
            if cell_state == EMPTY_STATE:
                neighbor.set_empty(neighbor.get_empty() + 1)
            if is_in_sensed_grid(neighbor.x, neighbor.y) and neighbor.get_nx() > 0:
                neighbor.set_uncertain(neighbor.get_uncertain() - 1)
            add_to_sensed_grid(neighbor)

    @staticmethod
    def update_current_state(state, explored_grid):
        if explored_grid[state.x][state.y] == 0:
            remove_uncertain(state)
            mark_empty(state)
            InferenceEngine.update_neighbors(state, EMPTY_STATE)
        else:
            remove_uncertain(state)
            mark_blocked(state)
            InferenceEngine.update_neighbors(state, BLOCKED_STATE)
        add_to_sensed_grid(state)
