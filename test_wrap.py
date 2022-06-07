import gym
from gym.wrappers import RescaleAction, TransformObservation
from gym.spaces import *

import numpy as np

# The goal of the wrapper is to create a new action space of type Box(low=0.0, high=1.0, shape=(3,), dtype=np.float32) 
# and to create a new observation space of type Box(low=-5.0, high=5.0, shape=(3,), dtype=np.float32)
#
# That can be done by transforming the action and observation spaces of the current environment
# so we need two wrappers --> ActionWrapper and ObservationWrapper
#
# Current Observation Space: Box([-1.5 -1.5 -5 -5 -3.1415927 -5 -0 -0])
# Current   Action    Space: Box([ 0.5  5.0 (2,) float32])

# Print env info
def printEnvInfo(env):
    print('======= Env Info =======')
    print('Name: {}'.format(env.unwrapped))
    print("Observation space: {}".format(env.observation_space))
    print("Action space: {}".format(env.action_space))
    print("Reward range: {}".format(env.reward_range))
    print("========================")

# Action Wrapper
class myActionWrapper(gym.ActionWrapper):
    def __init__(self, env, disc_to_cont):
        super().__init__(env)
        self.disc_to_cont = disc_to_cont
        self._action_space = Discrete(len(disc_to_cont))
    
    def action(self, act):
        return self.disc_to_cont[act]

# Observation Wrapper
class myObservationWrapper(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
        self._observation_space = Box(low=-np.inf, high=+np.inf, shape=(2,), dtype=np.float32)

    def observation(self, obs):
        return obs["target"] - obs["agent"]

# Main function of program
if __name__ == "__main__":
    base_env = gym.make(
        "LunarLander-v2",
        continuous = True,
        gravity = -9.81,
        enable_wind = False,
        wind_power = 7.5,
        turbulence_power = 0.5,
    )
    base_env.reset()

    printEnvInfo(base_env)

    actionWrapped_env = myActionWrapper(base_env, [np.array([1,0])],[np.array([-1,0])],[np.array([0,1])],[np.array([0,-1])])
    wrapped_env = myObservationWrapper(actionWrapped_env)

    printEnvInfo(wrapped_env)