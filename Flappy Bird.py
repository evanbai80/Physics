import pygame
import sys
import math
import random
pygame.init()
screen=pygame.display.set_mode((288,512))
player=pygame.Rect((50,216),(32,32))
playerimage=pygame.Surface((32,32))

toppipe_y=random.randint(0,300)
bottompipe_y=362-toppipe_y
toppipe=pygame.Rect((288,0),(130,toppipe_y))
bottompipe=pygame.Rect((288,512-bottompipe_y),(130,bottompipe_y))
topimage=pygame.Surface((40,toppipe_y))
bottomimage=pygame.Surface((40,bottompipe_y))
bottomimage.fill((255,255,255))
topimage.fill((255,255,255))


clock=pygame.time.Clock()
bird=pygame.image.load('bird.png')
bird=pygame.transform.scale(bird,(32,32))
g=9.8
dt=0.1
v=0
while True:
    clock.tick(10)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                v=-15
    toppipe.move_ip(-5,0)
    bottompipe.move_ip(-5,0)
    if toppipe.x<-50:
        toppipe_y=random.randint(0,300)
        bottompipe_y=362-toppipe_y
        toppipe=pygame.Rect((288,0),(130,toppipe_y))
        bottompipe=pygame.Rect((288,512-bottompipe_y),(130,bottompipe_y))
        topimage=pygame.Surface((40,toppipe_y))
        bottomimage=pygame.Surface((40,bottompipe_y))
        bottomimage.fill((255,255,255))
        topimage.fill((255,255,255))
    if player.colliderect(toppipe) or player.colliderect(bottompipe):
        print("GAME OVER!")
        quit()
    v=v+g*dt
    player.move_ip(0,v)
    print(v)

    screen.blit(topimage,toppipe)
    screen.blit(bottomimage,bottompipe)
    screen.blit(bird,player.topleft)
    pygame.display.update()
