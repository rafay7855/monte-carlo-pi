import bokeh
import random as r

# All points get random x, y between [-1, 1]

def newPoint():
    x = r.uniform(-1, 1)
    y    = r.uniform(-1, 1)
    return x, y

interval = 0.1 # Generate a new point after every _ seconds
def main():
    px, py = newPoint()
    d = px^2 + py^2 # Distance from center
