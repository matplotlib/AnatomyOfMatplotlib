#import required libraries 
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1) # generates exact same random values as they are here inside .seed(value)

# Generate Random  data...
y_raw = np.random.randn(1000).cumsum() + 15
x_raw = np.linspace(0, 24, y_raw.size)

# Get averages of every 100 samples...
x_pos = x_raw.reshape(-1, 100).min(axis=1)
y_avg = y_raw.reshape(-1, 100).mean(axis=1)
y_err = y_raw.reshape(-1, 100).ptp(axis=1)

bar_width = x_pos[1] - x_pos[0]

# Make a made up future prediction with a fake confidence
x_pred = np.linspace(0, 30)
y_max_pred = y_avg[0] + y_err[0] + 2.3 * x_pred
y_min_pred = y_avg[0] - y_err[0] + 1.2 * x_pred

# Just so you don't have to guess at the colors...
barcolor, linecolor, fillcolor = 'wheat', 'salmon', 'lightblue'

# Now you're on your own!

#making sublots
fig, ax = plt.subplots()

#Styling the Plot a little ...
ax.plot(x_raw, y_raw, color=linecolor)
ax.bar(x_pos, y_avg, width=bar_width, color=barcolor, yerr=y_err, 
       ecolor='gray', edgecolor='gray')
ax.fill_between(x_pred, y_min_pred, y_max_pred, color=fillcolor)

ax.set(title='Future Projection of Attitudes', 
       ylabel='Snarkiness (snark units)', 
       xlabel='Minutes since class began')

plt.show()
