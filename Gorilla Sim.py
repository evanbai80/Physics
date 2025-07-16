import pygame
import sys
import math
pygame.init()
screen = pygame.display.set_mode((1600,1000))
player=pygame.Rect((0,500),(32,32))
playerimage=pygame.Surface((32,32))

monkey=pygame.image.load('monkey.png')
bananana=pygame.image.load('banana.png')
monkey=pygame.transform.scale(monkey,(100,100))
bananana=pygame.transform.scale(bananana,(40,20))

w=0
angle=0

banana=None
bananaimage=pygame.Surface((3,8))
bananaimage.fill((255,255,0))
g=2
playerimage.fill((255,255,255))

c=0
v=0

while True:
    screen.fill((0,0,0))
    #print(vx,vy)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                player.move_ip(0,-20)
            elif event.key==pygame.K_s:
                player.move_ip(0,20)
            elif event.key==pygame.K_a:
                player.move_ip(-20,0)
            elif event.key==pygame.K_d:
                player.move_ip(20,0)
            elif event.key==pygame.K_UP:
                angle=angle+10
            elif event.key==pygame.K_DOWN:
                angle=angle-10
            elif event.key==pygame.K_SPACE:
                v=0
                radian=angle*3.14/180

                #print(angle)
                vx=20*math.cos(radian)
                vy=-20*math.sin(radian)

                banana=pygame.Rect((player.x,player.y),(8,3))
    if banana!=None:
        if banana.x>1600 or banana.y>1000:
            banana=None
            c=0
        else:
            vx-=w
            vy+=g*0.5
            banana.move_ip(vx,vy)
            screen.blit(bananana,banana.topleft)
            c=c+1
    #print (c)
    randomthing=pygame.transform.rotate(monkey,angle)
    screen.blit(randomthing,player.topleft)
    pygame.display.update()
    
    
