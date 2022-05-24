# https://www.gymlibrary.ml/content/environment_creation/
# Set-ExecutionPolicy -ExecutionPolicy Unrestricted
# Set-ExecutionPolicy -ExecutionPolicy Default

# test file for creating new OpenAIGym Environments
import gym
from gym import spaces
import numpy as np
from typing import Optional
from gym.utils.renderer import Renderer

class Falcon9Env(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 10}

    def __init__(self, render_mode: Optional[str] = None):
        assert render_mode is None or render_mode in self.metadata["render_modes"]

        # Observations are dictionaries with the agent's and the target's location.
        # Each location is encoded as an element of {0, ..., `size`}^2, i.e. MultiDiscrete([size, size]).
        self.observation_space = spaces.Dict (
            {
                # Currently set to grid of 5x5
                "agent": spaces.Box(0, 5 - 1, shape=(2,), dtype=int),
                "target": spaces.Box(0, 5 - 1, shape=(2,), dtype=int),
            }
        )

        # Actions can be either full or no thrust of each of the 3 engines (Left/Center/Right)
        # It can also be a combination of those thrusts ---> 2^3 = 8 different actions
        self.action_space = spaces.Discrete(8)