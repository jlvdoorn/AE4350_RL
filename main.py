import numpy as np
import gym

class Rocket:
    name = "Falcon 9 - Stage 1"
    height = 41.2   # m
    diam = 3.7      # m
    dtrhust = 1.5   # m

    mass_empty = 25600          # kg
    mass_propellant = 395700    # kg
    fraction_burned = 0.2       # -
    mass = mass_empty + fraction_burned * mass_propellant # kg

    thrust_max = 7607e3 # N (@ Mean Sea Level)
    burn_time = 162     # s

f9 = Rocket
print(f9.name)