class SensedState:
    def __init__(self,  x,  y, grid):
        self.x = x
        self.y = y
        self.id = str(x) + "_" + str(y)
        self.complete_grid = grid

        # derived parameters
        self.neighbours = []
        self.sensed_count = 0
        self.blocked_count = 0
        self.empty_count = 0
        self.uncertain_count = 0

    @staticmethod
    def generate_neighbors(state, grid):
        neighbors = []
        positions = [[0, 1], [1, 0], [1, 1], [-1, -1], [-1, 0], [0, -1], [1, -1], [-1, 1]]
        for i in positions:
            if len(grid) > state.x + i[0] >= 0 and len(grid) > state.y + i[1] >= 0:
                neighbors.append(SensedState(state.x + i[0], state.y + i[1], grid))
        return neighbors

    def get_neighbors(self):
        return self.neighbours

    def get_nx(self):
        return len(self.neighbours)

    def __contains__(self, item):
        return self.id == item.id

    def __hash__(self):
        return hash(self.id)

    def set_sensed(self, count):
        self.sensed_count = count

    def set_empty(self, count):
        self.empty_count = count

    def set_blocked(self, count):
        self.blocked_count = count

    def set_uncertain(self, count):
        self.uncertain_count = count

    def get_sensed(self):
        return self.sensed_count

    def get_blocked(self):
        return self.blocked_count

    def get_empty(self):
        return self.empty_count

    def get_uncertain(self):
        return self.uncertain_count
