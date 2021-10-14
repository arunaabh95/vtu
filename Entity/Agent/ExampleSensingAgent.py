from Entity.Agent.Agent import Agent
from Main.util import *
from Sensing.InferenceEngine import InferenceEngine
from Sensing.sensor import *


class ExampleSensingAgent(Agent):
    def __init__(self, complete_grid, goal_state, heuristic_function, heuristic_weight):
        self.inference_engine = InferenceEngine(complete_grid)
        super().__init__(complete_grid, goal_state, heuristic_function, heuristic_weight)

    def update_explored_grid(self, explored_grid, state):
        explored_grid[state.x][state.y] = 1
        self.inference_engine.update_kb(state)

    def follow_path(self, explored_grid, path):
        final_state = None
        for state in path:
            sensed_state = process_state(state, self.complete_grid)
            self.inference_engine.infer(sensed_state, explored_grid)

            # If post inference we find path is blocked
            if is_path_blocked(explored_grid, path):
                self.bumped = False
                final_state = state
                break

            # if we encounter an block in our path we check for final state and also mark it as blocked
            if self.complete_grid[state.x][state.y] == 1:
                self.update_explored_grid(explored_grid, state)
                final_state = state.parent_state
                break

            # if we have found the goal state then also we should return
            if state.x == self.goal_state.x and state.y == self.goal_state.y:
                self.bumped = False
                final_state = state
                break

        return final_state


    def has_bumped(self):
        return self.bumped
