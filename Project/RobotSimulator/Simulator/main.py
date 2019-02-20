import pygame, time, random, os, math
import numpy as np
from pygame.math import Vector2
from math import tan, radians, degrees, copysign
from Display import Display
from ModeloSimples import ModeloSimples
from Simulator import Simulator

display = Display()
simulator = Simulator()
mouse = pygame.mouse.get_pos()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.MOUSEBUTTONUP:
			mouse = pygame.mouse.get_pos()
			if 200 < mouse[0] < 1920 and 100 < mouse[1] < 1080:
				simulator.objective = pygame.mouse.get_pos()
				simulator.screen.blit(simulator.objective_image, simulator.objective)
				pygame.display.flip()
				simulator.clock.tick(300)

	simulator.run()
	display.menu()

	pygame.display.update()
