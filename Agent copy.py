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
        accuracy = 0.0001
        acc = 1
        while acc > accuracy:
            acc = 0
            for row in range(ROWS):
                for col in range(COLS):
                    state = row,col
                    if self.env.board[state] != 0:
                        continue
                    old_value = self.Value[state]
                    action = Action(self.Policy[state])
                    new_state, reward = self.env(state, action)
                    new_value = reward + self.gamma * self.Value[new_state]
                    self.Value[state] = new_value
                    acc = max(acc, abs(old_value - new_value))
        

    def Policy_improv (self):
        pass

    def Policy_Iteration (self):
        pass

    
    def Value_Iteration():
        pass

    def __call__(self, state):
        return self.get_action(state)
    

    