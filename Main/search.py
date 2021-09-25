from Entity.Grid import Grid
from Entity.Agent import Agent
from Main.util import *
import time

GRID_SIZE = 101
HEURISTIC = get_manhattan
FIELD_VIEW = 1
GET_EXPLORED_GRID = 0


def initialize_search(complete_grid, grid_size):
    # initialize start state and goal state
    # describe the parameters of start and end state
    explored_grid = Grid.make_grid(0, grid_size)
    start = State(0, 4, complete_grid[0][4], 0, grid_size + grid_size - 1)
    goal = State(grid_size - 1, grid_size - 1, complete_grid[grid_size - 1][grid_size - 1], 0, 0)
    return explored_grid, start, goal


# main function to implement repeated A-start algorithm
def solve_maze(complete_grid, grid_size, heuristic=HEURISTIC, field_view=FIELD_VIEW,
               get_explored_grid=GET_EXPLORED_GRID):

    start, goal, explored_grid = initialize_search(complete_grid, grid_size)
    final_path = [start]

    # call astar algorithm until we find the maze or fail to do so
    while True:
        #print(explored_grid)
        path = a_star(explored_grid, start, goal, heuristic)

        # unable  to solve the maze
        if len(path) == 0:
            print("No path found")
            return []

        if path[len(path) - 1] == goal:
            final_state = Agent.follow_path(complete_grid, explored_grid, path, goal, heuristic, field_view)

            add_to_final_path(final_path, start, final_state)
            if final_state == goal:
                if get_explored_grid:
                    return final_path, explored_grid
                else:
                    return final_path
            start = final_state


def a_star(grid, start, goal, heuristic):
    # initializing open list, closed list and path variables then adding start node to the open list
    priority_queue = []
    heap.heappush(priority_queue, start)
    closed_list = set()
    while len(priority_queue) > 0:
       # print_list(priority_queue)
        current_state = heap.heappop(priority_queue)
        closed_list.add(current_state)
      #  print("Current State: ", current_state.x, "  ", current_state.y, "  ", current_state.gx, "   ", current_state.hx)

        if current_state == goal:
            # print(current_state.x, " Goal ", current_state.y )
            return find_path(start, current_state)

        children = get_children(current_state, goal, grid, heuristic)

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


def voyage_on_grid(grid):
    start, goal, explored_grid = initialize_search(grid, len(grid))


def voyage():
    grid = Grid.make_grid(0.3, GRID_SIZE)
    '''
    grid = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 1, 0, 1, 0],
            [1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
            [1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
            [1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    '''
    # print(grid)
    start = time.perf_counter()
    for i in range(1,100):
        path = solve_maze(grid, GRID_SIZE)
    print(time.perf_counter() - start)

    ''' 
    print("Success yaya!")
    # print_path(path)
    if(len(path)) > 0:
        return True
    else:
        return False
    '''


# voyage()
