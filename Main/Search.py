from Main.util import *
from Constants.environment_constants import *
from Entity.Agent import Agent
from Entity.Heuristics import Heuristics
import time


class Search:

    def __init__(self, grid, start_state, goal_state, heuristics_flag=MANHATTAN_HEURISTICS,
                 restrict_field_of_view=ALLOW_FIELD_OF_VIEW, search_type=A_STAR, heuristic_weight=1):
        # Basic Variables
        self.grid = grid
        self.start_state = start_state
        self.goal_state = goal_state

        # Runtime entities
        self.agent = None
        self.heuristics_function = None
        self.search_function = None

        # Algorithm flags
        self.heuristics_flag = heuristics_flag
        self.heuristics_weight = heuristic_weight
        self.restrict_field_of_view = restrict_field_of_view
        self.search_type = search_type

        # Analytics
        self.cells_traversed = 0
        self.final_path = []
        self.explored_grid = [[0]]
        self.time = 0
        # self.final_state is not used by us but can be used if we want to see where the algorithm got stuck in the maze
        self.final_state = None

    # All functions to get search state variables
    def get_search_time(self):
        return self.time

    def get_cells_processed(self):
        return self.cells_traversed

    def get_path_length(self):
        return len(self.final_path)

    def is_maze_solved(self):
        return len(self.final_path) > 0

    def get_final_path(self):
        return self.final_path

    def get_explored_grid(self):
        return self.explored_grid

    def get_heuristic_function(self):
        return self.heuristics_function

    def initialize_entities(self):
        grid_size = len(self.grid)
        self.explored_grid = make_empty_grid(grid_size)
        self.heuristics_function = Heuristics.get_heuristic_function(self.heuristics_flag, self.heuristics_weight)
        self.agent = Agent(self.grid, self.goal_state, self.heuristics_function, self.heuristics_weight,
                           self.restrict_field_of_view)
        if self.search_type == A_STAR:
            self.search_function = self.a_star
        elif self.search_type == BFS:
            self.search_function = self.bfs
        else:
            self.search_function = self.a_star

        self.final_path.append(self.start_state)

    # main function to solve the maze
    def solve_maze(self):
        self.initialize_entities()
        start_timer = time.perf_counter()
        # call astar algorithm until we find the maze or fail to do so
        while True:
            # print(explored_grid)
            path = self.search_function()

            # unable  to solve the maze
            if len(path) == 0:
                print("No path found")
                self.final_path = []
                return

            if path[len(path) - 1] == self.goal_state:
                final_state = self.agent.follow_path(self.explored_grid, path)
                add_to_final_path(self.final_path, self.start_state, final_state)
                if final_state == self.goal_state:
                    self.time = time.perf_counter() - start_timer
                    return
                self.start_state = final_state


    # This a-star takes information from the search class
    def a_star(self):
        # initializing open list, closed list and path variables then adding start node to the open list
        priority_queue = []
        heap.heappush(priority_queue, self.start_state)
        closed_list = set()

        while len(priority_queue) > 0:

            current_state = heap.heappop(priority_queue)
            closed_list.add(current_state)

            if current_state == self.goal_state:
                self.cells_traversed += len(closed_list)
                return find_path(self.start_state, current_state)

            children = State.get_children(current_state, self.goal_state, self.explored_grid, self.heuristics_function, self.heuristics_weight)

            if len(children) == 0:
                continue

            for child in children:
                if child in closed_list:
                    continue

                old_state = get_element_from_list(priority_queue, child)

                if old_state is None:
                    heap.heappush(priority_queue, child)
                # if we see that the path to current child is smaller than the existing path in the open list
                # we update the node in open list
                elif closer_from_start(old_state, child):
                    update_with_child(priority_queue, child, old_state)

        # we calculate cells precessed even when we do not get any result
        self.cells_traversed += len(closed_list)
        return []

    # redundant duplication we use this to run astar on complete/ final grid for questions post q5
    @staticmethod
    def generic_a_star(grid, start_state, goal_state, heuristics_function):
        # initializing open list, closed list and path variables then adding start node to the open list
        priority_queue = []
        heap.heappush(priority_queue, start_state)
        closed_list = set()

        while len(priority_queue) > 0:
            # print_list(priority_queue)
            current_state = heap.heappop(priority_queue)
            closed_list.add(current_state)

            if current_state == goal_state:
                # print(current_state.x, " Goal ", current_state.y )
                return find_path(start_state, current_state)

            children = State.get_children(current_state, goal_state, grid, heuristics_function)

            if len(children) == 0:
                continue

            for child in children:
                if child in closed_list:
                    continue

                old_state = get_element_from_list(priority_queue, child)

                if old_state is None:
                    heap.heappush(priority_queue, child)
                elif closer_from_start(old_state, child):
                    update_with_child(priority_queue, child, old_state)
        return []

    # general bfs implementation
    def bfs(self):
        # initializing open list, closed list and path variables then adding start node to the open list
        queue = [self.start_state]
        closed_list = set()

        while len(queue) > 0:
            # print_list(priority_queue)
            current_state = queue.pop(0)
            closed_list.add(current_state)

            if current_state == self.goal_state:
                # print(current_state.x, " Goal ", current_state.y )
                self.cells_traversed += len(closed_list)
                return find_path(self.start_state, current_state)

            children = State.get_children(current_state, self.goal_state, self.explored_grid, self.heuristics_function)

            if len(children) == 0:
                continue
            for child in children:
                if child in closed_list:
                    continue

                queue.append(child)
                closed_list.add(child)

        self.cells_traversed += len(closed_list)
        return []

    # bfs implementation for extra credits
    @staticmethod
    def generic_bfs(grid, start_state, goal_state, heuristics_function):
        # initializing open list, closed list and path variables then adding start node to the open list
        queue = [start_state]
        closed_list = set()

        while len(queue) > 0:
            # print_list(priority_queue)
            current_state = heap.heappop(queue)
            closed_list.add(current_state)

            if current_state == goal_state:
                # print(current_state.x, " Goal ", current_state.y )
                return find_path(start_state, current_state)

            children = State.get_children(current_state, goal_state, grid, heuristics_function)

            if len(children) == 0:
                continue

            for child in children:
                if child in closed_list:
                    continue
                queue.append(child)
                closed_list.add(child)
        return []
