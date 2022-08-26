from particle import particle
import numpy as np

def checkBoundary(p,radius):
	pos=p.getPos()
	dist=pos[0]**2+pos[1]**2
	if dist>radius**2:
		frac=np.sqrt(dist)/radius
		pos=pos/frac
	p.setPos(pos[0],pos[1])

p=particle(0,0,0.01)
p.updateVel(np.random.rand()*0.5, np.random.rand()*0.5)

## Size of world
radius=1.0

TT=1.5e3

pos_file=open("pos.txt","w")

setup_file=open("setup.txt","w")

setup_file.write(str(radius)+" "+str(TT))

## Act: 0=straight, 1=left, 2=right
act=0

for t in np.arange(TT):
	p.moveStep()
	checkBoundary(p,radius)
	pos=p.getPos()
	string=str(pos[0])+" "+str(pos[1])+"\n"
	pos_file.write(string)
	prob=np.random.rand()

	if t%10==0:
		## Brownian motion (radians for rotating)
		## Turn left
		if prob<1.0/3:
			act=1
			# p.rotate(0.1)
		## Turn right
		elif prob<2.0/3:
			act=2
			# p.rotate(-0.1)
		## Else keep straight
		else:
			act=0
	if act==1:
		p.rotate(0.1)
	elif act==2:
		p.rotate(-0.1)
