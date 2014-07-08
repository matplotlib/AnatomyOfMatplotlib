fig, ax = plt.subplots(1, 1)
ax.plot([-2, 2, 3, 4], [-10, 20, 25, 5])

ax.spines['top'].set_position('center')
ax.spines['right'].set_position('center')
ax.tick_params(axis='both', direction='inout', length=10)

# Move the two remaining spines "out" away from the plot by 10 points
ax.spines['bottom'].set_position(('outward', 10))
ax.spines['left'].set_position(('outward', 10))

plt.show()
