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
def printEnvInfo(env, wrapped):
    if wrapped == False:
        print('======= Env Info =======')
    elif wrapped == True: 
        print('=== Wrapped Env Info ===')
    print('Name: {}'.format(env.spec.name))
    print("Observation space: {}".format(env.observation_space))
    print("Action space: {}".format(env.action_space))
    print("Reward range: {}".format(env.reward_range))
    print("========================")

# Action Wrapper --> From box(-1, 1, (2,), float32) to box(0, 1, (3,), float32)
class myActionWrapper(gym.ActionWrapper):
    def __init__(self, env):
        super().__init__(env)
        self._action_space = Box(0, 1, (3,), np.float32)
    
    def action(self):
        pass

# Observation Wrapper --> From box(array(8), array(8), (8,), float32) to box(array(8), array(8), (8,), float32)
class myObservationWrapper(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
        self._observation_space = Box(low=-np.inf, high=+np.inf, shape=(8,), dtype=np.float32)

    def observation(self):
        pass

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

    printEnvInfo(base_env, False)

    actionWrapped_env = RescaleAction(base_env, min_action=0, max_action=1)
    wrapped_env = actionWrapped_env #myObservationWrapper(actionWrapped_env)

    printEnvInfo(wrapped_env, True)

    observation, info = wrapped_env.reset(seed=42, return_info=True)
    for _ in range(1000):
        action = wrapped_env.action_space.sample()
        observation, reward, done, info = wrapped_env.step(action)
        wrapped_env.render(mode='human')

        if done:
            observation, info = wrapped_env.reset(return_info=True)

    wrapped_env.close()