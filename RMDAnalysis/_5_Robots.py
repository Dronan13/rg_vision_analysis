import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import style, markers
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import ShowFunc as sf

def autolabel(rects, type):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                type % height,
                ha='center', va='bottom')

pre_map = np.rot90(np.loadtxt('E:/experiments/mode_Group#5/common/maps/M1.txt'))

r1_map = np.rot90(np.loadtxt('E:/experiments/mode_Group#5/R1/maps/M1.txt'))
r1_map = np.logical_not(r1_map).astype(int)
r2_map = np.rot90(np.loadtxt('E:/experiments/mode_Group#5/R2/maps/M1.txt'))
r2_map = np.logical_not(r2_map).astype(int)
r3_map = np.rot90(np.loadtxt('E:/experiments/mode_Group#5/R3/maps/M1.txt'))
r3_map = np.logical_not(r3_map).astype(int)
r4_map = np.rot90(np.loadtxt('E:/experiments/mode_Group#5/R4/maps/M1.txt'))
r4_map = np.logical_not(r4_map).astype(int)
r5_map = np.rot90(np.loadtxt('E:/experiments/mode_Group#5/R5/maps/M1.txt'))
r5_map = np.logical_not(r5_map).astype(int)
sum_map = np.add(r5_map, np.add(np.add(r1_map, r2_map), np.add(r3_map, r4_map)))

df_1 = pd.read_json('E:/experiments/mode_Group#5/R1/frames/FE1.json')
df_2 = pd.read_json('E:/experiments/mode_Group#5/R2/frames/FE1.json')
df_3 = pd.read_json('E:/experiments/mode_Group#5/R3/frames/FE1.json')
df_4 = pd.read_json('E:/experiments/mode_Group#5/R4/frames/FE1.json')
df_5 = pd.read_json('E:/experiments/mode_Group#5/R5/frames/FE1.json')

sf.show_movement(df_1,'r')
sf.show_movement(df_2,'g')
sf.show_movement(df_3,'b')
sf.show_movement(df_4,'c')
sf.show_movement(df_5,'y')

sf.show_map(df_1,'r') 
sf.show_map(df_2,'g') 
sf.show_map(df_3,'b') 
sf.show_map(df_4,'c') 
sf.show_map(df_5,'y') 

sf.show_frame()
plt.show()

unique, counts = np.unique(sum_map, return_counts=True)
D = dict(zip(unique, counts))

plt.bar(range(len(D)), list(D.values()), align='center')
plt.xticks(range(len(D)), list(D.keys()))

print(D)
plt.show()

cmap = mpl.colors.ListedColormap(['white', 'green', 'blue', 'cyan', 'yellow', 'red' ])
cmap.set_over('0.25')
cmap.set_under('0.75')
bounds = [0, 1, 2, 3, 4, 5]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

plt.subplot(231)
plt.imshow(r1_map, cmap=cmap, norm=norm)
plt.subplot(232)
plt.imshow(r2_map, cmap=cmap, norm=norm)
plt.subplot(233)
plt.imshow(r3_map, cmap=cmap, norm=norm)
plt.subplot(234)
plt.imshow(r4_map, cmap=cmap, norm=norm)
plt.subplot(235)
plt.imshow(r5_map, cmap=cmap, norm=norm)
plt.subplot(236)
plt.imshow(sum_map, cmap=cmap, norm=norm)
plt.show()

#Effectiveness R5
r51_map_unique = ((r1_map - r2_map - r3_map - r4_map - r5_map) == 1).astype(int)
r52_map_unique = ((r2_map - r1_map - r3_map - r4_map - r5_map) == 1).astype(int)
r53_map_unique = ((r3_map - r2_map - r1_map - r4_map - r5_map) == 1).astype(int)
r54_map_unique = ((r4_map - r2_map - r3_map - r1_map - r5_map) == 1).astype(int)
r55_map_unique = ((r5_map - r2_map - r3_map - r4_map - r1_map) == 1).astype(int)

sum_map_unique = np.add(r55_map_unique, np.add(np.add(r51_map_unique, r52_map_unique), np.add(r53_map_unique, r54_map_unique)))
sum_map_unique = (sum_map_unique == 1).astype(int)

total_unique = [np.sum(r51_map_unique), np.sum(r52_map_unique), np.sum(r53_map_unique), np.sum(r54_map_unique), np.sum(r55_map_unique)]
print(total_unique)

N = 5
# the x locations for the groups
ind = np.arange(N)*5
width = 1

sumt = np.sum(sum_map_unique)
effectivenes = [total_unique[0]*100/sumt,
                total_unique[1]*100/sumt,
                total_unique[2]*100/sumt,
                total_unique[3]*100/sumt,
                total_unique[4]*100/sumt,]

fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, effectivenes, width, color='blue')
ax.set_title('Individual effectiveness')
ax.set_xticks(ind)
ax.set_xticklabels(('Robot#1', 'Robot#2', 'Robot#3', 'Robot#4', 'Robot#5'))
autolabel(rects1,'%0.2f')
plt.grid(True)
plt.ylim(top=100)
plt.ylabel('Effectiveness (%)')
plt.show()




