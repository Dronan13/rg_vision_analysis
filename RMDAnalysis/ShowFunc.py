import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style, markers
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

#Map
def show_frame():
    plt.plot([-52, -52, 52, 52, -52], [-52, 52, 52, -52, -52])
    plt.axis('equal')
    plt.grid(True)

#movement
def show_movement(df,rc):
    positions = pd.DataFrame(np.vstack(df['position']), columns=['X', 'Y', 'Z'])
    plt.scatter(positions['X'], positions['Z'], s=1, c=rc, marker=".")

#Map
def show_map(df, rc):
    map = pd.DataFrame(np.vstack(df['points']), columns=['X', 'Y', 'Z', 'D'])
    plt.scatter(map['X'], map['Z'], s=1, c=rc, marker=".")

    #plt.show()
    
#Frame 3D
def show_frame3d(df, frame_num):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect('equal')
    
    frame = pd.DataFrame(df['points'][frame_num], columns=['X', 'Y', 'Z', 'D'])
    ax.scatter(frame['X'],frame['Z'],frame['Y'], c='b', marker='.')

#Frames 2D
def show_frame2d(df, frame_num):
    bigmap = pd.DataFrame(np.vstack(df['points'][frame_num]), columns=['X', 'Y', 'Z', 'D'])
    bigmap.plot(x='X',y='Z', color='b', style='.', markersize=1)
    plt.plot([-52, -52, 52, 52, -52], [-52, 52, 52, -52, -52])
    plt.axis('equal')
    plt.grid(True)
    #plt.show()
    
   

    
def show_map3d(df):
    bigmap = pd.DataFrame(np.vstack(df['points']), columns=['X', 'Y', 'Z', 'D'])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect('equal')
    ax.scatter(bigmap['X'],bigmap['Z'],bigmap['Y'], c='b', marker='.')

