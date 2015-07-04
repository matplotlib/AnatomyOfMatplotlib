import numpy as np
import matplotlib.pyplot as plt

import example_utils

x = np.linspace(0, 10, 100)

fig, axes = example_utils.setup_axes()
for ax in axes:
    ax.margins(y=0.10)

# Default plotting, colors will be determined by the axes' color_cycle
for i in range(1, 6):
    axes[0].plot(x, i * x)

# Demonstrating different linestyles
for i, ls in enumerate(['-', '--', ':', '-.']):
    axes[1].plot(x, np.cos(x) + i, linestyle=ls)

# Using linestyles and markers
for i, (ls, mk) in enumerate(zip(['', '-', ':'], ['o', '^', 's'])):
    axes[2].plot(x, np.cos(x) + i * x, linestyle=ls, marker=mk, markevery=10)

example_utils.title(fig, '"ax.plot(x, y, ...)": Lines and/or markers', y=0.95)
fig.savefig('plot_example.png', facecolor='none')

plt.show()
