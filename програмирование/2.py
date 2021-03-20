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
boxIMG = pygame.image.load('box.png')
right = False
left = False
up = False
down = False
right2 = False
left2 = False
up2 = False
down2 = False
X_list=[]
Y_list=[]
for i in range(9):
    X_list.append(i*90)
    Y_list.append(i*90)
print(X_list)
a = 0
a2 = 0
b = 0
b2 = 0
allbox = 0
xb = 0
yb = 0
Bx = []
By = []
for i in range(8):
    Bx.append(0)
    By.append(0)
def hero(x,y):
    gameDisplay.blit(heroIMG, (x,y))

def hero2(x2,y2):
    gameDisplay.blit(hero2IMG, (x2,y2))

def box(bx,by):
    gameDisplay.blit(boxIMG, (bx,by))

b_g_Img = pygame.image.load('mlg.jpg')
# ship = pygame.image.load("mlg.jpg")ip.get_height()
# ship_left = gameDisplay.get_width()/2 - ship.get_width()/2

gameDisplay.blit(b_g_Img,(0,0))
step = True
def move(x,y,a,b):
    if right == True and a < 7:
        a = a+1
        x = X_list[a]  
    if left == True and a > 0:
        a = a-1
        x = X_list[a]  
    if up == True and b > 0:
        b = b-1
        y = Y_list[b]  
    if down == True and b < 7:
        b=b+1
        y = Y_list[b]
    if x==Bx[i] and  or y == bx or by:
        
    return x,y,b,a
def spawn(D1,D2):
    if D1 == 1:    
        a = random.randint(0,1)   
        b = random.randint(0,7)    
        x = X_list[a]    
        y = Y_list[b]    
        hero(x,y)    
    if D2 == 1:    
        a2 = random.randint(6,7)   
        b2 = random.randint(0,7)    
        x2 = X_list[a2]    
        y2 = Y_list[b2]    
        hero2(x2,y2)    
    return a,b,a2,b2
clock = pygame.time.Clock()
gameS = True
crashed = False
if gameS == True:
    a,b,a2,b2 =spawn(1,1)
    x = X_list[a]    
    y = Y_list[b]
    x2 = X_list[a2]    
    y2 = Y_list[b2]
while not crashed:
    if allbox < 8:
        Bx[allbox] = X_list[random.randint(2,5)]
        By[allbox] = Y_list[random.randint(0,7)]
        allbox = allbox + 1
    for event in pygame.event.get():
        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            elif event.key == pygame.K_RIGHT:
                right = True
            elif event.key == pygame.K_UP:
                up = True
            elif event.key == pygame.K_DOWN:
                down = True
         ############################
            if step ==True: 
                x,y,b,a = move(x,y,a,b)
                print(x,y)      
                left = False
                right = False
                up = False
                down = False
                step = False
            else:
                x2,y2,b2,a2 = move(x2,y2,a2,b2)
                left = False
                right = False
                up = False
                down = False 
                step = True           
    gameDisplay.blit(b_g_Img,(0,0))
    for i in range (8):
        box(Bx[i],By[i])
    hero(x,y)
    hero2(x2,y2)
    # if HDead == True:
        # spawn(1,0)    
    # if H2Dead == True:
        # spawn(0,1)    
    if event.type == pygame.QUIT:       
        crashed = True     
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()