from Entity.Agent.Agent import Agent
from Main.util import *
from Sensing.BasicInferenceAgent import InferenceEngine
from Sensing.sensor import *
from Constants.environment_constants import *


class ExampleSensingAgent(Agent):
    def __init__(self, complete_grid, goal_state, heuristic_function, heuristic_weight):
        reset_knowledge_base()
        self.inference_engine = InferenceEngine(complete_grid)
        super().__init__(complete_grid, goal_state, heuristic_function, heuristic_weight)

    def update_explored_grid(self, explored_grid, state):
        explored_grid[state.x][state.y] = 1

    def follow_path(self, explored_grid, path, data=None):
        final_state = None
        for state in path:
            sensed_state = process_state(state, self.complete_grid)
            # print_state(sensed_state)

            # The above were pre execution steps we do not check complete grid as of now so no real execution
            # if we encounter an block in our path we check for final state and also mark it as blocked
            if self.complete_grid[state.x][state.y] == 1:
                self.update_explored_grid(explored_grid, state)
                self.inference_engine.update_neighbors(sensed_state, BLOCKED_STATE)
                self.update_parent(state.parent_state, explored_grid)
                final_state = state.parent_state
                break

            data[len(data) - 1].append(explored_grid)
            data[len(data) - 1].append([state.x - data[len(data) - 1][0][0], state.y - data[len(data) - 1][0][1]])
            data.append([[state.x, state.y]])
            # if we have found the goal state then also we should return
            if state.x == self.goal_state.x and state.y == self.goal_state.y:
                self.bumped = False
                final_state = state
                break

            InferenceEngine.infer(sensed_state, explored_grid)

            blocked_by_inference = self.infer_to_block(sensed_state, explored_grid, path)

            if blocked_by_inference:
                final_state = state
                break

            # print_state(sensed_state)

        return final_state

    def infer_to_block(self, sensed_state, explored_grid, path):
        blocked_by_inference = False

        # If post inference we find path is blocked
        if is_path_blocked(explored_grid, path):
            InferenceEngine.infer(sensed_state, explored_grid)
            self.bumped = False
            blocked_by_inference = True

        return blocked_by_inference

    def has_bumped(self):
        return self.bumped

    def update_parent(self, parent_state, explored_grid):
        sensed_state = process_state(parent_state, self.inference_engine.complete_grid)
        InferenceEngine.infer(sensed_state, explored_grid)
