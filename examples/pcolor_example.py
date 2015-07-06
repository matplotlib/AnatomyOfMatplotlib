"""
Shows the basics of pcolor/pcolormesh.
One note: Use imshow if your data is on a rectangular grid, as it's much
faster. This example shows a case that imshow can't handle.
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cbook import get_sample_data

import example_utils

# Set up our data...
z = np.load(get_sample_data('axes_grid/bivariate_normal.npy'))
ny, nx = z.shape
y, x = np.mgrid[:ny, :nx]
y = (y - y.mean()) * (x + 10)**2

mask = (z > -0.1) & (z < 0.1)
z2 = np.ma.masked_where(mask, z)

fig, axes = example_utils.setup_axes()

# Either pcolor or pcolormesh would produce the same result here.
# pcolormesh is faster, however.
axes[0].pcolor(x, y, z, cmap='gist_earth')
example_utils.label(axes[0], 'either')

# The difference between the two will become clear as we turn on edges:

# pcolor will completely avoid drawing masked cells...
axes[1].pcolor(x, y, z2, cmap='gist_earth', edgecolor='black')
example_utils.label(axes[1], 'pcolor(x,y,z)')

# While pcolormesh will draw them as empty (but still present) cells.
axes[2].pcolormesh(x, y, z2, cmap='gist_earth', edgecolor='black', lw=0.5,
                   antialiased=True)
example_utils.label(axes[2], 'pcolormesh(x,y,z)')

example_utils.title(fig, 'pcolor/pcolormesh: Colormapped 2D arrays')
fig.savefig('pcolor_example.png', facecolor='none')

plt.show()
