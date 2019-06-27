import matplotlib.pyplot as plot
import math

def f(x):
    # my code
    return math.sin(x)

x_axis = list(range(-5, 5, 1))
y_axis = []

for x in x_axis:
    y_axis.append(f(x))

plot.plot(x_axis, y_axis)
plot.show()