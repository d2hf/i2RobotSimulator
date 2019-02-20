import pygame, time, random, os, math
import numpy as np
from pygame.math import Vector2
from math import tan, radians, degrees, copysign

class ModeloSimples:
	def __init__(self, x, y, angle=0, length=20,radius=10):
		self.x = x
		self.y = y
		self.position = np.array([x, y])
		self.angle = angle
		self.length = length
		self.radius = radius
		self.max_velocity = 0.13

		self.tip = [self.x + self.length * math.cos(self.angle), self.y + self.length * math.sin(self.angle)]
		self.bottom = [self.x - self.length * math.cos(self.angle), self.y - self.length * math.sin(self.angle)]
		self.bottom_l = [self.bottom[0] - self.radius * math.sin(self.angle), self.bottom[1] + self.radius * math.cos(self.angle)]
		self.bottom_r = [self.bottom[0] + self.radius * math.sin(self.angle), self.bottom[1] - self.radius * math.cos(self.angle)]

	def go_to_goal(self,theta_a,sum_theta,kp=0.01,ki=0,kd=0):
		x_dis = self.goal_x - self.x
		y_dis = self.goal_y - self.y
		euc_dis = (x_dis ** 2 + y_dis ** 2) ** (1 / 2)
		print(euc_dis)

		theta_r = math.atan2(y_dis, x_dis)
		delta_theta = theta_r - self.angle
		omega = kp * math.atan2(math.sin(delta_theta),math.cos(delta_theta)) + sum_theta * ki + (self.angle - theta_a) * kd

		if delta_theta < 0:
			vr = self.max_velocity
			vl = vr - (omega * self.length) / self.radius
			v = ((vr + vl) / 2) * self.radius

		elif delta_theta > 0:
			vl = self.max_velocity
			vr =  vl + (omega * self.length) / self.radius
			v = ((vr + vl) / 2) * self.radius

		else:
			v = self.max_velocity
			omega = 0

		if euc_dis < 70:
			v = 0
			omega = 0

		return [v, omega]

	def goal(self,objetivo):
		self.goal_x = objetivo[0]
		self.goal_y = objetivo[1]


	def show(self,screen):
		pygame.draw.polygon(screen, (255,0,0), [self.tip, self.bottom_l, self.bottom_r], 0)
