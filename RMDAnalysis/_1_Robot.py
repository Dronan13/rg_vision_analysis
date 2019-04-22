import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style, markers
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import ShowFunc as sf
from matplotlib.patches import Circle, PathPatch
import mpl_toolkits.mplot3d.art3d as art3d
import math
from itertools import product, combinations

style.use('ggplot')

def animated_frames2d(i):  
    frame = pd.DataFrame(np.vstack(df['points'][i*speed]), columns=['X', 'Y', 'Z', 'D']) 
    ax2d.clear() 
    ax2d.set_aspect("equal")    
    fov = plt.Circle((positions['X'][i*speed], positions['Z'][i*speed]), 20, color='r',fill=False)
    ax2d.add_artist(fov)    
    ax2d.plot([-52, -52, 52, 52, -52], [-52, 52, 52, -52, -52], color='black')
    ax2d.scatter(positions['X'][i*speed], positions['Z'][i*speed], c='r', marker='*', s = 20)
    ax2d.scatter(frame['X'], frame['Z'], c='b', marker='.', s = 1) 
    
def show_vision2d():       
    anim = animation.FuncAnimation(fig, animated_frames2d, interval=10)
    plt.axis('equal')
    plt.show()

def animated_frames3d(i):  
    frame = pd.DataFrame(np.vstack(df['points'][i*speed]), columns=['X', 'Y', 'Z', 'D']) 
    ax3d.clear()    
    
    x = np.array([-20, -20, 20, 20,-20, -20, 20, 20]) + positions['X'][i*speed]
    y = np.array([-20, 20, 20, -20, -20, 20, 20, -20]) + positions['Z'][i*speed]
    z = np.array([-3, -3, -3, -3, 4, 4, 4, 4]) + positions['Y'][i*speed]
    ax3d.scatter(x, y, z, color='black')
    
    ax3d.scatter(positions['X'][i*speed], positions['Z'][i*speed], positions['Y'][i*speed], c='r', marker='.', s = 200)
    ax3d.scatter(frame['X'], frame['Z'], frame['Y'], c='b', marker='.', s = 1)
    ax3d.set_aspect('equal')#7/40
        
def show_vision3d():       
    anim = animation.FuncAnimation(fig, animated_frames3d, interval=10)  
    plt.show()    

def animated_frames(i):  
    frame = pd.DataFrame(np.vstack(df['points'][i*speed]), columns=['X', 'Y', 'Z', 'D'])
    
    ax2d.clear() 
    ax3d.clear()
    ax2d.set_aspect("equal")    
    fov = plt.Circle((positions['X'][i*speed], positions['Z'][i*speed]), 20, color='r',fill=False)
    ax2d.add_artist(fov)    
    ax2d.plot([-52, -52, 52, 52, -52], [-52, 52, 52, -52, -52], color='black')
    ax2d.scatter(positions['X'][i*speed], positions['Z'][i*speed], c='r', marker='*', s = 20)
    ax2d.scatter(frame['X'], frame['Z'], c='b', marker='.', s = 1) 
           
    x = np.array([-20, -20, 20, 20,-20, -20, 20, 20]) + positions['X'][i*speed]
    y = np.array([-20, 20, 20, -20, -20, 20, 20, -20]) + positions['Z'][i*speed]
    z = np.array([-3, -3, -3, -3, 4, 4, 4, 4]) + positions['Y'][i*speed]
    ax3d.scatter(x, y, z, color='black')
    
    ax3d.scatter(positions['X'][i*speed], positions['Z'][i*speed], positions['Y'][i*speed], c='r', marker='.', s = 200)
    ax3d.scatter(frame['X'], frame['Z'], frame['Y'], c='b', marker='.', s = 1)
    ax3d.set_aspect('equal')
    
def show_vision():       
    anim = animation.FuncAnimation(fig, animated_frames, interval=10)  
    plt.show()    

#Main data frame (All data)

df = pd.read_json('E:/experiments/mode_Group#1/R1/frames/FE1.json')
print('Total frames:', df['points'].size)
positions = pd.DataFrame(np.vstack(df['position']), columns=['X', 'Y', 'Z'])
rotations = pd.DataFrame(np.vstack(df['roation']), columns=['X', 'Y', 'Z'])

speed=3
fig = plt.figure()
ax2d = fig.add_subplot(121)  
ax3d = fig.add_subplot(122, projection='3d') #3d cloud
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
sums_grid1 = np.loadtxt('E:/experiments/mode_Group#1/common/maps/sums.txt').astype(int)
N1 = len(sums_grid1)
ind1 = np.arange(N1)
max1 = max(sums_grid1)
plt.plot(ind1,sums_grid1/max1*100)
plt.xlabel('Iterations')
plt.ylabel('Knowledge')
plt.title('Entropy Reduction')
plt.show()


#show_vision()
#show_vision2d()
#show_vision3d()        

