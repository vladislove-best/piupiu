import pygame
import random
pygame.init()
display_width = 850
display_height = 691
gameDisplay = pygame.display.set_mode((display_width,display_height))
itemsbar = pygame.image.load('items.png')
b_g_Img = pygame.image.load('mlg.jpg')
gameDisplay.blit(itemsbar,(768,0))
gameDisplay.blit(itemsbar,(768,491))
gameDisplay.blit(b_g_Img,(0,0))
pygame.display.set_caption('XCOM 0.0.0.0.0.1')
black = (0,0,0)
white = (255,255,255)
swordIMG = pygame.image.load('sword.png')
staminIMG = pygame.image.load('stamin.png')
healthIMG = pygame.image.load('health.png')
heroIMG = pygame.image.load('hero.jpg')
hero2IMG = pygame.image.load('hero2.jpg')
boxIMG = pygame.image.load('box.png')
darkIMG = pygame.image.load('dark.png')
hero_a = 0
hero_b = 0
hero2_a = 0
hero2_b = 0
b = [0,0]
a = [0,0]
cell_size=90
D1 = 0
D2 = 0
def sword (x,y):
    gameDisplay.blit(swordIMG, (x,y))
def health (x,y):
    gameDisplay.blit(healthIMG, (x,y))
def dark (x,y):
    gameDisplay.blit(darkIMG, (x,y))
def stamin (x,y):
    gameDisplay.blit(staminIMG, (x,y))
def hero(x,y):
    gameDisplay.blit(heroIMG, (x*cell_size,y*cell_size))
def hero2(x2,y2):
    gameDisplay.blit(hero2IMG, (x2*cell_size,y2*cell_size))
def box(bx,by):
    gameDisplay.blit(boxIMG, (bx,by))
def spawn(D1,D2):
    if D1 == 1: 
        hero_a = random.randint(0,1) 
        hero_b = random.randint(0,7) 
        hero(hero_a,hero_b) 
    if D2 == 1: 
        hero2_a = random.randint(6,7) 
        hero2_b = random.randint(0,7) 
        hero2(hero2_a,hero2_b) 
    D1 = 0
    D2 = 0  
    return hero_a,hero_b,hero2_a,hero2_b
def move (hero_a,hero_b):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero_a = hero_a - cell_size
            elif event.key == pygame.K_RIGHT:
                hero_a = hero_a + cell_size
            elif event.key == pygame.K_UP:
                hero_b = hero_b + cell_size
            elif event.key == pygame.K_DOWN:
                hero_b = hero_b - cell_size
crashed = False
while not crashed:
    health(740,0)
    health(740,70)
    health(740,140)
    health(740,491)
    health(740,561)
    health(740,631)
    spawn(1,1)
    move(hero_a,hero_b)
