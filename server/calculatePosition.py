import numpy as np
from scipy.optimize import fsolve
from math import sin, cos, sqrt, atan2, radians

spSound = 0.343 #meters/milisecond

def calcDist(lat1, lon1, lat2, lon2):
    R = 6373000.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

def equations(vars):
    x, y, t = vars
    eq1 = calcDist(h1, k1, x, y) - ((abs(t) + a)*spSound)
    eq2 = calcDist(h2, k2, x, y) - ((abs(t) + b)*spSound)
    eq3 = calcDist(h3, k3, x, y) - ((abs(t) + c)*spSound)
    return [eq1, eq2, eq3]

def calculatePosition(lat1, lon1, time1, lat2, lon2, time2, lat3, lon3, time3):
    global h1, k1, h2, k2, h3, k3, a, b, c
    h1 = lat1
    k1 = lon1
    h2 = lat2
    k2 = lon2
    h3 = lat3
    k3 = lon3
    a = time1 - min(time1,time2,time3)
    b = time2 - min(time1,time2,time3)
    c = time3 - min(time1,time2,time3)
    initial_guess = [(h1+h2+h3)/3, (k1+k2+k3)/3, 1]
    # Solve the system of equations
    solution = fsolve(equations, initial_guess)
    x, y, t = solution
    return [round(x,10), round(y,10), round(abs(t),10)]