
empty_cells = set()
blocked_cells = set()
uncertain_cells = set()
visited = set()
sensed_grid = [[]]  # To store neighbors that are not processed


def mark_blocked(cell):
    blocked_cells.add(cell)


def mark_empty(cell):
    empty_cells.add(cell)


def mark_uncertain(cell):
    uncertain_cells.add(cell)


def remove_uncertain(cell):
    if cell in uncertain_cells:
        uncertain_cells.remove(cell)


def is_uncertain(cell):
    return cell in uncertain_cells


def is_empty(cell):
    return cell in empty_cells


def is_blocked(cell):
    return cell in blocked_cells


def mark_visited(cell):
    visited.add(cell)


def is_visited(cell):
    return cell in visited


def initialize_sensed_grid(grid):
    global sensed_grid
    sensed_grid = [[None for i in range(len(grid))] for j in range(len(grid[0]))]


def add_to_sensed_grid(state):
    sensed_grid[state.x][state.y] = state


def is_in_sensed_grid(x, y):
    return sensed_grid[x][y] is not None


def get_element_from_sensed_grid(x, y):
    return sensed_grid[x][y]
