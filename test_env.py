# https://www.gymlibrary.ml/content/environment_creation/
# Set-ExecutionPolicy -ExecutionPolicy Unrestricted
# Set-ExecutionPolicy -ExecutionPolicy Default

# test file for creating new OpenAIGym Environments
import gym
from gym import spaces
import numpy as np
from typing import Optional
# from gym.utils.renderer import Renderer

class Falcon9Env(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 10}

    def __init__(self, render_mode: Optional[str] = None):
        assert render_mode is None or render_mode in self.metadata["render_modes"]

        self.window_size = 512 # pygame window size
  
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

        # Human rendering mode --> Display
        if render_mode == "human":
            import pygame

            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode((self.window_size, self.window_size))
            self.clock = pygame.time.clock()

    def _get_obs(self):
        return {"agent": self._agent_location, "target": self._target_location}

    def _get_info(self):
        return {"distance": np.linalg.norm(self._agent_location - self._target_location, ord=1)}

    def reset(self, seed=None, return_info=False, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        # Choose the agent's location uniformly at random
        self._agent_location = self.np_random.integers(0, self.size, size=2)

        # We will sample the target's location randomly until it does not coincide with the agent's location
        self._target_location = self._agent_location
        while np.array_equal(self._target_location, self._agent_location):
            self._target_location = self.np_random.integers(0, self.size, size=2)

        # clean the render collection and add the initial frame
        self.renderer.reset()
        self.renderer.render_step()

        observation = self._get_obs()
        info = self._get_info()
        return (observation, info) if return_info else observation
