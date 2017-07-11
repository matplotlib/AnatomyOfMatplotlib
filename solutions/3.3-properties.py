t = np.arange(0.0, 5.0, 0.1)
a = np.exp(-t) * np.cos(2*np.pi*t)
plt.plot(t, a, 'r:D', mfc='y', mec='g')
plt.show()
