import pygame, time, random, os, math
import numpy as np
from pygame.math import Vector2
from math import tan, radians, degrees, copysign
from Display import Display
from ModeloSimples import ModeloSimples
from SimulatorModeloSimples import SimulatorModeloSimples

display = Display()
simulatorModeloSimples = SimulatorModeloSimples()
mouse = pygame.mouse.get_pos()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		if event.type == pygame.MOUSEBUTTONUP:
			mouse = pygame.mouse.get_pos()
			if 200 < mouse[0] < 1920 and 100 < mouse[1] < 1080:
				simulatorModeloSimples.objective = pygame.mouse.get_pos()
				simulatorModeloSimples.screen.blit(simulatorModeloSimples.objective_image, simulatorModeloSimples.objective)
				pygame.display.flip()
				simulatorModeloSimples.clock.tick(300)

	simulatorModeloSimples.run()
	display.menu()

	pygame.display.update()
