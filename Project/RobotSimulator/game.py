import pygame, time, random

pygame.init()

display_width = 1920
display_height = 1080

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()

carImg = pygame.image.load('../differential2.jpeg')

def game_intro():

	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(white)

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x, y):
	gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
	textSurface = font.render(text, True, red)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width / 2), (display_height / 2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(2)

	game_loop()

def crash():
	message_display('You Crashed')

def game_loop():
	x = (display_width * 0.5)
	y = (display_height * 0.5)

	x_change = 0
	y_change = 0

	thing_starty = -100
	thing_speed = 15
	thing_width = 100
	thing_height = 100
	thing_startx = random.randrange(0, display_width - thing_width)

	gameExit = False

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5
				elif event.key == pygame.K_RIGHT:
					x_change = 5
				if event.key == pygame.K_UP:
					y_change = -5
				elif event.key == pygame.K_DOWN:
					y_change = 5
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0

		x += x_change
		y += y_change

		gameDisplay.fill(black)

		things(thing_startx, thing_starty, thing_width, thing_height, red)
		thing_starty += thing_speed

		car(x, y)

		if x > display_width or x < 0:
			crash()

		if thing_starty > display_height:
			thing_starty = -100
			thing_startx = random.randrange(0, display_width - thing_width)

		if y < thing_starty + thing_height:
			if x > thing_startx and x < thing_startx + thing_width:
				crash()

		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()