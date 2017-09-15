import pygame
pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('The Chawa Game')
clock = pygame.time.Clock()

crash = False

while not crash:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crash = True

		print(event)

	pygame.display.update()

	clock.tick(50)

pygame.quit()
quit()