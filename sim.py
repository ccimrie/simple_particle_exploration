import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import cv2

setup_txt=open('setup.txt')
pos_txt=open('pos.txt')

setup=np.loadtxt(setup_txt)
radius=setup[0]

fig=plt.figure()

speed=int(sys.argv[1])

if speed==0:
    speed=1

# Setting up animation of simulation    
ax_sim=plt.subplot(111)
ax_sim.set_xlim([-radius-0.1, radius+0.1])
ax_sim.set_ylim([-radius-0.1, radius+0.1])

xCirc=np.sin(np.linspace(-np.pi,np.pi))*radius
yCirc=np.cos(np.linspace(-np.pi,np.pi))*radius

ax_sim.set_aspect('equal')
circle=ax_sim.plot(xCirc,yCirc)

pos=np.loadtxt(pos_txt)
t=int(setup[1])

points=ax_sim.scatter(pos[0,0], pos[0,1], marker='o', color=(1,0,0))

def animate(t):
    if t==1:
        plt.waitforbuttonpress()
    t_ind=t*speed
    new_pos=pos[t_ind,:]
    points.set_offsets(np.c_[new_pos[0], new_pos[1]])
 
    plt.title(t_ind)

    return points, 

sim_ani=animation.FuncAnimation(fig, animate, frames=t-1, interval=50, blit=False, repeat=False)
plt.show()