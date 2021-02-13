import pygame
import random
pygame.init()
display_width = 700
display_height = 691
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('I kill you ,friend')
black = (0,0,0)
white = (255,255,255)
heroIMG = pygame.image.load('hero.jpg')
hero2IMG = pygame.image.load('hero2.jpg')

def hero(x,y):
    gameDisplay.blit(heroIMG, (x,y))
def hero2(x2,y2):
    gameDisplay.blit(hero2IMG, (x2,y2))
b_g_Img = pygame.image.load('mlg.jpg')
# ship = pygame.image.load("mlg.jpg")ip.get_height()
# ship_left = gameDisplay.get_width()/2 - ship.get_width()/2

gameDisplay.blit(b_g_Img,(0,0))

def spawn(D1,D2):
    if D1 == 1:
        x = random.randint(0,int(display_width/8*2))
        y = random.randint(0,display_height)
        hero(x,y)
    if D2 == 1:
        x2 = random.randint(int(display_width/8*7),int(display_width))
        y2 = random.randint(0,display_height)
        hero2(x2,y2)
clock = pygame.time.Clock()
gameS = True
crashed = False
if gameS == True:
    spawn(1,1)
while not crashed:
    # if HDead == True:
        # spawn(1,0)
    # if H2Dead == True:
        # spawn(0,1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    pygame.display.update()
    clock.tick(60)



pygame.quit()
quit()