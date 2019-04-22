import pandas as pd
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math 
import time
import threading
import sys

print('Opening serial...')
serial_port = serial.Serial(port = "COM5", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE) 
print('Serial opened')

zero = [(0, 0)]    
dataTD = pd.DataFrame(zero, columns = ['T' , 'D'])

fig = plt.figure()
ax = plt.subplot(111, projection='polar')
ax.grid(True)

def read_serial_to_df():
    while(1):
        buffer = serial_port.readline()
        decoded = buffer.decode('ascii').replace("\r","").replace("\n","")    
        xy = decoded.split(',')
        global dataTD
        try:
            xy[0] = 2.0*float(xy[0])*math.pi/2048.0           
            dataTD = dataTD.append({'T':xy[0], 'D':int(xy[1])}, ignore_index=True)
        except:
            print(xy)

def print_df():    
    while(1):
        global dataTD
        print(dataTD.size)
        time.sleep(1)
    
def animate(i):    
    ax.clear()   
    ax.plot(dataTD['T'], dataTD['D'], '.')

time.sleep(2)

print('Send START')
serial_port.write('777'.encode())

print('Thread starting...')
t1 = threading.Thread(target = read_serial_to_df)
#t2 = threading.Thread(target = print_df)
t1.start()
print('Thread started')

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show() 

time.sleep(20)

serial_port.write('999'.encode())
print('Send STOP') 

print(dataTD.head())

sys.exit(0)

    