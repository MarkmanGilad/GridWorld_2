import random
from typing import Any
import numpy as np
from Graphics import *
from Action import Action
from Environement import Environement as Env


class Random_Agent:
    def __init__(self, env) -> None:
        self.env : Env = env
        self.Reward = 0
    
    def get_action(self, state):
        actions = self.env.get_actions(state)
        return random.choice(actions)
            
    def add_reward(self, reward):
        self.Reward += reward

    def __call__(self, state):
        return self.get_action(state)
    
class AI_Agent:
    def __init__(self, env) -> None:
        self.env : Env = env
        self.Reward = 0
        self.Policy = np.full((ROWS, COLS), 3)  # Random policy always down
        self.Value = np.zeros((ROWS, COLS))     # Random Value all zero
        self.gamma = 0.9

    def get_action(self, state):
        return Action(self.Policy[state])
            
    def add_reward(self, reward):
        self.Reward += reward

    def policy_eval (self):
        pass

    def Policy_improv (self):
        pass

    def Policy_Iteration (self):
        pass

    
    def Value_Iteration():
        pass

    def __call__(self, state):
        return self.get_action(state)
    

    