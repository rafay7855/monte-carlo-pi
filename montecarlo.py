#   Monte Carlo simulation of Pi
#   Rafay Sheikh

#   Simulates value of pi by randomly generating points
#   on a square grid between (-1, -1) and (1, 1).
#   Inside the square is an inscribed circle. Any points
#   with a distance from center <= 1 are inside the circle.
#   pi / 4 == points inside / points total or 

#   Pi = 4 * (points inside / points total)

##############################################

# import bokeh
import random as r

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math
from PyQt5.QtWidgets import * # QApplication, QWidget, QMainWindow, QPushButton

##############################################

# To be modified by user. 1,000,000 is default
points_total = 1000000

def main():
    for x in range(0, points_total):
        simulation_tick()
        update_stats()
        # draw()
    print_summary()

    
# These are modified during simluation run
points_sofar = 0
points_inside = 0

def simulation_tick():
    px, py = new_point()
    d = math.sqrt(px ** 2 + py ** 2) # Distance from center
    if (d <= 1.0):                   # IF distance is <= 1, point is inside the circle (radius 1)
        points_inside += 1
    points_sofar += 1

# Get updated each simulation tick
experimental_pi = 0.0
r_squared = 0.0

def update_stats():
    experimental_pi = 4 * (points_inside / points_sofar)
    r_squared = 0


def new_point():    # All points get random x, y between [-1, 1]
    x = r.uniform(-1, 1)
    y = r.uniform(-1, 1)
    return x, y


def print_summary():
    print()

def draw(x, y, d):
    pass



##############################################

#   Planned: Animate the simulation and make a running graph
#   of the error between experimental and actual pi
    
# class window(QMainWindow):
#     def __init__(self):
#         super(window, self).__init__()
#         self.init_menu()
#         self.init_simulation()
#         simulation()

#     def init_menu(self):
#         mainMenu = self.menuBar()
#         fileMenu = mainMenu.addMenu('Options')

#     def init_simulation(self):
#         simview = QHBoxLayout()
#         simview.addStretch(1)
#         # self.setLayout(simview)

#         self.setGeometry(50,50,700,300)
#         self.setWindowTitle('Monte Carlo')
#         self.show()

# def run():
#     app = QApplication(sys.argv)
#     Gui = window()
#     sys.exit(app.exec_())

# run()
