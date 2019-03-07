#!/usr/bin/python

#   Monte Carlo simulation of Pi
#   Rafay Sheikh

#   Simulates value of pi by randomly generating points
#   on a square grid between (-1, -1) and (1, 1).
#   Inside the square is an inscribed circle. Any points
#   with a distance from center <= 1 are inside the circle.
#   pi / 4 == points inside / points total or

#   Pi = 4 * (points inside / points total)

##############################################

import random as r
import math
import time
import datetime

# To be modified by user. 1,000,000 is default
points_total = 1000000

def main():
    start_time = time.time()
    f_path = "./simulation_logs/"
    f_date =  datetime.datetime.fromtimestamp(start_time).strftime('%m-%d_%H-%M-%S')
    filename = f_path + f_date + ".log"
    
    logfile = open(filename, "w+")
    print(filename)

    for _ in range(0, points_total):
        (x, y, d) = simulation_tick()
        logfile.write("x: {0:.3f} y: {0:.3f} d: {0:.5f}\n".format(x, y, d))
        update_stats()
    global delta_time
    delta_time = time.time() - start_time
    print_summary()


# These are modified during simluation run
points_sofar = 0
points_inside = 0

def simulation_tick():
    global points_sofar, points_inside
    x, y = new_point()
    d = math.sqrt(x ** 2 + y ** 2) # Distance from center

    isInCircle = False
    if (d <= 1.0): # IF distance is <= 1, point is inside the circle (radius 1)
        points_inside += 1
        isInCircle = True
    points_sofar += 1

    #print("x: {0:.3f}\ty: {1:.3f}\t d:{2:.4f}\tStatus: {3}\n".format(x, y, d, isInCircle))
    return (x, y, d)


# Get updated each simulation tick
experimental_pi = 0.0
residual = 0

def update_stats():
    global experimental_pi, residual
    experimental_pi = 4 * (points_inside / points_sofar)
    # Difference between observed and expected values
    residual = experimental_pi - math.pi


def new_point():    # All points get random x, y between [-1, 1]
    x = r.uniform(-1, 1)
    y = r.uniform(-1, 1)
    return x, y

delta_time = 0

def print_summary():
    lines = []
    lines.append("---- After {0:d} simulated points ----".format(points_total))
    lines.append("Experimental pi ====> {0:.12f}".format(experimental_pi))
    lines.append("Actual pi       ====> {0:.12f}".format(math.pi))
    lines.append("Residual: {0:.12f}".format(residual))
    lines.append("---- Completed in {0:.0f} seconds ----".format(delta_time))
    for l in lines:  
        print(l, end="\n")


main()
