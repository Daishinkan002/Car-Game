import pygame,sys
import random
from pygame.locals import *
from time import sleep
from datetime import datetime


pygame.init()

#SETTING DISPLAY SCREEEN

screen=game_display=pygame.display.set_mode((500,1000))
pygame.display.set_caption('First Game')




def exit():
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            quit()

def move(carx,cary):
    for event in pygame.event.get():
        if (event.type==KEYDOWN and event.key == K_RIGHT and carx<=340):
            carx+=90
        elif (event.type==KEYDOWN and event.key == K_LEFT and carx>=90):
            carx-=90
        else:
            return carx,cary
    return (carx,cary)

def update_points(points):
    fontObj = pygame.font.Font('freesansbold.ttf',64)
    textSurfaceObj = fontObj.render(str(points),True,Green,Blue)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center=(400,900)
    screen.blit(textSurfaceObj,textRectObj)
    pygame.display.update()





Aqua = (100,149,237)
Black=(0, 0,0)
Blue=(0,0, 255)
Green=(0, 128,0)
White=(255, 255, 255)

sound=pygame.mixer.music.load('Nightcore-Monster_GJMenN-LqVg.mp3')
pygame.mixer.music.play(-1,0.0)
a=random.randint(0,1910)
b=0

car = pygame.image.load ('CAR.jpg')
car = pygame.transform.scale(car, (90, 100))
villaincar=pygame.image.load('car.png')
villaincar = pygame.transform.scale(villaincar, (90, 100))

carx=10
cary=910
start = datetime.now()
points=0

while True:
    screen.fill(Aqua)
    screen.blit(villaincar,(a,b))
    screen.blit(car,(carx,cary))
    (carx,cary)=move(carx,cary)
    if ((a>carx-70 and a<=carx+90) and  b==cary):
        screen.fill(Black)
        fontObj = pygame.font.Font('freesansbold.ttf',34)
        pointSurfaceObj=fontObj.render('Points = '+str(points) ,True,Green,Blue)
        pointRectObj = pointSurfaceObj.get_rect()
        pointRectObj.center=(200,500)
        screen.blit(pointSurfaceObj,pointRectObj)
        pygame.display.update()
        sleep(1)
        pygame.quit()
        quit()
    b+=10
    exit()
    sleep(0.005)
    end=datetime.now()
    if((end-start).seconds==90):        
        screen.fill(Black)
        fontObj = pygame.font.Font('freesansbold.ttf',10)
        textSurfaceObj = fontObj.render('CONGRATULATIONS YOU WON !!!!',True,Green,Blue)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center=(200,500)
        screen.blit(textSurfaceObj,textRectObj)
        pygame.display.update()
        last_update_points(points)
        sleep(1)
        pygame.quit()
        quit()
        
    (carx,cary)=move(carx,cary)
    if(b>=1000 ):
        points+=1
        a=random.randint(0,350)
        b=0
    update_points(points)
    pygame.display.update()
    (carx,cary)=move(carx,cary)
    exit()
    
    
