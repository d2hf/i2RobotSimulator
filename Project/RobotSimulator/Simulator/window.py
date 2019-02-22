import pygame, os

class window:

	clock = pygame.time.Clock()

	primary = (41, 98, 255)
	primary_light = (118, 143, 255)
	primary_dark = (0, 57, 203)

	secondary = (250, 250, 250)
	secondary_light = (255, 255, 255)
	secondary_dark = (199, 199, 199)

	black = (0, 0, 0)
	white = (255, 255, 255)

	display_width = 800
	display_height = 600

	pygame.init()
	gameDisplay = pygame.display.set_mode((display_width, display_height))
	pygame.display.set_caption('Robot Simulator - Menu')
	gameDisplay.fill((255, 255, 255))

	def __init__(self):
		self.run()

	def menu(self):
		# self.gameDisplay.fill((255, 255, 255))
		self.message_display("Robot Simulator", 400, 50, 50)

		self.mouse = pygame.mouse.get_pos()
		self.click = pygame.mouse.get_pressed()

		self.button(300, 200, 200, 98, "Simples", self.mouse, self.click, 1)
		self.button(300, 350, 200, 98, "Fila", self.mouse, self.click, 2)

	def button(self, x, y, width, height, text, mouse, click, action=None):
		if x + width > mouse[0] > x and y + height > mouse[1] > y:
			pygame.draw.rect(self.gameDisplay, self.primary_light, (x, y, width, height))
			if click[0] == 1 and action != None:
				if action == 1:
					os.system("python simples.py")
				elif action == 2:
					os.system("python fila.py")
		else:
			pygame.draw.rect(self.gameDisplay, self.secondary_light, (x, y, width, height))

		self.message_display(text, x + 95, y + 50, 20)

	def text_objects(self, text, font):
		self.textSurface = font.render(text, True, self.black)
		return self.textSurface, self.textSurface.get_rect()

	def message_display(self, text, x, y, size):
		self.Text = pygame.font.Font('freesansbold.ttf', size)
		self.TextSurf, self.TextRect = self.text_objects(text, self.Text)
		self.TextRect.center = (x, y)
		self.gameDisplay.blit(self.TextSurf, self.TextRect)

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()			

			self.menu()
			pygame.display.update()

window()