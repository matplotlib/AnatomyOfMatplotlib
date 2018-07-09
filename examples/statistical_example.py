"""
Matplotlib has a handful of specalized statistical plotting methods.

For many statistical plots, you may find that a specalized statistical plotting
package such as Seaborn (which uses matplotlib behind-the-scenes) is a better
fit to your needs.
"""
import numpy as np
import matplotlib.pyplot as plt

import example_utils

def main():
    colors = ['cyan', 'red', 'blue', 'green', 'purple']
    dists = generate_data()

    fig, axes = example_utils.setup_axes()
    hist(axes[0], dists, colors)
    boxplot(axes[1], dists, colors)
    violinplot(axes[2], dists, colors)

    example_utils.title(fig, 'hist/boxplot/violinplot: Statistical plotting',
                        y=0.9)
    fig.savefig('statistical_example.png', facecolor='none')

    plt.show()

def generate_data():
    means = [0, -1, 2.5, 4.3, -3.6]
    sigmas = [1.2, 5, 3, 1.5, 2]
    # Each distribution has a different number of samples.
    nums = [150, 1000, 100, 200, 500]

    dists = [np.random.normal(*args) for args in zip(means, sigmas, nums)]
    return dists

def hist(ax, dists, colors):
    # We could call "ax.hist(dists, ...)" and skip the loop, but we'll plot
    # each distribution separately so they'll overlap and turn on transparency
    ax.set_color_cycle(colors)
    for dist in dists:
        ax.hist(dist, bins=20, density=True, edgecolor='none', alpha=0.5)

    ax.margins(y=0.05)
    ax.set_ylim(bottom=0)

    example_utils.label(ax, 'ax.hist(dists)')

def boxplot(ax, dists, colors):
    result = ax.boxplot(dists, patch_artist=True, notch=True, vert=False)

    for box, color in zip(result['boxes'], colors):
        box.set(facecolor=color, alpha=0.5)
    for item in ['whiskers', 'caps', 'medians']:
        plt.setp(result[item], color='gray', linewidth=1.5)
    plt.setp(result['fliers'], markeredgecolor='gray', markeredgewidth=1.5)
    plt.setp(result['medians'], color='black')

    ax.margins(0.05)
    ax.set(yticks=[], ylim=[0, 6])

    example_utils.label(ax, 'ax.boxplot(dists)')

def violinplot(ax, dists, colors):
    result = ax.violinplot(dists, vert=False, showmedians=True)
    for body, color in zip(result['bodies'], colors):
        body.set(facecolor=color, alpha=0.5)
    for item in ['cbars', 'cmaxes', 'cmins', 'cmedians']:
        plt.setp(result[item], edgecolor='gray', linewidth=1.5)
    plt.setp(result['cmedians'], edgecolor='black')

    ax.margins(0.05)
    ax.set(ylim=[0, 6])

    example_utils.label(ax, 'ax.violinplot(dists)')

main()
