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

