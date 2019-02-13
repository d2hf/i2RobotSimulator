import pygame, time, random

# Classe do que vai ser mostrado na tela
class Display:
	# Dimensões
	display_width = 1920
	display_height = 1080

	# Clock
	clock = pygame.time.Clock()

	# Colors
	black = (0, 0, 0)
	white = (255, 255, 255)
	gray = (211, 211, 211)

	def __init__(self):
		# Ininialização do PyGame
		pygame.init()

		# Dimensões da janela
		self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
		
		# Título da janela
		pygame.display.set_caption('Robot Simulator')

	def menu(self):
		# Área do simulador
		self.gameDisplay.fill(self.white)

		# Barras do menu
		pygame.draw.rect(self.gameDisplay, self.black, (0, 0, 300, self.display_height))
		pygame.draw.rect(self.gameDisplay, self.black, (300, 0, self.display_width - 300, 130))
		self.message_display("Robot Simulator", 1050, 60, 50)

		# Posição do mouse
		self.mouse = pygame.mouse.get_pos()
		self.click = pygame.mouse.get_pressed()

		# Botões
		self.button(50, 40, 200, 90, "Simples", self.mouse, self.click, 1)
		self.button(50, 170, 200, 90, "Simples", self.mouse, self.click, 2)

	def button(self, x, y, width, height, text, mouse, click, action=None):
		# 1080 de altura. No máximo 8 botões e 40 de espaço para cada.
		# 8 botões com 40 de espaço entre eles.
		# 40 * 9 = 360 | 1080 - 360 = 720 | 720 / 8 = 90
		if x + width > mouse[0] > x and y + height > mouse[1] > y:
			pygame.draw.rect(self.gameDisplay, self.gray, (x, y, width, height))
			if click[0] == 1 and action != None:
				if action == 1:
					print(1)
				elif action == 2:
					print(2)
		else:
			pygame.draw.rect(self.gameDisplay, self.white, (x, y, width, height))

		self.message_display(text, x + 90, y + 40, 20)

	def text_objects(self, text, font):
		self.textSurface = font.render(text, True, self.gray)
		return self.textSurface, self.textSurface.get_rect()

	def message_display(self, text, x, y, size):
		self.Text = pygame.font.Font('freesansbold.ttf', size)
		self.TextSurf, self.TextRect = self.text_objects(text, self.Text)
		self.TextRect.center = (x, y)
		self.gameDisplay.blit(self.TextSurf, self.TextRect)

# Classe da simulação
class Simulator:
	def __init__(self):
		print('')

# Classe de execução 
class Main:
	def __init__(self):
		display = Display()
		simulator = Simulator()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			display.menu()

			pygame.display.update()


# Rodar o Main()
if __name__ == '__main__':
	Main()