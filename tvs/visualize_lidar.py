import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

dataXY = pd.read_csv('dataXY.csv')

dataXY = dataXY[(dataXY['Y']>20)&(dataXY['Y']<200)]
dataXY['X'] = 2*dataXY['X']*math.pi/2048.0

ax = plt.subplot(111, projection='polar')
ax.plot(dataXY['X'], dataXY['Y'], '.')
ax.grid(True)
plt.show()