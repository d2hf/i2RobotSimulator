import pygame, time

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
