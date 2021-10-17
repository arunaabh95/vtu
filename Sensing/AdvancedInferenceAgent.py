from Entity.SensedState import SensedState
from Sensing.KnowledgeBase import *
from Constants.environment_constants import *
from Main.util import *


class AdvancedInferenceEngine:

    def __init__(self, complete_grid):
        self.complete_grid = complete_grid
        self.path = None
        initialize_sensed_grid(complete_grid)

    @staticmethod
    def infer(state, sensed_state, explored_grid):
        if is_visited(sensed_state) or sensed_state.get_uncertain() == 0:
            return
        AdvancedInferenceEngine.apply_rules(state, sensed_state, explored_grid)
        mark_visited(sensed_state)

    @staticmethod
    def apply_rules(state, sensed_state, explored_grid):
        neighbors = sensed_state.get_neighbors()
        if sensed_state.get_sensed() == sensed_state.get_blocked():
            # print("Old inference ", state.x, "  ", state.y)
            sensed_state.set_empty(sensed_state.get_empty() + sensed_state.get_uncertain())
            sensed_state.set_uncertain(0)
            AdvancedInferenceEngine.mark_all_uncertain_cells_empty(neighbors)
        if len(neighbors) - sensed_state.get_sensed() == sensed_state.get_empty():
            # print("Old Inference ", state.x, "  ", state.y)
            sensed_state.set_blocked(sensed_state.get_blocked() + sensed_state.get_uncertain())
            sensed_state.set_uncertain(0)
            AdvancedInferenceEngine.mark_all_uncertain_cells_blocked(explored_grid, neighbors)
        AdvancedInferenceEngine.apply_inference_with_parent(state, sensed_state, explored_grid)
        AdvancedInferenceEngine.update_current_state(sensed_state, explored_grid)

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
                AdvancedInferenceEngine.block_cell(cell, explored_grid)

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
            AdvancedInferenceEngine.update_neighbors(state, EMPTY_STATE)
        else:
            remove_uncertain(state)
            mark_blocked(state)
            AdvancedInferenceEngine.update_neighbors(state, BLOCKED_STATE)
        add_to_sensed_grid(state)

    @staticmethod
    def apply_inference_with_parent(state, sensed_state, explored_grid):
        parent = state.parent_state
        if parent is None:
            return
        sensed_parent = get_element_from_sensed_grid(parent.x, parent.y)
        if sensed_state.get_uncertain() - sensed_parent.get_uncertain() == 3:
            print("vignesh chutiya ", state.x, "  ", state.y)
            neighbors = sensed_state.get_neighbors()
            for neighbor in neighbors:
                # do not change parent or any cell that is not in uncertain already
                if (neighbor.x == sensed_parent.x and neighbor.y == sensed_parent.y) or not is_uncertain(neighbor):
                    continue
                # if parent was on left
                if sensed_parent.x == sensed_state.x - 1:
                    if neighbor.x == sensed_state.x + 1:
                        AdvancedInferenceEngine.block_cell(neighbor, explored_grid)
                        AdvancedInferenceEngine.update_neighbors(neighbor, BLOCKED_STATE)
                # if parent was on right
                if sensed_parent.x == sensed_state.x + 1:
                    if neighbor.x == sensed_state.x-1:
                        AdvancedInferenceEngine.block_cell(neighbor, explored_grid)
                        AdvancedInferenceEngine.update_neighbors(neighbor,BLOCKED_STATE)
                # if parent was below
                if sensed_parent.y == sensed_state.y - 1:
                    if neighbor.y == sensed_state.y + 1:
                        AdvancedInferenceEngine.block_cell(neighbor, explored_grid)
                        AdvancedInferenceEngine.update_neighbors(neighbor, BLOCKED_STATE)
                # if parent was above
                if sensed_parent.y == sensed_state.y - 1:
                    if neighbor.y == sensed_state.y - 1:
                        AdvancedInferenceEngine.block_cell(neighbor, explored_grid)
                        AdvancedInferenceEngine.update_neighbors(neighbor, BLOCKED_STATE)

    @staticmethod
    def block_cell(cell, explored_grid):
        remove_uncertain(cell)
        mark_blocked(cell)
        explored_grid[cell.x][cell.y] = 1
        add_to_sensed_grid(cell)
