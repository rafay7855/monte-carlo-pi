#   Monte Carlo simulation of Pi
#   Rafay Sheikh

#   Simulates value of pi by randomly generating points
#   on a square grid between (-1, -1) and (1, 1).
#   Inside the square is an inscribed circle. Any points
#   with a distance from center <= 1 are inside the circle.
#   pi / 4 == points inside / points total or

#   Pi = 4 * (points inside / points total)

##############################################

import random
import sys
import math
import time

##############################################

# Default number of points if user does not specify
total_points_default = 1000000

def main():
    total_points = total_points_default
    if len(sys.argv) > 1:   # If user specified number of points
        total_points = int(sys.argv[1])

    for _ in range(0, total_points):
        point = simulation_tick()
        update_stats()
        draw(point)
    print_summary(total_points)

    
# These are modified during simluation run
points_sofar = 0
points_inside = 0

def simulation_tick():
    global points_sofar, points_inside
    x, y = new_point()
    d = math.sqrt(x ** 2 + y ** 2) # Distance from center
    if (d <= 1.0):                 # If point is inside the circle (radius 1)
        points_inside += 1
    points_sofar += 1
    return (x, y, d)


def new_point():    # All points get random x, y between [-1, 1]
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    return x, y


# Get updated each simulation tick
experimental_pi = 0.0
residual = 0

def update_stats():
    global experimental_pi, residual
    experimental_pi = 4 * (points_inside / points_sofar)
    # Difference between observed and expected values
    residual = experimental_pi - math.pi


def print_summary(total_points):
    line = []
    line.append("---- After {0:d} simulated points ----".format(total_points))
    line.append("Experimental pi ====> {0:.12f}".format(experimental_pi))
    line.append("Actual pi       ====> {0:.12f}".format(math.pi))
    line.append("Residual: {0:.12f}".format(residual))
    for l in line:
        print(l, end="\n")


# Placeholder for future animation
def draw(point):
    x, y, d = point
    pass

##############################################

start_time = time.time()
main()
print("---- Completed in {0:.0f} seconds ----".format(time.time() - start_time))