from Entity.Agent.Agent import Agent


class ExampleSensingAgent(Agent):
    def __init__(self, complete_grid, goal_state, heuristic_function, heuristic_weight):
        super().__init__(complete_grid, goal_state, heuristic_function, heuristic_weight)

    def update_explored_grid(self, explored_grid, state):
        pass

    def follow_path(self, explored_grid, path):
        pass
