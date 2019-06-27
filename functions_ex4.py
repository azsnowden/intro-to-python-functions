import matplotlib.pyplot as plot
import math

def f(x):
    # my code
    if x%2 == 1:
        return 1
    else:
        return -1  

xs = list(range(-5, 5, 1))
ys = []

for x in xs:
    ys.append(f(x))

plot.bar(xs, ys)
plot.show()