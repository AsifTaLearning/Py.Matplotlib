import matplotlib.pyplot as plt
import numpy as np

# Matplotlib Line
# Linestyle

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

# Another example

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dashed')

plt.show()

# Shorter Syntax

"""

linestyle can be written as ls.

dotted can be written as :.

dashed can be written as --.

"""

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls = ':')

plt.show()

# Line Styles
# 'solid' (default)

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls = '-')
plt.show()

# 'dotted'

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls = ':')
plt.show()

# 'dashed'

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls = '--')
plt.show()

# 'dashdot'

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls = '-.')
plt.show()

# 'None'

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls = " ")
plt.show()

# Line Color

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()

# Another example

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, c = '#4CAF50')
plt.show()

# Another example

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, c = 'hotpink')
plt.show()

# Line Width

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()

# Multiple Lines

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

# Another example

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()






