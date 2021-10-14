
empty_cells = set()
blocked_cells = set()
uncertain_cells = set()
visited = set()


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

