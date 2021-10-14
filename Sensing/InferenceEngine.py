from Entity.SensedState import SensedState
from Sensing.KnowledgeBase import *


class InferenceEngine:

    def __init__(self, complete_grid):
        self.complete_grid = complete_grid
        self.path = None

    def infer(self, state, explored_grid):
        if is_visited(state):
            return
        self.apply_rules(state, explored_grid)
        mark_visited(state)

    def apply_rules(self, state, explored_grid):
        neighbors = state.get_neighbors()
        if state.get_sensed() == state.get_blocked():
            self.mark_all_uncertain_cells_empty(neighbors)
        if len(neighbors) - state.get_sensed() == state.get_empty():
            self.mark_all_uncertain_cells_blocked(explored_grid, neighbors)

    @staticmethod
    def mark_all_uncertain_cells_empty(cells):
        for cell in cells:
            if is_uncertain(cell):
                remove_uncertain(cell)
                mark_empty(cell)

    @staticmethod
    def mark_all_uncertain_cells_blocked(explored_grid, cells):
        for cell in cells:
            if is_uncertain(cell):
                remove_uncertain(cell)
                mark_blocked(cell)
                explored_grid[cell.x][cell.y] = 1

    @staticmethod
    def update_kb(cell):
        if is_uncertain(cell):
            uncertain_cells.remove(cell)
            mark_blocked(cell)
            InferenceEngine.update_neighbors(cell)

    @staticmethod
    def update_neighbors(cell):
        neighbors = cell.get_neighbors()
        for neighbor in neighbors:
            if is_visited(neighbor):
                neighbor.set_blocked(neighbor.get_blocked() + 1)
                neighbor.set_uncertian(neighbor.get_uncertain() - 1)

