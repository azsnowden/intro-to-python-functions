import matplotlib.pyplot as plot
import math

def f(x):
    # my code
    return x**2

xs = list(range(-100, 100, 1))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()