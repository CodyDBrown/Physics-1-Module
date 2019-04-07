import numpy as np
import one_d_motion as od
import matplotlib.pyplot as plt

"""
Module for solving standard physics one problems for motion in two dimensions. 

For Now I'm assuming that all of these problems are on flat ground, so I don't have to worry about any kind of elevation 
changes. In future versions I hope to make this an option.
"""


def flight_time(v0, theta):
    theta = np.radians(theta)
    vy = v0 * np.sin(theta)
    time = od.time(xf=0, v0=vy)  # Time it takes for the object to go up then back down.
    return time


def distance(v0, theta):
    theta = np.radians(theta)
    g = 9.8
    r = v0**2 / g * np.sin(2*theta)
    return r


def height(v0, theta):
    theta = np.radians(theta)
    vy = v0*np.sin(theta)
    h = od.distance(v0=vy, vf=0)
    return h


def plot_trajectory(v0, theta):
    g = 9.8
    r = distance(v0, theta)
    theta = np.radians(theta)
    x = np.linspace(0, r, 1000)
    y = np.tan(theta)*x - ((g*x**2)/(2*v0**2*np.cos(theta)**2))

    fig = plt.figure(figsize=(10, 10))
    plt.plot(x, y)
    plt.show()


"""
Want to have some programs for target hitting. If there is a set target you want to hit, what v0 or theta do you need.
"""


def target_hit(v0=None, theta=None, r=None):
    g = 9.8
    theta = np.radians(theta)
    if v0 is None:
        v0 = np.sqrt((r*g) / np.sin(2*theta))
        return v0
    if theta is None:
        theta = 0.5 * np.arcsin((r*g) / v0**2)
        return np.rad2deg(theta)
