
"""
Module for solving standard physics one problems for motion in one dimention.
"""

import numpy as np
import matplotlib.pyplot as plt


def distance(x0=0, v0=None, vf=None, t=None, a=None):
    if vf is None:
        xf = x0 + v0*t + 1/2 * a * t**2
        return xf
    elif t is None:
        xf = x0 + (vf**2 - v0**2) / (2*a)
        return xf
    elif a is None:
        xf = x0 + 1/2 * (v0 + vf)*t
        return xf
    elif v0 is None:
        xf = x0 + v0*t - 1/2 * a * t**2
        return xf
    else:
        print("Not enough information to solve for distance traveled")
        pass


def time(x0=0, xf=None, v0=None, vf=None, a=None):
    if xf is None:
        t = (vf - v0)/a
        return t
    elif vf is None:
        t1 = (-v0 + np.sqrt(v0**2 - 2*a*x0)) / a
        t2 = (-v0 - np.sqrt(v0**2 - 2*a*x0)) / a
        return t1, t2
    elif a is None:
        t = 2*(xf - x0) / (v0 + vf)
        return t
    elif v0 is None:
        t1 = (-vf + np.sqrt(vf ** 2 + 2 * a * x0)) / -a
        t2 = (-vf - np.sqrt(vf ** 2 + 2 * a * x0)) / -a
        return t1, t2
    else:
        print("Not enough information to solve for distance traveled")
        pass


def velocity(v0=0, x0=0, xf=None, t=None, a=None):
    if xf is None:
        vf = v0 + a*t
        return vf
    elif t is None:
        vf = np.sqrt(v0**2 + 2*a*(xf - x0))
        return vf
    elif a is None:
        vf = 2*(xf - x0)/t - v0
        return vf
    else:
        print("Not enough information to solve for the final velocity")

def acceleration(x0=0, v0=0, xf=None, vf=None, t=None):
    if xf is None:
        


def avg_velocity(dx, dt):
    if type(dx) is list and type(dt) is not list:
        v_avg = (dx[1] - dx[0]) / dt
        return v_avg
    elif type(dx) is list and type(dt) is list:
        v_avg = (dx[1] - dx[0]) / (dt[1] - dt[0])
        return v_avg
    else:
        v_avg = dx / dt
        return v_avg
