from Entity.State import State
from Main.util import *
from Constants.environment_constants import *


class Agent:
    # An Agent should can either see in compass directions or can only see in the direction of motion
    # We have passed heuristic function just to compute the h(x) of the children and this is a design flaw
    def __init__(self, complete_grid, goal_state, heuristic_function, heuristic_weight, restrict_field_view_flag):
        self.complete_grid = complete_grid
        self.heuristic_function = heuristic_function
        self.restrict_field_view_flag = restrict_field_view_flag
        self.heuristic_weight = heuristic_weight
        self.goal_state = goal_state

    # update the explored grid based on the path traversed by the agent
    # view all children and update blocks in explored_grid
    def update_explored_grid(self, explored_grid, state):
        children = State.get_children(state, self.goal_state, explored_grid,
                                      self.heuristic_function, self.heuristic_weight)
        for child in children:
            if self.complete_grid[child.x][child.y] == 1:
                explored_grid[child.x][child.y] = 1

    # return the first blocked cell while the agent is traversing the path given to it by the planner
    # Once the agent is stuck it will return the position of the last block it is stuck on
    # We have also included the functionality to update the grid as the agent is traversing it
    def follow_path(self, explored_grid, path, data):
        final_state = None
        for state in path:
            data.append([[state.parent_state.x, state.parent_state.y], explored_grid, [state.x - state.parent_state.x, state.y - state.parent_state.y]])
            # IF the agent is blind we do not need to update the neighbours of the explored grid
            if self.restrict_field_view_flag == ALLOW_FIELD_OF_VIEW:
                self.update_explored_grid(explored_grid, state)

            # if we encounter an block in our path we check for final state and also mark it as blocked
            if self.complete_grid[state.x][state.y] == 1:
                explored_grid[state.x][state.y] = 1
                final_state = state.parent_state
                break

            # if we have found the goal state then also we should return
            if state.x == self.goal_state.x and state.y == self.goal_state.y:
                final_state = state
                break

        return final_state
