import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)


# Generate random data with different ranges...
data1 = np.random.random((10, 10))
data2 = 2 * np.random.random((10, 10))
data3 = 3 * np.random.random((10, 10))

# Set up our figure and axes...
fig, axes = plt.subplots(ncols=3, figsize=plt.figaspect(0.5))
fig.tight_layout() # Make the subplots fill up the figure a bit more...
cax = fig.add_axes([0.25, 0.1, 0.55, 0.03]) # Add an axes for the colorbar

# Now you're on your own!
for ax, data in zip(axes, [data1, data2, data3]):
    # Display data, explicitly making the colormap cover values from 0 to 3
    im = ax.imshow(data, vmin=0, vmax=3, interpolation='nearest')

fig.colorbar(im, cax=cax, orientation='horizontal')
plt.show()
