import matplotlib.pyplot as plt
import numpy as np

data = [('dogs', 4, 4), ('frogs', -3, 1), ('cats', 1, 5), ('goldfish', -2, 2)]
animals, friendliness, popularity = zip(*data)


def plot_and_setup_spines(ax, animals, y, ylabel):
    x = np.arange(len(animals))
    ax.bar(x, y, align='center', color='gray')
    ax.set(xticks=x, xticklabels=animals, ylabel=ylabel)

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.tick_params(axis='x', direction='inout', length=8)
    ax.margins(0.05)

fig, axes = plt.subplots(nrows=2)
fig.subplots_adjust(hspace=0.0)

plot_and_setup_spines(axes[0], animals, friendliness, 'Friendliness')
plot_and_setup_spines(axes[1], animals, popularity, 'Popularity')

plt.show()
