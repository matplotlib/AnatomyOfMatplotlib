"""
Illustrates the basics of using "scatter".
"""
import numpy as np
import matplotlib.pyplot as plt

import example_utils

# Generate some random data...
np.random.seed(1874)
x, y, z = np.random.normal(0, 1, (3, 100))
t = np.arctan2(y, x)
size = 50 * np.cos(2 * t)**2 + 10

fig, axes = example_utils.setup_axes()

axes[0].scatter(x, y, marker='o', facecolor='white', s=80)
example_utils.label(axes[0], 'scatter(x, y)')

axes[1].scatter(x, y, s=size, marker='s', color='darkblue')
example_utils.label(axes[1], 'scatter(x, y, s)')

axes[2].scatter(x, y, c=z, s=size, cmap='gist_ncar')
example_utils.label(axes[2], 'scatter(x, y, s, c)')

example_utils.title(fig,'"ax.scatter(...)": Colored/scaled markers',
                    y=0.95)
fig.savefig('scatter_example.png', facecolor='none')

plt.show()
