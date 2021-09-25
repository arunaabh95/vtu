# this file calculates density vs solvability graph
import matplotlib.pyplot as plt
from Main.search import *

SIZE = 101
TEST_COUNT = 100


def test_main():
    probabilities = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]
    solvability_list = []
    for probability in probabilities:
        solvability_list.append(run_tests(probability, TEST_COUNT) / TEST_COUNT * 100)
    plot_graph(probabilities, solvability_list)


def run_tests(probability, test_counts):
    solvability = 0
    for test_count in range(1, test_counts):
        grid = Grid.make_grid(probability, SIZE)
        path = solve_maze(grid, SIZE)
        if len(path) > 0:
            solvability += 1
    return solvability


def plot_graph(probabilities, solvability_list):
    print(solvability_list)
    plt.title("Density vs Solvabilty")
    plt.xlabel("Density")
    plt.ylabel("Solvability")
    plt.plot(probabilities, solvability_list, color="red")
    plt.show()


test_main()
