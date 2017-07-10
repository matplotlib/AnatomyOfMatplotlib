import numpy as np
import matplotlib.pyplot as plt

plt.style.use('classic')

t = np.linspace(0, 2 * np.pi, 150)
x1, y1 = np.cos(t), np.sin(t)
x2, y2 = 2 * x1, 2 * y1

colors = ['darkred', 'darkgreen']

fig, ax = plt.subplots()
ax.plot(x1, y1, color=colors[0], label='Inner', linewidth=3)
ax.plot(x2, y2, color=colors[1], label='Outer', linewidth=3)
ax.legend()

ax.axis('equal')
ax.margins(0.05)

plt.show()
