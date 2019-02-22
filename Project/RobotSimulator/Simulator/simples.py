import pygame, time, random, os, math
import numpy as np
from pygame.math import Vector2
from math import tan, radians, degrees, copysign
import os

class Car:
	def __init__(self, x, y, angle=0, length=20,radius=10):
		self.x = x
		self.y = y
		self.position = np.array([x, y])
		self.angle = angle
		self.length = length
		self.radius = radius
		self.max_velocity = 0.13
		self.euc_dis = 0

		self.tip = [self.x + self.length * math.cos(self.angle), self.y + self.length * math.sin(self.angle)]
		self.bottom = [self.x - self.length * math.cos(self.angle), self.y - self.length * math.sin(self.angle)]
		self.bottom_l = [self.bottom[0] - self.radius * math.sin(self.angle), self.bottom[1] + self.radius * math.cos(self.angle)]
		self.bottom_r = [self.bottom[0] + self.radius * math.sin(self.angle), self.bottom[1] - self.radius * math.cos(self.angle)]

	def go_to_goal(self,theta_a,sum_theta,mode,kp=0.01,ki=0.0,kd=0.0):
		x_dis = self.goal_x - self.x
		y_dis = self.goal_y - self.y
		euc_dis = (x_dis ** 2 + y_dis ** 2) ** (1 / 2)


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

		if euc_dis < 70:
			v = 0
			omega = 0

		self.euc_dis = euc_dis
		return [v, omega]

	def euc_dis(self):
		return this.euc_dis

	def goal(self,objetivo):
		self.goal_x = objetivo[0]
		self.goal_y = objetivo[1]


	def show(self,screen):
		pygame.draw.polygon(screen, (255,0,0), [self.tip, self.bottom_l, self.bottom_r], 0)

class simples:

	display_width = 1920
	display_height = 1080

	pygame.init()
	gameDisplay = pygame.display.set_mode((display_width, display_height))
	pygame.display.set_caption('Robot Simulator - SimpleModel')
	gameDisplay.fill((255, 255, 255))

	def __init__(self):
		self.screen = self.gameDisplay
		self.clock = pygame.time.Clock()
		self.objective_path = os.path.join("../Images/flag.png")
		self.objective_image = pygame.image.load(self.objective_path)
		self.objective = [(272.5, 265.5)]
		self.car_x = 500; self.car_y = 500; self.car_ang = 0
		self.car = Car(self.car_x, self.car_y, self.car_ang)
		self.screen.blit(self.objective_image, self.objective[0])
		pygame.display.flip()
		self.black_box= {"theta": self.car_ang,
					"theta_a": 0,
					"sum_theta": 0}
		self.run()

	def runCar(self, mode):
		self.screen.fill((255, 255, 255))
		self.car = Car(self.car_x, self.car_y, self.car_ang)
		self.car.goal(self.objective[0])
		self.car.show(self.screen)
		[vl,w] = self.car.go_to_goal(self.black_box["theta_a"], self.black_box["sum_theta"], mode)
		self.car_x += vl * math.cos(self.car.angle)
		self.car_y += vl * math.sin(self.car.angle)
		self.car_ang += w


		self.black_box["theta_a"] = self.black_box["theta"]
		self.black_box["sum_theta"] += self.black_box["theta"]
		self.black_box["theta"] = self.car_ang

		i = 0
		while i < len(self.objective):
			self.screen.blit(self.objective_image, self.objective[i])
			# pygame.display.flip()
			self.clock.tick(1000)
			i = i + 1

		self.screen.blit(self.objective_image, self.objective[0])
		pygame.display.flip()
		self.clock.tick(1000)

	def run(self):
		objective = [(272.5, 265.5)]
		mouse = pygame.mouse.get_pos()
		mode = 1

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

				if event.type == pygame.MOUSEBUTTONUP:
					objective = []
					objective.append((pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))


			if self.car.euc_dis < 70:
				if len(objective) > 1:
					objective.pop(0)
			self.objective = objective

			self.runCar(mode)

			pygame.display.update()

simples()
