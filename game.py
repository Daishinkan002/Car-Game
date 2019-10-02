from __future__ import division
import pygame,sys
import random
from pygame.locals import *
from time import sleep
from datetime import datetime
from os import path

img_dir = path.join(path.dirname(__file__),'images')
sound_dir = path.join(path.dirname(__file__),'sound')


pygame.init()
# DISPLAY SCREEEN
screen=game_display=pygame.display.set_mode((500,1000))
pygame.display.set_caption('Car Game')



#To Exit from the game
def exit():
	for event in pygame.event.get():
		print(event)
		if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			quit()

#To Move the car.
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
Blue = (0,0,255)
Green=(0, 128,0)
White=(255, 255, 255)

sound=pygame.mixer.music.load(path.join(sound_dir,'Nightcore-Monster_GJMenN-LqVg.mp3'))
pygame.mixer.music.play(-1,0.0)
a=random.randint(0,1910)
b=0

car = pygame.image.load (path.join(img_dir,'CAR.jpg'))
car = pygame.transform.scale(car, (90, 100))
villaincar=pygame.image.load(path.join(img_dir,'car.png'))
villaincar=pygame.transform.scale(villaincar,(90, 100))

carx=10
cary=910
start = datetime.now()
points=0
opening =0 
font_style = 'freesansbold.ttf'

def draw_text(surface,text,size,x,y):
	font=pygame.font.Font(font_style,size)
	text_surface=font.render(text,True,Black)
	text_box=text_surface.get_rect()
	text_box.midtop=(x,y)
	surface.blit(text_surface,text_box)

screen.fill(Blue)
while True:
	fontObj = pygame.font.Font('freesansbold.ttf',34)
	draw_text(screen,"Car-Game",50,250,200)
	event = pygame.event.poll()
	if event.type==pygame.KEYDOWN:
		if event.key == pygame.K_RETURN:
			opening=1
			break;
		elif event.key == pygame.K_q:
			pygame.quit()
			quit()
	elif event.type == pygame.QUIT:
		pygame.quit()
		quit()
	else:
		draw_text(screen,"Press [Enter] to continue ",30, 250,500)
		draw_text(screen,"Press [Q] to Quit",30,250,560)
		pygame.display.update()

speed = 0.015

while opening:
	screen.fill(Aqua)
	screen.blit(villaincar,(a,b))
	screen.blit(car,(carx,cary))
	(carx,cary)=move(carx,cary)

    #If the car hit the villain car
	if ((a>carx-70 and a<=carx+90) and  b==cary):
		screen.fill(Black)
		fontObj = pygame.font.Font('freesansbold.ttf',34)
		pointSurfaceObj=fontObj.render('Points = '+str(points) ,True,Green,Blue)
		pointRectObj = pointSurfaceObj.get_rect()
		pointRectObj.center=(200,500)
		screen.blit(pointSurfaceObj,pointRectObj)
		pygame.display.update()
		sleep(2)
		pygame.quit()
		quit()
	b+=10
	exit()
	sleep(speed)
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
	if(b>=1000):
		points+=1
		a=random.randint(0,350)
		b=0
		if(points%10==0):
			speed-=0.002
	update_points(points)
	pygame.display.update()
	(carx,cary)=move(carx,cary)
	exit()


