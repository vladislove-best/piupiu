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
X_list=[]
y_list=[]
for i in range(9):
    X_list.append(i*90)
    y_list.append(i*90)
def hero(x,y):
    gameDisplay.blit(heroIMG, (x,y))
def hero2(x2,y2):
    gameDisplay.blit(hero2IMG, (x2,y2))
b_g_Img = pygame.image.load('mlg.jpg')
# ship = pygame.image.load("mlg.jpg")ip.get_height()
# ship_left = gameDisplay.get_width()/2 - ship.get_width()/2

gameDisplay.blit(b_g_Img,(0,0))
step = True

def move(x,y):
    finish = False
    while finish == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x = x-100
                elif event.key == pygame.K_RIGHT:
                    x = x+100
                elif event.key == pygame.K_UP:
                    y = y+100
                elif event.key == pygame.K_DOWN:
                    y = y-100
                finish = True
    return x,y
def spawn(D1,D2):
    if D1 == 1:
        x = X_list [random.randint(0,1)]
        y = y_list [random.randint(0,7)]
        hero(x,y)
    if D2 == 1:
        x2 = X_list [random.randint(6,7)]
        y2 = y_list [random.randint(0,7)]
        hero2(x2,y2)
    return x,y,x2,y2
clock = pygame.time.Clock()
gameS = True
crashed = False
if gameS == True:
    x,y,x2,y2 =spawn(1,1)
while not crashed:
    if step ==True:
        x,y= move(x,y)
        x,y= move(x,y)
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