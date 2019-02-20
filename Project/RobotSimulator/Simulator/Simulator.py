import pygame, time, random, os, math
import numpy as np
from pygame.math import Vector2
from math import tan, radians, degrees, copysign
from Display import Display
from ModeloSimples import ModeloSimples

class Simulator:
	display = Display()
	screen = display.gameDisplay
	clock = display.clock
	objective_path = os.path.join("../Images/flag.png")
	objective_image = pygame.image.load(objective_path)
	objective = Vector2(272.5, 265.5)
	car_x = 500; car_y = 500; car_ang = 0

	def __init__(self):
		self.screen.blit(self.objective_image, self.objective)
		pygame.display.flip()
		self.black_box= {"theta": self.car_ang,
					"theta_a": 0,
					"sum_theta": 0}

	def run(self):
		self.modeloSimples = ModeloSimples(self.car_x, self.car_y, self.car_ang)
		self.modeloSimples.goal(self.objective)
		self.modeloSimples.show(self.screen)
		[vl,w] = self.modeloSimples.go_to_goal(self.black_box["theta_a"], self.black_box["sum_theta"])
		self.car_x += vl * math.cos(self.modeloSimples.angle)
		self.car_y += vl * math.sin(self.modeloSimples.angle)
		self.car_ang += w

		self.black_box["theta_a"] = self.black_box["theta"]
		self.black_box["sum_theta"] += self.black_box["theta"]
		self.black_box["theta"] = self.car_ang

		self.screen.blit(self.objective_image, self.objective)
		pygame.display.flip()
		self.clock.tick(1000)
