# call solve_maze and pass field_view = 1
from Entity.Grid import Grid
from Main.search import *
import time
import matplotlib as plt


PROBABILITIES = [0.03, 0.06, 0.09, 0.12, 0.15, 0.18, 0.21, 0.24, 0.27, 0.3, 0.33, 0.36]
TEST_COUNT = 100
GRID_SIZE = 101

def run_performance_test():
    conduct_tests()
    collect_data()
    generate_graphs()

def conduct_tests():
    for probability in PROBABILITIES:
        paths = []
        for test_index in range(TEST_COUNT):
            grid = Grid.make_grid(PROBABILITIES, GRID_SIZE)
            path = solve_maze(grid, len(grid))

def generate_graphs():
