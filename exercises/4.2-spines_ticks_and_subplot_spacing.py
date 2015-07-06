import matplotlib.pyplot as plt
import numpy as np

# Try to reproduce the figure shown in images/exercise_4.2.png
# This one is a bit trickier!

# Here's the data...
data = [('dogs', 4, 4), ('frogs', -3, 1), ('cats', 1, 5), ('goldfish', -2, 2)]
animals, friendliness, popularity = zip(*data)
