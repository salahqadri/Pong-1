# Import required modules
import pygame

pygame.init()

# Constants
WIN_WIDTH, WIN_HEIGHT = 1280, 720

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game clock
FPS = 60
clock = pygame.time.Clock()

# Load images
game_icon = pygame.image.load('Assets/game icon.png')

# Set-up window
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Pong!')
pygame.display.set_icon(game_icon)

# Main function
def main():

	run = True
	# Main game loop
	while run:
		clock.tick(FPS)
		# Check for events in the game loop
		for event in pygame.event.get():
			# Break out of the loop if the exit window button is pressed
			if event.type == pygame.QUIT:
				run = False 

main()

pygame.quit()