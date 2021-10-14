from Entity.Agent.Agent import Agent


class FinalSensingAgent(Agent):
    def __init__(self, complete_grid, goal_state, heuristic_function, heuristic_weight):
        super().__init__(complete_grid, goal_state, heuristic_function, heuristic_weight)

    def update_explored_grid(self, explored_grid, state):
        pass

    def follow_path(self, explored_grid, path):
        final_state = None
        for state in path:

            # if we encounter an block in our path we check for final state and also mark it as blocked
            if self.complete_grid[state.x][state.y] == 1:
                explored_grid[state.x][state.y] = 1
                final_state = state.parent_state
                break

            # if we have found the goal state then also we should return
            if state.x == self.goal_state.x and state.y == self.goal_state.y:
                final_state = state
                self.bumped = False
                break

        return final_state

    def has_bumped(self):
        return self.bumped
