# Reinforcement Learning Assignment for AE4350
This is a reinforcement learning model for the control of a simplified [falcon 9](https://www.spaceflightinsider.com/hangar/falcon-9) rocket of SpaceX.

## Info
```main.py``` is the main file

```test_.py``` is a test file for creating an new gym environment

````test_ll.py``` is a test file for creating an instance of the LunarLander environment

```test_wrap.py``` is a test file for creating a wrapper around the LunarLander environment

## Virtual Environment
Create venv: ```conda create -n myvenv```

Activate: ```conda activate myvenv```

Deactivate: ```deactive```


## Status
Work in Progress

## Ideas
### Action space
#### 1. MultiBinary

2D - There are three thrusters (left, center, right) that can have either no or full thrust.

```action_space = MultiBinary(3)```


3D - There are nine thrusters (center, 8 tusters around center) that can have either no or full thrust.

```action_space = MultiBinary(9)```

#### 2. Box

2D - There are three thrusters (left, center, right) that can have a range of thrust from 0.0 (0%) to 1.0 (100%).

```action_space = Box(low=0.0, high=1.0, shape=(3,), dtype=np.float32)```


3D - There are nine thrusters (center, 8 thrusters around center) that can have a range of thrust from 0.0 (0%) to 1.0 (100%).

```action_space = Box(low=0.0, high=1.0, shape=(9,), dtype=np.float32)```

### Observation space
#### 1. 2-Dimensional

A 2D 'box' with origin 0.0, ranging from -5.0 to +5.0 on x and y axes.

```observation_space = Box(low=-5.0, high=5.0, shape=(2,), dtype=np.float32)```

#### 2. 3-Dimensional

A 3D 'box' with origin 0.0, ranging from -5.0 to +5.0 on x, y and z axes.

```observation_space = Box(low=-5.0, high=5.0, shape=(3,), dtype=np.float32)```
