import numpy as np

class particle(object):
	def __init__(self, _pos_x, _pos_y, _max_vel):
		self.pos_x=_pos_x
		self.pos_y=_pos_y
		self.max_vel=_max_vel

		self.vel_x=0
		self.vel_y=0

	def updateVel(self, _vel_x, _vel_y):
		self.vel_x=_vel_x
		self.vel_y=_vel_y

		## Check if we are faster than max vel
		vel_mag=self.vel_x**2+self.vel_y**2
		if vel_mag>self.max_vel**2:
			vel_frac=np.sqrt(vel_mag)/self.max_vel
			self.vel_x=self.vel_x/vel_frac
			self.vel_y=self.vel_y/vel_frac

	def rotate(self, theta):
		vel_x_temp=np.cos(theta)*self.vel_x-np.sin(theta)*self.vel_y
		vel_y_temp=np.cos(theta)*self.vel_y+np.sin(theta)*self.vel_x
		self.updateVel(vel_x_temp, vel_y_temp)

	def moveStep(self):
		self.pos_x=self.pos_x+self.vel_x
		self.pos_y=self.pos_y+self.vel_y

	def setPos(self, _pos_x, _pos_y):
		self.pos_x=_pos_x
		self.pos_y=_pos_y

	def getPos(self):
		return np.array([self.pos_x, self.pos_y])