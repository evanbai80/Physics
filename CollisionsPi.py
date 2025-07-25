import pygame
import sys
import math
import random
pygame.init()
screen=pygame.display.set_mode((1400,800))
clock=pygame.time.Clock()

timeelapse=0

counter=0

class box:
    def __init__(self,mass,velocity):
        self.mass=mass
        self.velocity=velocity
        
    #def wallcollision(p):
     #   if self.R.cooliderect(p):
            
#b1=box(pygame.Rect((1000,600),(200,200)),1000,-10)
b1=pygame.Rect((1000,600),(200,200))
b2=pygame.Rect((600,600),(50,50))
s1=pygame.Surface((200,200))
s1.fill((255,255,255))
s2=pygame.Surface((50,50))
s2.fill((255,255,255))
m1=100
m2=1
v1=-10
v2=0
#b2=box(pygame.Rect

while False:
    v2=-v2
    counter=counter+1
    print(counter,v1,v2)
    if v1 > v2:
        break
    store=v1
    v1=((m1-m2)*v1+2*m2*v2)/(m1+m2)
    v2=(2*m1*store+(m2-m1)*v2)/(m1+m2)
    counter=counter+1
    print(counter,v1,v2)
    

while True:
    clock.tick(60)
    screen.fill((0,0,0))
    timeelapse=timeelapse+0.001
    tim=1
    if b1.colliderect(b2) or b2.colliderect(b1):
        store=v1
        v1=((m1-m2)*v1+2*m2*v2)/(m1+m2)
        v2=(2*m1*store+(m2-m1)*v2)/(m1+m2)
        counter=counter+1
        print(counter,v1,v2)
        tim=timeelapse
        timeelapse=0
    if b2.x<=25:
        v2=v2*-1
        counter=counter+1
        tim=timeelapse
        print(counter,v1,v2)
    b1.move_ip(v1*tim,0)
    b2.move_ip(v2*tim,0)
    screen.blit(s1,b1)
    screen.blit(s2,b2)

    pygame.display.update()
