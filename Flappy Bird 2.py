import pygame
import sys
import math
import random
pygame.init()
screen=pygame.display.set_mode((288,512))
player=pygame.Rect((50,216),(32,32))
playerimage=pygame.Surface((32,32))





class Pipe:
    def __init__(self):
        #self.topleft=topleft
        #self.height=height
        self.pipegap=150
        self.top_height=random.randint(0,300)
        self.bottom_height=512-self.top_height-130
        self.x=random.randint(288,500)
        self.toppipe=pygame.Rect((self.x,0),(40,self.top_height))
        self.bottompipe=pygame.Rect((self.x,512-self.bottom_height),(40,self.bottom_height))

        self.topimage=pygame.Surface((40,self.top_height))
        self.bottomimage=pygame.Surface((40,self.bottom_height))
        self.topimage.fill((255,255,255))
        self.bottomimage.fill((255,255,255))
    def scrollthing(self):
        self.toppipe.move_ip(-5,0)
        self.bottompipe.move_ip(-5,0)
    def blit(self,screen):
        screen.blit(self.topimage,self.toppipe)
        screen.blit(self.bottomimage,self.bottompipe)
    def collisiondetect(self,player):
        if player.colliderect(self.toppipe) or player.colliderect(self.bottompipe):
            return True
        #print("GAME OVER")
            
        
pipes=[]
                                 

slist=[]


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
    #toppipe.move_ip(-5
    if len(pipes)<2:
        
        if len(pipes)==0:
            pipes.append(Pipe())
            #print(pipes)
        else:
            #print(pipes[0].x)
            if pipes[0].toppipe.x<=220:
                pipes.append(Pipe())
    print(len(pipes))    
    for p in pipes:
        p.scrollthing()
        p.blit(screen)
        if p.collisiondetect(player):
            print("GAME OVER")
            pygame.quit()
            sys.exit()
        if p.toppipe.x<-50:
            pipes.remove(p)

    v=v+g*dt
    player.move_ip(0,v)
    screen.blit(bird,player.topleft)
    pygame.display.update()
