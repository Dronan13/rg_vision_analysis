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
        
#1 ROBOTS
df1_1 = pd.read_json('E:/experiments/obstacles#2/mode_Group#1/R1/frames/FE1.json')
r11_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#1/R1/maps/M1.txt'))
r11_map = np.logical_not(r11_map).astype(int)
sum_map1 = r11_map

#2 ROBOTS
df2_1 = pd.read_json('E:/experiments/obstacles#2/mode_Group#2/R1/frames/FE1.json')
df2_2 = pd.read_json('E:/experiments/obstacles#2/mode_Group#2/R2/frames/FE1.json')
r21_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#2/R1/maps/M1.txt'))
r21_map = np.logical_not(r21_map).astype(int)
r22_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#2/R2/maps/M1.txt'))
r22_map = np.logical_not(r22_map).astype(int)
sum_map2 = np.add(r21_map, r22_map)

#3 ROBOTS
df3_1 = pd.read_json('E:/experiments/obstacles#2/mode_Group#3/R1/frames/FE1.json')
df3_2 = pd.read_json('E:/experiments/obstacles#2/mode_Group#3/R2/frames/FE1.json')
df3_3 = pd.read_json('E:/experiments/obstacles#2/mode_Group#3/R3/frames/FE1.json')
r31_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#3/R1/maps/M1.txt'))
r31_map = np.logical_not(r31_map).astype(int)
r32_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#3/R2/maps/M1.txt'))
r32_map = np.logical_not(r32_map).astype(int)
r33_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#3/R3/maps/M1.txt'))
r33_map = np.logical_not(r33_map).astype(int)
sum_map3 = np.add(np.add(r31_map, r32_map), r33_map)

#4 ROBOTS
df4_1 = pd.read_json('E:/experiments/obstacles#2/mode_Group#4/R1/frames/FE1.json')
df4_2 = pd.read_json('E:/experiments/obstacles#2/mode_Group#4/R2/frames/FE1.json')
df4_3 = pd.read_json('E:/experiments/obstacles#2/mode_Group#4/R3/frames/FE1.json')
df4_4 = pd.read_json('E:/experiments/obstacles#2/mode_Group#4/R4/frames/FE1.json')
r41_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#4/R1/maps/M1.txt'))
r41_map = np.logical_not(r41_map).astype(int)
r42_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#4/R2/maps/M1.txt'))
r42_map = np.logical_not(r42_map).astype(int)
r43_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#4/R3/maps/M1.txt'))
r43_map = np.logical_not(r43_map).astype(int)
r44_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#4/R4/maps/M1.txt'))
r44_map = np.logical_not(r44_map).astype(int)
sum_map4 = np.add(np.add(r41_map, r42_map), np.add(r43_map, r44_map))

#5 ROBOTS
df5_1 = pd.read_json('E:/experiments/obstacles#2/mode_Group#5/R1/frames/FE1.json')
df5_2 = pd.read_json('E:/experiments/obstacles#2/mode_Group#5/R2/frames/FE1.json')
df5_3 = pd.read_json('E:/experiments/obstacles#2/mode_Group#5/R3/frames/FE1.json')
df5_4 = pd.read_json('E:/experiments/obstacles#2/mode_Group#5/R4/frames/FE1.json')
df5_5 = pd.read_json('E:/experiments/obstacles#2/mode_Group#5/R5/frames/FE1.json')
r51_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#5/R1/maps/M1.txt'))
r51_map = np.logical_not(r51_map).astype(int)
r52_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#5/R2/maps/M1.txt'))
r52_map = np.logical_not(r52_map).astype(int)
r53_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#5/R3/maps/M1.txt'))
r53_map = np.logical_not(r53_map).astype(int)
r54_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#5/R4/maps/M1.txt'))
r54_map = np.logical_not(r54_map).astype(int)
r55_map = np.rot90(np.loadtxt('E:/experiments/obstacles#2/mode_Group#5/R5/maps/M1.txt'))
r55_map = np.logical_not(r55_map).astype(int)
sum_map5 = np.add(r55_map, np.add(np.add(r51_map, r52_map), np.add(r53_map, r54_map)))


#Iterations comparison
iterations = [df1_1['points'].size, 
              df2_1['points'].size, 
              df3_1['points'].size, 
              df4_1['points'].size, 
              df5_1['points'].size]
robots_exp = [1,2,3,4,5]

fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xticks([1,2,3,4,5])
ax.set_xticklabels(('Single Robot', '2 Robots', '3 Robots', '4 Robots', '5 Robots'))

plt.plot(robots_exp, iterations,'b', robots_exp, iterations,'ro')
for xy in zip(robots_exp, iterations):                                       
    ax.annotate('%s' % xy[1], xy=xy, textcoords='data') 
    
plt.grid(True)
plt.ylabel('Iterations')
plt.xlabel('Robots')

#Data
_, counts1 = np.unique(sum_map1, return_counts=True)
_, counts2 = np.unique(sum_map2, return_counts=True)
_, counts3 = np.unique(sum_map3, return_counts=True)
_, counts4 = np.unique(sum_map4, return_counts=True)
_, counts5 = np.unique(sum_map5, return_counts=True)
unique = [0,1,2,3,4,5]
#counts1 = np.append(counts1, [0,0,0,0])
D1 = dict(zip(unique, np.append(counts1, [0,0,0,0])))
D2 = dict(zip(unique, np.append(counts2, [0,0,0])))
D3 = dict(zip(unique, np.append(counts3, [0,0])))
D4 = dict(zip(unique, np.append(counts4, [0])))
D5 = dict(zip(unique, counts5))

del D1[0]
del D2[0]
del D3[0]
del D4[0]
del D5[0]

#
fig = plt.figure()
ax = fig.add_subplot(111)
N = 5
ind = np.arange(N)*5  # the x locations for the groups

width = 1       # the width of the bars
rects1 = ax.bar(ind-2*width, D1.values(), width, color='black')
rects2 = ax.bar(ind-width, D2.values(), width, color='red')
rects3 = ax.bar(ind, D3.values(), width, color='green')
rects4 = ax.bar(ind+width, D4.values(), width, color='blue')
rects5 = ax.bar(ind+2*width, D5.values(), width, color='yellow')

ax.set_title('Detected by individual robots in group')
ax.set_xticks(ind)
ax.set_xticklabels(('By 1 robot', 'By 2 robot2', 'By 3 robot2', 'By 4 robot2', 'By 5 robot2'))
ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), 
          ('Single Robot', '2 Robots', '3 Robots', '4 Robots', '5 Robots') )
plt.grid(True)
plt.ylabel('Sectors')
plt.xlabel('By N Robots')
autolabel(rects1,'%d')
autolabel(rects2,'%d')
autolabel(rects3,'%d')
autolabel(rects4,'%d')
autolabel(rects5,'%d')

total = [sum(D1.values()), sum(D2.values()), sum(D3.values()), sum(D4.values()), sum(D5.values())]
max_tiles = max(total)
total_comp = [sum(D1.values())*100/max_tiles, 
              sum(D2.values())*100/max_tiles, 
              sum(D3.values())*100/max_tiles, 
              sum(D4.values())*100/max_tiles, 
              sum(D5.values())*100/max_tiles];


#
fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, total_comp, width, color='blue')
ax.set_title('Detected areas compared to maximum value')
ax.set_xticks(ind)
ax.set_xticklabels(('Single Robot', '2 Robots', '3 Robots', '4 Robots', '5 Robots'))
autolabel(rects1,'%0.2f')
plt.grid(True)
plt.ylim(top=110)
plt.ylabel('%')
plt.xlabel('By N Robots')

#Knowledge
fig = plt.figure()
ax = fig.add_subplot(111)
sums_grid1 = np.loadtxt('E:/experiments/obstacles#2/mode_Group#1/common/maps/sums.txt').astype(int)#3766 #3763
sums_grid2 = np.loadtxt('E:/experiments/obstacles#2/mode_Group#2/common/maps/sums.txt').astype(int)[::2]#1696 #3370
sums_grid3 = np.loadtxt('E:/experiments/obstacles#2/mode_Group#3/common/maps/sums.txt').astype(int)[::3]#1270 #3789
sums_grid4 = np.loadtxt('E:/experiments/obstacles#2/mode_Group#4/common/maps/sums.txt').astype(int)[::4]#766 #3040
sums_grid5 = np.loadtxt('E:/experiments/obstacles#2/mode_Group#5/common/maps/sums.txt').astype(int)[::5]#714 #3535
N=[len(sums_grid1),len(sums_grid2),len(sums_grid3),len(sums_grid4),len(sums_grid5)]
ind=[np.arange(N[0]), np.arange(N[1]), np.arange(N[2]), np.arange(N[3]), np.arange(N[4])]
maxs = [max(sums_grid1), max(sums_grid2), max(sums_grid3), max(sums_grid4), max(sums_grid5)]
plt.plot(ind[0],sums_grid1/maxs[0]*100, 'r', label="Single robot")
plt.plot(ind[1],sums_grid2/maxs[1]*100, 'g', label="2 robots")
plt.plot(ind[2],sums_grid3/maxs[2]*100, 'b', label="3 robots")
plt.plot(ind[3],sums_grid4/maxs[3]*100, 'y', label="4 robots")
plt.plot(ind[4],sums_grid5/maxs[4]*100, 'k', label="5 robots")
plt.grid(True)
plt.legend()
plt.xlabel('Iterations')
plt.ylabel('Knowledge')
plt.title('Entropy Reduction')


plt.show()
