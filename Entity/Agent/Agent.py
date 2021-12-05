class Agent:
    def __init__(self, complete_grid, goal_state, heuristic_function, heuristic_weight):
        self.complete_grid = complete_grid
        self.heuristic_function = heuristic_function
        self.heuristic_weight = heuristic_weight
        self.goal_state = goal_state
        self.bumped = True

    def update_explored_grid(self, explored_grid, state):
        pass

    def follow_path(self, explored_grid, path, data=None):
        pass

    def has_bumped(self):
        pass
