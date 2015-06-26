t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
plt.plot(t, s, lw=2)

plt.annotate('local min', xy=(2.5, -1), xytext=(3.5, -1.5),
             arrowprops=dict(arrowstyle='fancy', color='red', shrink=0.5))

plt.ylim(-2, 2)
plt.show()
