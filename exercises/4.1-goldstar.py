from matplotlib.collections import StarPolygonCollection

fig, ax = plt.subplots(1, 1)

collection = StarPolygonCollection(5,
                                   offsets=[(0.5, 0.5)],
                                   transOffset=ax.transData)
ax.add_collection(collection)
plt.show()
