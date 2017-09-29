import pygame
pygame.init()

display_width = 1000
display_height = 600

#######IN RGB
black=(0,0,0)
whit=(255,255,255)
red=(255,0,0)
broun=(210,105,30)

Rat_image = pygame.image.load('ratn.png')
chees_image = pygame.image.load('chees.png')
back_image = pygame.image.load('w.gif')

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('The Chowa Game')
clock = pygame.time.Clock()

def rat(x,y):
	gameDisplay.blit(Rat_image,(x,y))
	gameDisplay.blit(chees_image,(x+200,y-200))

x = (-75+display_width /2  )
y = (display_height -150)

crash = False

while not crash:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crash = True
	
	gameDisplay.fill(whit)
	gameDisplay.blit(back_image,(0,0))
	rat(x,y)
	pygame.display.update()
	clock.tick(50)
	

pygame.quit()
quit()