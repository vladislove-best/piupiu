#backup
import pygame
import random
pygame.init()
display_width = 850
display_height = 691
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('XCOM 0.0.0.0.0.1')
black = (0,0,0)
white = (255,255,255)
death2IMG = pygame.image.load('смэрть2.png')
deathIMG = pygame.image.load('смэрть.png')
whiteIMG = pygame.image.load('white.png')
sword_invIMG = pygame.image.load('sword_in_bag.png')
swordIMG = pygame.image.load('sword.png')
staminIMG = pygame.image.load('stamin.png')
healthIMG = pygame.image.load('health.png')
heroIMG = pygame.image.load('hero.jpg')
hero2IMG = pygame.image.load('hero2.jpg')
boxIMG = pygame.image.load('box.png')
darkIMG = pygame.image.load('dark.png')
right = False
left = False
up = False
down = False
right2 = False
left2 = False
up2 = False
down2 = False
punch = False
P1_sword = False
P2_sword = False
alldeths = 0
alldeths2 = 0
allbox = 0
X_list=[]
Y_list=[]
for i in range(9):
    X_list.append(i*90)
    Y_list.append(i*90)
# print(X_list)
allsteps = 0
allstep = 0
steps_passed=0
a1 = 0
a2 = 0
b1 = 0
b2 = 0
xb = 0
yb = 0
Sx = []
Sy = []
Bx = []
By = []
INV_p1 = []
# for i in range(3):
#     Sx.append(0)
#     Sy.append(0) 
for i in range(8):
    Bx.append(0)
    By.append(0)
def death (x,y):
    gameDisplay.blit(deathIMG, (x,y))

def death2 (x,y):
    gameDisplay.blit(death2IMG, (x,y))

def whiteINV (x,y):
    gameDisplay.blit(whiteIMG, (x,y))

def sword (x,y):
    gameDisplay.blit(swordIMG, (x,y))

def sword_inv (x,y):
    gameDisplay.blit(sword_invIMG, (x,y))

def health (x,y):
    gameDisplay.blit(healthIMG, (x,y))

def dark (x,y):
    gameDisplay.blit(darkIMG, (x,y))

def stamin (x,y):
    gameDisplay.blit(staminIMG, (x,y))

def hero(x,y):
    gameDisplay.blit(heroIMG, (x,y))

def hero2(x2,y2):
    gameDisplay.blit(hero2IMG, (x2,y2))

def box(bx,by):
    gameDisplay.blit(boxIMG, (bx,by))
itemsbar = pygame.image.load('items.png')
b_g_Img = pygame.image.load('mlg.jpg')
# ship = pygame.image.load("mlg.jpg")ip.get_height()
# ship_left = gameDisplay.get_width()/2 - ship.get_width()/2
gameDisplay.blit(itemsbar,(768,0))
gameDisplay.blit(itemsbar,(768,491))
gameDisplay.blit(b_g_Img,(0,0))
step = True
def move(allstep,player,x,y,a,b): 
    stamin(820,346) 
    global a1,a2,b1,b2,P1_sword,P2_sword,alldeths,alldeths2,punch
    oldx = x
    oldy = y
    olda = a
    oldb = b
    # poop = False
    # right=False
    # left = False
    # up = False
    # down = False
    # while not poop:
    #     for event in pygame.event.get():
    #         ############################
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_LEFT:
    #                 left = True
    #                 poop = True
    #             elif event.key == pygame.K_RIGHT:
    #                 right = True
    #                 poop = True
    #             elif event.key == pygame.K_UP:
    #                 up = True
    #                 poop = True
    #             elif event.key == pygame.K_DOWN:
    #                 down = True
    #                 poop = True
    #         ############################
    # else:
    if right == True and a < 7:
        a = a+1
        # print('right true')
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
    if punch == True:
        if player == True:
            if abs(a - a2) <= 1 and abs(b - b2) <= 1 and P1_sword == True:
                P1_sword = False
                dark(740,631 - 70 * alldeths)
                alldeths = alldeths + 1
                whiteINV(774,565)               
                a1,b1,a2,b2 = spawn(0,1)
        if player == False:
            if abs(a - a1) <= 1 and abs(b - b1) <= 1 and P2_sword == True:
                P2_sword = False
                dark(740,140 - 70 * alldeths2)
                alldeths2 = alldeths2 + 1
                whiteINV(774,74)
                a1,b1,a2,b2 = spawn(1,0)
        punch = False
    for i in range (len(By)):
        if x==Bx[i] and y == By[i]:
            x = oldx
            y = oldy
            a = olda
            b = oldb
        # if allstep == 0:
        #     allstep = 3
        # print(allstep)
        dark(820,346) 
    return x,y,b,a
def pick_up(a1,b1,player):
    global P1_sword
    global P2_sword
    print(Sx,Sy)
    for i in range (len(Sx)):
        if a1 == Sx[i] and b1 == Sy[i]:
            del(Sx[i])
            del(Sy[i])
            if player == True:
                sword_inv(774,565)
                P1_sword = True
            else:
                P2_sword = True
                sword_inv (774,74)            
            break
def spawn(D1,D2):
    global a1,a2,b1,b2,P1_sword,P2_sword,alldeths,alldeths2
    if D1 == 1:    
        a1 = random.randint(0,1)   
        b1 = random.randint(0,7)    
        x = X_list[a1]    
        y = Y_list[b1]    
        hero(x,y)    
    if D2 == 1:    
        a2 = random.randint(6,7)   
        b2 = random.randint(0,7)    
        x2 = X_list[a2]    
        y2 = Y_list[b2]    
        hero2(x2,y2)    
    return a1,b1,a2,b2
clock = pygame.time.Clock()
gameS = True
crashed = False
if gameS == True:
    a1,b1,a2,b2 =spawn(1,1)
    x = X_list[a1]    
    y = Y_list[b1]
    x2 = X_list[a2]    
    y2 = Y_list[b2]
stamin(752,491)
health(740,0)
health(740,70)
health(740,140)
health(740,491)
health(740,561)
health(740,631)
while not crashed:
    global nowin
    # if allstep > 1:
    #     print(allstep)
    #     allstep = allstep - 1
    # # if allstep < 2:
  
        # Sx[allstep] = X_list[random.randint(2,5)]
        # Sy[allstep] = Y_list[random.randint(0,7)]
        # allstep = allstep - 1

    if allbox < 8:
        Bx[allbox] = X_list[random.randint(2,5)]
        By[allbox] = Y_list[random.randint(0,7)]
        allbox = allbox + 1
    step_done=False
    while step_done==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                step_done=True
                # print('crashed')
            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True
                    step_done=True
                elif event.key == pygame.K_RIGHT:
                    right = True
                    step_done=True
                    # print('right')
                elif event.key == pygame.K_UP:
                    step_done=True
                    up = True
                elif event.key == pygame.K_DOWN:
                    step_done=True
                    down = True
                elif event.key == pygame.K_SPACE:
                    step_done = True
                    punch = True
                ############################
    if step ==True:
        dark(752,491)
        stamin(752,0)
        stamin(752,110)
        if allsteps >= 1:
            dark(752,601)
        # a_temp=a1
        # while a_temp==a1:  
        x,y,b1,a1 = move(allstep,step,x,y,a1,b1)

        # print(a1, 'stepTrue')
        # print(x,y)      
        left = False
        right = False
        up = False
        down = False
        allsteps = allsteps + 1
        pick_up(x,y,step)
        if allsteps >= 2:
            step = False
        # print(a1,b1, ' a1 b1')
        # print(Sx, Sy, 'Sx Sy')
    else:
        dark(752,0) 
        stamin(752,491) 
        stamin(752,601)
        if allsteps <= 1:
            dark(752,110)
        x2,y2,b2,a2 = move(allstep,step,x2,y2,a2,b2)
        left = False
        right = False
        up = False
        down = False 
        allsteps = allsteps - 1
        pick_up(x2,y2,step)
        if allsteps <= 0:
            step = True
            steps_passed+=1  
    # print(a1,b1,a2,b2, 'steps')
    if len(Sx)<2:
        
        # print(allstep) 
        sword_position=random.randint(2,5)
        sword_position_y = random.randint(0,7)
        for k in range(len(Bx)):
            if sword_position * 90 !=Bx[k] and sword_position_y * 90 != By[k]:
                Sx.append(X_list[sword_position])        
                Sy.append(Y_list[sword_position_y])
                break
    gameDisplay.blit(b_g_Img,(0,0))
    print (Bx,By)
    print (Sx,Sy)
    if len(Sx)>0:
        for i in range(len(Sx)):
            sword(Sx[i],Sy[i])
    # allstep = 0
    for i in range (8):
        box(Bx[i],By[i])
    hero(a1 * 90,b1 * 90)
    hero2(a2 * 90,b2 * 90)
    # if HDead == True:
        # spawn(1,0)    
    # if H2Dead == True:
        # spawn(0,1)   
    if alldeths == 3 or alldeths2 == 3:
        nowin = False
        break
    pygame.display.update()
    clock.tick(60)
while not nowin:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nowin = True
    death(425,345)
    pygame.display.update()
    clock.tick(60)
pygame.quit()