import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import numpy as np

domain = np.linspace(0, 4, 1000)

fig, (addend1_axis, addend2_axis, sum_axis) = plt.subplots(1, 3)
for axis in (addend1_axis, addend2_axis, sum_axis):
    axis.set_xlim(domain[0], domain[-1])
    axis.set_ylim(-2, 2)

a = 1

addend1_y = np.cos(2 * np.pi * domain)
addend1_axis.plot(domain, addend1_y)
addend2_line, = addend2_axis.plot([], [])
sum_line, = sum_axis.plot([], [])


def animate(i):
    x = domain

    scalar = math.sin(.01 * i)
    addend2_y = np.cos(2 * np.pi * scalar * x)
    addend2_line.set_data(x, addend2_y)

    sum_y = addend1_y + addend2_y
    sum_line.set_data(x, sum_y)

    return addend2_line,sum_line


addend2_ani = animation.FuncAnimation(fig, func=animate, interval=10, blit=True)
plt.show()
