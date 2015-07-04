import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cbook import get_sample_data
from mpl_toolkits import axes_grid1

import example_utils

def main():
    fig, axes = setup_axes()
    plot(axes, *load_data())
    example_utils.title(fig, '"ax.imshow(data, ...)": Colormapped or RGB arrays')
    fig.savefig('imshow_example.png', facecolor='none')
    plt.show()

def plot(axes, img_data, scalar_data, ny):
    # Note: I'm defining the extent so I can cheat a bit when using ImageGrid
    # to make all of the axes the same height...

    # Default: Linear interpolation
    axes[0].imshow(scalar_data, cmap='gist_earth', extent=[0, ny, ny, 0])

    # Use nearest interpolation instead.
    axes[1].imshow(scalar_data, cmap='gist_earth', interpolation='nearest',
                   extent=[0, ny, ny, 0])

    # Show RGB/RGBA data instead of colormapping a scalar.
    axes[2].imshow(img_data)

def load_data():
    img_data = plt.imread(get_sample_data('grace_hopper.png'))
    ny, nx, nbands = img_data.shape
    scalar_data = np.load(get_sample_data('axes_grid/bivariate_normal.npy'))
    return img_data, scalar_data, ny

def setup_axes():
    # We'll set up the axes a bit differently here so that they'll all be the
    # same height even though the aspect will be set and adjustable is "box".
    fig = plt.figure(figsize=(6,3))
    axes = axes_grid1.ImageGrid(fig, [0, 0, .93, 1], (1, 3), axes_pad=0)

    for ax in axes:
        ax.set(xticks=[], yticks=[])
    return fig, axes

main()
