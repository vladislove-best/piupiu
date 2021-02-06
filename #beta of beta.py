#beta of beta 
import pygame
import random
pygame.init()
display_width = 1000
display_height = 1000
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('I kill you ,friend')
black = (0,0,0)
white = (255,255,255)
hero = pygame.image.load('hero.png')
hero2 = pygame.image.load('hero2.png')

def hero(x,y):
    gameDisplay.blit(hero, (x,y))
def hero2(x,y):
    gameDisplay.blit(hero2, (x,y))
b_g_Img = pygame.image.load('mlg.jpg')
ship = pygame.image.load("mlg.jpg")
ship_top = gameDisplay.get_height() - ship.get_height()
ship_left = gameDisplay.get_width()/2 - ship.get_width()/2

gameDisplay.blit(ship, (ship_left,ship_top))

def spawn(D1,D2):
    if D == 1:
        x = random.randint(0,int(display_width/8*2))
        y = random.randint(0,display_height)
    if D2 == 1:
        x2 = rand.int(int(display_width/8*7),int(display_width))
        y2 = rand.int(0,display_height)
clock = pygame.time.Clock()
gameS = True
crashed = False
if gameS = True:
    spawn(1,1)
while not crashed:
    if HDead = True:
        spawn(1,0)
    if H2Dead = True:
        spawn(0,1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    pygame.display.update()
    clock.tick(60)



pygame.quit()
quit()