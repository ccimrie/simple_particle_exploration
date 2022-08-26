import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import cv2

# coverage=np.zeros([N,1])
agent_radius=0.05

setup_txt=open('setup.txt')
setup=np.loadtxt(setup_txt)
# print(setup)
radius=float(setup[0])
time=int(setup[1])
scale=100.0

dist_x, dist_y=np.meshgrid(np.arange(-(radius),(radius),1.0/scale),np.arange(-(radius),(radius),1.0/scale))
dist=np.sqrt(dist_x*dist_x+dist_y*dist_y)

coverage_t=np.zeros(time)

pos_txt=open("pos.txt")

## Area coverage
## 2 slices: one for initial and one for coverage by particle (can increase for comparative experiments)
area=np.zeros([int((radius)*2*scale),int((radius)*2*scale),2])

for i in np.arange(np.shape(area)[0]):
    for j in np.arange(np.shape(area)[1]):
        if dist[i,j]>radius:
            area[i,j,0]=1

pos=np.loadtxt(pos_txt)
t=len(pos)

area[:,:,0]=area[:,:,0]>0
area[:,:,1]=area[:,:,0]
# area[:,:,2]=area[:,:,0]

area_unexplored=np.sum(np.sum(area[:,:,0]<1))


for tt in np.arange(t):
    # BROWNIAN RECORDING
    new_pos=pos[tt,:]
    dist_x_temp=dist_x-new_pos[0]
    dist_y_temp=dist_y-new_pos[1]
    dist_temp=np.sqrt(dist_x_temp*dist_x_temp+dist_y_temp*dist_y_temp)
    area_temp=dist_temp<agent_radius
    area[:,:,1]=area[:,:,1]+area_temp
    area[:,:,1]=area[:,:,1]>0
    coverage_t[tt]=float(area_unexplored-np.sum(np.sum(area[:,:,1]<1)))/area_unexplored

area[:,:,1]=area[:,:,1]>0
# area[:,:,2]=area[:,:,2]>0

explored=float(area_unexplored-np.sum(np.sum(area[:,:,1]<1)))/area_unexplored

## For averages(?)
# coverage[n-1]=explored

print("Explored: "+str(np.round(explored*100,2))+"%")

## Showing before and after
# cv2.imshow("Before", area[:,:,0])
# cv2.imshow("After", area[:,:,1])
# cv2.waitKey(1000)

## Saving before and after
cv2.imwrite('test_before.png',area[:,:,0]*255)
cv2.imwrite('test_after.png',area[:,:,1]*255)

## Plot area exploration timecourse
fig=plt.figure()
plt.plot(np.arange(time), coverage_t*100)
plt.legend()
plt.ylabel('Area covered (%)')
plt.xlabel('Timestep')
plt.show()