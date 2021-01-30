#beta of beta 
import pygame
pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('I kill you ,friend')
black = (0,0,0)
white = (255,255,255)

b_g_Img = pygame.image.load('mlg.jpg')
ship = pygame.image.load("mlg.jpg")
ship_top = gameDisplay.get_height() - ship.get_height()
ship_left = gameDisplay.get_width()/2 - ship.get_width()/2

gameDisplay.blit(ship, (ship_left,ship_top))

clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    pygame.display.update()
    clock.tick(60)



pygame.quit()
quit()