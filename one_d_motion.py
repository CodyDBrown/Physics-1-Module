import numpy as np

"""
Module for solving standard physics one problems for motion in one dimention.
"""

"""
2019-04-07: I should rework these functions so that each if statement checks what I do have, not what I'm missing. It 
            probably doesn't matter but it would be a little bit nicer and easier for humans to read and understand. 
"""


def distance(x0=0, a=-9.8, v0=None, vf=None, t=None,):
    if vf is None:
        try:
            xf = x0 + v0*t + 1/2 * a * t**2
            return xf
        except TypeError:
            print("Not enough information to solve for distance traveled")
    elif t is None:
        try:
            xf = x0 + (vf**2 - v0**2) / (2*a)
            return xf
        except TypeError:
            print("Not enough information to solve for distance traveled")
    elif a is None:
        try:
            xf = x0 + 1/2 * (v0 + vf)*t
            return xf
        except TypeError:
            print("Not enough information to solve for distance traveled")
    elif v0 is None:
        try:
            xf = x0 + v0*t - 1/2 * a * t**2
            return xf
        except TypeError:
            print("Not enough information to solve for distance traveled")


def time(x0=0, a=-9.8, xf=None, v0=None, vf=None):
    if xf is None:
        try:
            t = (vf - v0)/a
            return t
        except TypeError:
            print("Not enough information to solve for time")
    elif vf is None:
        try:
            t1 = (-v0 + np.sqrt(v0**2 - 2*a*x0)) / a
            t2 = (-v0 - np.sqrt(v0**2 - 2*a*x0)) / a
            return t1, t2
        except TypeError:
            print("Not enough information to solve for time")
    elif a is None:
        try:
            t = 2*(xf - x0) / (v0 + vf)
            return t
        except TypeError:
            print("Not enough information to solve for time")
    elif v0 is None:
        try:
            t1 = (-vf + np.sqrt(vf ** 2 + 2 * a * x0)) / -a
            t2 = (-vf - np.sqrt(vf ** 2 + 2 * a * x0)) / -a
            return t1, t2
        except TypeError:
            print("Not enough information to solve for time")


def velocity(v0=0, x0=0, a=-9.8, xf=None, t=None):
    if xf is None:
        try:
            vf = v0 + a*t
            return vf
        except TypeError:
            print("Not enough information to solve for velocity")
    elif t is None:
        try:
            vf = np.sqrt(v0**2 + 2*a*(xf - x0))
            return vf
        except TypeError:
            print("Not enough information to solve for velocity")
    elif a is None:
        try:
            vf = 2*(xf - x0)/t - v0
            return vf
        except TypeError:
            print("Not enough information to solve for velocity")


def acceleration(x0=0, v0=0, xf=None, vf=None, t=None):
    if xf is None:
        try:
            a = (vf - v0)/t
            return a
        except TypeError:
            print("Not enough information to solve for acceleration.")
    elif vf is None:
        try:
            a = 2*(xf - x0 - v0*t) / t**2
            return a
        except TypeError:
            print("Not enough information to solve for the acceleration")
    elif t is None:
        try:
            a = (vf**2 - v0**2) / (2 * (xf - x0))
            return a
        except TypeError:
            print("Not enough information to solve for the acceleration")


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
