# import bokeh
import random as r

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from math import pi
from PyQt5.QtWidgets import * # QApplication, QWidget, QMainWindow, QPushButton

##############################################


def new_point():    # All points get random x, y between [-1, 1]
    x = r.uniform(-1, 1)
    y = r.uniform(-1, 1)
    return x, y

points_inside = 0
points_total = 0

experimental_pi = 0.0
r_squared = 0.0
def simulation():
    global points_inside, points_total

    px, py = new_point()
    d = px ** 2 + py ** 2 # Distance from center
    if (d <= 1.0):                      # IF distance is <= 1, point is inside the circle (radius 1)
        points_inside += 1
    points_total += 1
    draw(px, py, d)
    update_stats(px, py)

     
def draw(x, y, d):
    pass

def update_stats(px, py):
    experimental_pi = 4 * (points_inside / points_total)
    r_squared = 0
    
class window(QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.init_menu()
        self.init_simulation()
        simulation()

    def init_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Options')

    def init_simulation(self):
        simview = QHBoxLayout()
        simview.addStretch(1)
        # self.setLayout(simview)

        self.setGeometry(50,50,700,300)
        self.setWindowTitle('Monte Carlo')
        self.show()
def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()
