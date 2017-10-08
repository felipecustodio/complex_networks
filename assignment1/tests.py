import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(0, 2 * np.pi, 100)
y1 = 2 * np.sin(x1)

x2 = np.linspace(0, 3 * np.pi, 100)
y2 = 3 * np.sin(x1)

x3 = np.linspace(0, 4 * np.pi, 100)
y3 = 1 * np.sin(x1)

x4 = np.linspace(0, 5 * np.pi, 100)
y4 = 1 * np.sin(x1)

graph = plt.subplot()
graph.loglog(x1, y1, color='#D45C7E', marker='None', label='euroroad')
graph.loglog(x2, y2, color='#C9533E', marker='None', label='powergrid')
graph.loglog(x3, y3, color='#45415C', marker='None', label='airports')
graph.loglog(x4, y4, color='#DC7B28', marker='None', label='hamster')

# Hide the right and top spines
graph.spines['right'].set_visible(False)
graph.spines['top'].set_visible(False)
# Only show ticks on the left and bottom spines
graph.yaxis.set_ticks_position('left')
graph.xaxis.set_ticks_position('bottom')


plt.legend()
# Tweak spacing between subplots to prevent labels from overlapping
plt.subplots_adjust(hspace=0.5)
plt.show()