import sys


class State:
    def __init__(self, x, y, is_blocked, gx, hx, parent_state=None):
        self.x = x
        self.y = y
        self.is_blocked = is_blocked
        self.gx = gx
        self.hx = hx
        self.fx = gx + hx
        self.parent_state = parent_state

    def __eq__(self, other):
        if isinstance(other, State):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

        # override the comparison operator

    def __lt__(self, nxt):
        if isinstance(nxt, State):
            return self.get_fx() < nxt.get_fx()
        return -1

    def x(self):
        return self.x

    def y(self):
        return self.y

    def get_fx(self):
        return self.gx + self.hx

    def gx(self):
        return self.gx

    def hx(self):
        return self.hx

    def parent_state(self):
        return self.parent_state

    def is_blocked(self):
        return self.is_blocked

    def mark_blocked(self):
        self.is_blocked = True

    @staticmethod
    def get_children(parent, goal, grid, heuristic, heuristic_weight=1):
        children = []

        x = parent.x
        y = parent.y
        if y > 0 and grid[x][y - 1] == 0:
            upper_child = State(x, y - 1, grid[x][y - 1], parent.gx + 1,
                                heuristic(x, y - 1, goal, heuristic_weight), parent)
            children.append(upper_child)

        if y < len(grid) - 1 and grid[x][y + 1] == 0:
            lower_child = State(x, y + 1, grid[x][y + 1], parent.gx + 1,
                                heuristic(x, y + 1, goal, heuristic_weight), parent)
            children.append(lower_child)

        if x > 0 and grid[x - 1][y] == 0:
            left_child = State(x - 1, y, grid[x - 1][y], parent.gx + 1,
                               heuristic(x - 1, y, goal, heuristic_weight), parent)
            children.append(left_child)

        if x < len(grid) - 1 and grid[x + 1][y] == 0:
            right_child = State(x + 1, y, grid[x + 1][y], parent.gx + 1,
                                heuristic(x + 1, y, goal, heuristic_weight), parent)
            children.append(right_child)

        return children

