import pygame
import sys


def run():

	print('Game started')
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption('Space defence')
	bg_color = (0, 0, 0)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("Game exit")
				sys.exit()

		screen.fill(bg_color)
		pygame.display.flip()

run()