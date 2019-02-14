import pygame, time, random, os, math
import numpy as np
from pygame.math import Vector2
from math import tan, radians, degrees, copysign

# Classe do que vai ser mostrado na tela
class Display:
	# Dimensões
	display_width = 1920
	display_height = 1080

	# Clock
	clock = pygame.time.Clock()

	# Colors
	primary = (41, 98, 255)
	primary_light = (118, 143, 255)
	primary_dark = (0, 57, 203)

	secondary = (250, 250, 250)
	secondary_light = (255, 255, 255)
	secondary_dark = (199, 199, 199)

	black = (0, 0, 0)

	def __init__(self):
		# Ininialização do PyGame
		pygame.init()

		# Dimensões da janela
		self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
		
		# Título da janela
		pygame.display.set_caption('Robot Simulator')

		# Área do simulador
		self.gameDisplay.fill(self.secondary)

	def menu(self):
		self.gameDisplay.fill((255, 255, 255))
		# Barras do menu
		# Barra lateral
		pygame.draw.rect(self.gameDisplay, self.primary, (0, 100, 200, self.display_height))

		# Barra do topo
		pygame.draw.rect(self.gameDisplay, self.primary_dark, (0, 0, self.display_width, 100))

		# Linha lateral
		pygame.draw.rect(self.gameDisplay, self.black, (200, 100, 2, self.display_height))

		# Linha topo
		pygame.draw.rect(self.gameDisplay, self.black, (200, 100, self.display_width, 2))
		self.message_display("Robot Simulator", 950, 50, 50)

		# Posição do mouse
		self.mouse = pygame.mouse.get_pos()
		self.click = pygame.mouse.get_pressed()

		# Botões
		self.button(0, 100, 200, 98, "Simples", self.mouse, self.click, 1)
		self.button(0, 198, 200, 98, "Fila", self.mouse, self.click, 2)

	def button(self, x, y, width, height, text, mouse, click, action=None):
		# 1080 de altura. No máximo 8 botões e 40 de espaço para cada.
		# 8 botões com 40 de espaço entre eles.
		# 40 * 9 = 360 | 1080 - 360 = 720 | 720 / 8 = 90
		if x + width > mouse[0] > x and y + height > mouse[1] > y:
			pygame.draw.rect(self.gameDisplay, self.primary_light, (x, y, width, height))
			if click[0] == 1 and action != None:
				if action == 1:
					print(1)
				elif action == 2:
					print(2)
		else:
			pygame.draw.rect(self.gameDisplay, self.secondary_light, (x, y, width, height))

		self.message_display(text, x + 90, y + 40, 20)

	def text_objects(self, text, font):
		self.textSurface = font.render(text, True, self.black)
		return self.textSurface, self.textSurface.get_rect()

	def message_display(self, text, x, y, size):
		self.Text = pygame.font.Font('freesansbold.ttf', size)
		self.TextSurf, self.TextRect = self.text_objects(text, self.Text)
		self.TextRect.center = (x, y)
		self.gameDisplay.blit(self.TextSurf, self.TextRect)

# Carro
class Car:
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

	def go_to_goal(self,theta_a,sum_theta,kp=0.01,ki=0.000001,kd=0.000001):
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
			w = 0

		if euc_dis < 70:
			v = 0
			w = 0

		return [v, omega]

	def goal(self,objetivo):
		self.goal_x = objetivo[0]
		self.goal_y = objetivo[1]


	def show(self,screen):
		pygame.draw.polygon(screen, (255,0,0), [self.tip, self.bottom_l, self.bottom_r], 0)

# Classe da simulação
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
		self.car = Car(self.car_x, self.car_y, self.car_ang)
		self.car.goal(self.objective)
		self.car.show(self.screen)
		[vl,w] = self.car.go_to_goal(self.black_box["theta_a"], self.black_box["sum_theta"])
		self.car_x += vl * math.cos(self.car.angle)
		self.car_y += vl * math.sin(self.car.angle)
		self.car_ang += w

		self.black_box["theta_a"] = self.black_box["theta"]
		self.black_box["sum_theta"] += self.black_box["theta"]
		self.black_box["theta"] = self.car_ang

		self.screen.blit(self.objective_image, self.objective)
		pygame.display.flip()
		self.clock.tick(1000)

# Classe de execução 
class Main:
	def __init__(self):
		display = Display()
		simulator = Simulator()
		mouse = pygame.mouse.get_pos()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

				if event.type == pygame.MOUSEBUTTONUP:
					if 200 < mouse[0] < 1920 and 100 < mouse[1] < 1080:
						simulator.objective = pygame.mouse.get_pos()
						simulator.screen.blit(simulator.objective_image, simulator.objective)
						pygame.display.flip()
						simulator.clock.tick(300)
						print(simulator.objective)

			simulator.run()
			display.menu()

			pygame.display.update()

# Rodar o Main()
if __name__ == '__main__':
	Main()