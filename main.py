import numpy as np
import gym
import matplotlib.pyplot as plt
from matplotlib.patches import *

class Rocket:
    height = 41.2   # m
    diam = 3.7      # m
    dthrust = 1.5   # m

    mass_empty = 25600          # kg
    mass_propellant = 395700    # kg
    fraction_burned = 0.2       # -
    mass = mass_empty + fraction_burned * mass_propellant # kg

    thrust_max = 7607e3 # N (@ Mean Sea Level)
    burn_time = 162     # s

    h_0 = 50 # m (initial height)

    def __init__(self, name):
        self.name = name

    def plot(self):
        fig, ax = plt.subplots()

        # add plot info
        plt.title('Automated '+self.name+' landing using RL')

        # plot rocket
        ax.add_patch(Rectangle((-self.diam/2,self.h_0),self.diam,self.height))
        plt.xlim([-self.diam-5,self.diam+5])
        plt.ylim([-10,self.h_0+self.height*1.3])

        # plot thrusters
        plt.plot([-self.dthrust/2,-self.dthrust/2],[self.h_0,self.h_0-0.25*self.height],'r',linewidth=4)
        plt.plot([0,0],[self.h_0,self.h_0-0.25*self.height],'r',linewidth=8)
        plt.plot([self.dthrust/2,self.dthrust/2],[self.h_0,self.h_0-0.25*self.height],'r',linewidth=4)

        # plot ground
        plt.plot([-self.diam-5,self.diam+5],[0,0],'k',linewidth=10)
        
        plt.show()
        
f9 = Rocket('Falcon-9')
f9.plot()