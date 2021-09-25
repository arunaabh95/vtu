from Main.util import *


class Agent:

    @staticmethod
    def update_explored_grid(complete_grid, explored_grid, state, goal, heuristic):
        # update the explored gate with the path
        # view all children an update blocks in explored_grid
        children = get_children(state, goal, explored_grid, heuristic)
        for child in children:
            if complete_grid[child.x][child.y] == 1:
                explored_grid[child.x][child.y] = 1

    @staticmethod
    def follow_path(complete_grid, explored_grid, path, goal, heuristic, field_view):
        final_state = None
        for state in path:
            if field_view == 1:
                Agent.update_explored_grid(complete_grid, explored_grid, state, goal, heuristic)

            # if we encounter an block in our path we check for final state and also mark it as blocked
            if complete_grid[state.x][state.y] == 1:
                explored_grid[state.x][state.y] = 1
                final_state = state.parent_state
                break

            # if we have found the goal state then also we should return
            if state.x == goal.x and state.y == goal.y:
                final_state = state
                break

        return final_state
