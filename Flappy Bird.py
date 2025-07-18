import pygame
import sys
import math
import random
pygame.init()
screen=pygame.display.set_mode((288,512))
player=pygame.Rect((50,216),(32,32))
playerimage=pygame.Surface((32,32))

tlist=[]
blist=[]
for i in range(2):
    pipe_x=random.randint(300,400)
    toppipe_y=random.randint(0,300)
    bottompipe_y=362-toppipe_y
    toppipe=pygame.Rect((pipe_x,0),(40,toppipe_y))
    bottompipe=pygame.Rect((pipe_x,512-bottompipe_y),(40,bottompipe_y))
    tlist.append(toppipe)
    blist.append(bottompipe)
    print (tlist[i])
    print (blist[i])

topimage=pygame.Surface((40,toppipe_y))
bottomimage=pygame.Surface((40,bottompipe_y))
bottomimage.fill((255,255,255))
topimage.fill((255,255,255))

slist=[]
for q in range (6):
    slist.append(topimage)

clock=pygame.time.Clock()
bird=pygame.image.load('bird.png')
bird=pygame.transform.scale(bird,(32,32))
g=9.8
dt=0.1
v=0
s=[0,0]
t=[0,0]
while True:
    clock.tick(15)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                v=-15
    #toppipe.move_ip(-5,0)
    #bottompipe.move_ip(-5,0)
    for toppipe in tlist:
        if toppipe.x<-50:
            tlist.remove(toppipe)
            o=random.randint(1,10)
            if o<=5:            
                
                pipe_x=random.randint(288,400)
                s[i]=pipe_x
                toppipe_y=random.randint(0,300)
                t[i]=toppipe_y
                toppipe=pygame.Rect((pipe_x,0),(40,toppipe_y))
                tlist.append(toppipe)
                topimage=pygame.Surface((40,toppipe_y))
                topimage.fill((255,255,255))
        toppipe.move_ip(-5,0)
    for toppipe in tlist:
        screen.blit(topimage,toppipe)
                
                
                #bottomimage=pygame.Surface((40,bottompipe_y))
                #bottomimage.fill((255,255,255))
                
    for bottompipe in blist:
        if bottompipe.x<-50:
            blist.remove(bottompipe)
            z=random.randint(1,10)
            if z<=5:
                
                print (s[i])
                bottompipe_y=362-toppipe_y
                bottompipe=pygame.Rect((s[i],512-t[i]),(40,t[i]))
                blist.append(bottompipe)
                bottomimage=pygame.Surface((40,bottompipe_y))
                bottomimage.fill((255,255,255))
        bottompipe.move_ip(-5,0)
    if player.colliderect(toppipe) or player.colliderect(bottompipe):
        print("GAME OVER!")
        quit()
    v=v+g*dt
    player.move_ip(0,v)
    #print(v)

    for bottompipe in blist:
        screen.blit(bottomimage,bottompipe)
    
    screen.blit(bird,player.topleft)
    pygame.display.update()
