from Constants.environment_constants import *
import math


# class to return heuristics
class Heuristics:

    @staticmethod
    def get_heuristic_function(heuristic_flag, heuristic_weight):
        if heuristic_weight > 1:
            return Heuristics.get_weighed_manhattan
        if heuristic_flag == MANHATTAN_HEURISTICS:
            return Heuristics.get_manhattan
        if heuristic_flag == EUCLIDEAN_HEURISTICS:
            return Heuristics.get_euclidean
        if heuristic_flag == CHEBYSHEV_HEURISTICS:
            return Heuristics.get_chebyshev
        if heuristic_flag == COMBINED_HEURISTICS:
            return Heuristics.get_combined_heuristics

        return Heuristics.get_manhattan

    @staticmethod
    def get_manhattan(x, y, goal, heuristic_weight=1):
        return abs(x - goal.x) + abs(y - goal.y)

    @staticmethod
    def get_euclidean(x, y, state2, heuristic_weight=1):
        return math.sqrt(pow(abs(state2.x - x), 2) + pow(abs(state2.y - y), 2))

    @staticmethod
    def get_chebyshev(x, y, state2, heuristic_weight=1):
        return max(abs(state2.x - x), abs(y - state2.y))

    @staticmethod
    def get_weighed_manhattan(x, y, state2, weight):
        return weight * abs(x - state2.x) + weight * abs(y - state2.y)

    @staticmethod
    def get_combined_heuristics(x, y, state2, weight=1):
        return (abs(x - state2.x) + abs(y - state2.y) +
                math.sqrt(pow(abs(state2.x - x), 2) + pow(abs(state2.y - y), 2)) +
                max(abs(state2.x - x), abs(y - state2.y))) / 3
