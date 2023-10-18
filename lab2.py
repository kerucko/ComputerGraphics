from matplotlib import pyplot as plt
import numpy as np



fig = plt.figure()
ax = fig.add_subplot(projection="3d")

x1, y1, z1 = [0, 2, 1, 0], [0, 0, np.sqrt(3), 0], [-1, -1, -1, -1]
x2, y2, z2 = [0, 2, 1, 0], [0, 0, np.sqrt(3), 0], [1, 1, 1, 1]
x3, y3, z3 = [0, 0], [0, 0], [1, -1]
x4, y4, z4 = [2, 2], [0, 0], [1, -1]
x5, y5, z5 = [1, 1], [np.sqrt(3), np.sqrt(3)], [-1, 1]

ax.scatter(x1, y1, z1, c='blue', s=100)
ax.scatter(x2, y2, z2, c='blue', s=100)
ax.scatter(x3, y3, z3, c='blue', s=100)
ax.scatter(x4, y4, z4, c='blue', s=100)
ax.scatter(x5, y5, z5, c='blue', s=100)

ax.plot(x1, y1, z1, color='blue')
ax.plot(x2, y2, z2, color='blue')
ax.plot(x3, y3, z3, color='blue')
ax.plot(x4, y4, z4, color='blue')
ax.plot(x5, y5, z5, color='blue')

plt.show()
