from Constants.environment_constants import *
from Entity.Agent.ExampleSensingAgent import ExampleSensingAgent
from Entity.Agent.FinalSensingAgent import FinalSensingAgent
from Entity.Agent.FullViewAgent import FullViewAgent
from Entity.Agent.NoViewAgent import NoViewAgent


def get_agent(visibility_flag, grid, goal_state, heuristics_function, heuristics_weight):
    if visibility_flag == ALLOW_FIELD_OF_VIEW:
        return FullViewAgent(grid, goal_state, heuristics_function, heuristics_weight)

    if visibility_flag == RESTRICT_FIELD_OF_VIEW:
        return NoViewAgent(grid, goal_state, heuristics_function, heuristics_weight)

    if visibility_flag == ALLOW_BASIC_SENSING:
        return ExampleSensingAgent(grid, goal_state, heuristics_function, heuristics_weight)

    if visibility_flag == ALLOW_ADVANCED_SENSING:
        return FinalSensingAgent(grid, goal_state, heuristics_function, heuristics_weight)
