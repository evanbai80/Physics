import pygame
import sys
import math
import random
import pyautogui
pygame.init()
width=800
height=400
screen=pygame.display.set_mode((width,height))
#cue=pygame.Rect((50,216),(30,300))
#cueimage=pygame.Surface((30,300))
#cueimage.fill((255,255,255))
WHITE=((255,255,255))
mainballimage=pygame.Surface((32,32))
clock = pygame.time.Clock()


balls=[]
angle=0
friction=0.98
distance=0
def finddistance(objectx,objecty):
    distance=math.dist((objectx.x,objectx.y),(objecty.x,objecty.y))
    return distance
point=(0,0)
def findcollision(objectx,objecty):
    point=((objectx.x+objecty.x)/2,(objectx.y+objecty.y)/2)
    return point

class Ball:
    def __init__ (self,centerx,centery,color):
        self.x=centerx
        self.y=centery
        self.vx=0
        self.vy=0
        self.mass=20
        #self.x=random.randint(50,550)
        #self.y=random.randint(50,750)
        self.radius=10
        self.color=color

        ballsurface=pygame.Surface((32,32))
        #self.ball=pygame.draw.circle(ballsurface,WHITE,(self.x,self.y),self.radius)
    def draw(self,surface):
        pygame.draw.circle(surface,self.color,(int(self.x),int(self.y)),self.radius)
    
    def move(self):
        self.x+=self.vx
        self.y+=self.vy
        self.vx*=friction
        self.vy*=friction

        if self.x<=15 or self.x>=width-self.radius:
            self.vx*=-1
        if self.y<=15 or self.y>=height-self.radius:
            self.vy*=-1
balls=[Ball(400,200,(255,255,255)),Ball(500,200,(255,0,0)), Ball(520,190,(255,255,0)),Ball(520,210,(0,0,255))]
balls[0].vx=0
balls[0].vy=0
def collisions(balls):
    for i in range(len(balls)):
        for j in range(i+1,len(balls)):
            b1=balls[i]
            b2=balls[j]
            distance=math.hypot(b2.x-b1.x,b2.y-b1.y)
            if distance<=2*b1.radius:
                #print ("Collision")
                angle=math.atan2(b2.y-b1.y,b2.x-b1.x)
                vxsum=b1.vx-b2.vx
                vysum=b1.vy-b2.vy
                f=vxsum*math.cos(angle)+vysum*math.sin(angle)
                b1.vx-=f*math.cos(angle)
                b2.vx+=f*math.cos(angle)
                b1.vy-=f*math.sin(angle)
                b2.vy+=f*math.sin(angle)

                overlap=2*b1.radius-distance
                b1.x-=math.cos(angle)*overlap/2
                b1.y-=math.sin(angle)*overlap/2
                b2.x+=math.cos(angle)*overlap/2
                b2.y+=math.sin(angle)*overlap/2
shoot=False
while True:
    clock.tick(60)
    screen.fill((0,0,0))
    pos=pyautogui.position()
    #cue.center=pos
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                angle=angle+10
            elif event.key==pygame.K_DOWN:
                angle=angle-10
        elif event.type==pygame.MOUSEBUTTONDOWN:
                if balls[0].vx<=0.05:
                    shoot=True
                    mouse_start=pygame.mouse.get_pos()
        elif event.type==pygame.MOUSEBUTTONUP:
            if shoot==True:
                mouse_end=pygame.mouse.get_pos()
                dx= mouse_start[0]-mouse_end[0]
                dy=mouse_start[1]-mouse_end[1]
                balls[0].vx=dx/10
                balls[0].vy=dy/10
                shoot=False
                
    #for z in range (3):
        #if finddistance(balls[z],balls[
    if shoot==True:
        mouse_pos=pygame.mouse.get_pos()
        pygame.draw.line(screen,(200,200,200),(balls[0].x,balls[0].y),mouse_pos,2)
    for b in (balls):
        b.move()
        b.draw(screen) 
    
    
    #rotatecue=pygame.transform.rotate(cueimage,angle)
    #screen.blit(rotatecue,cue.topleft)
    
    collisions(balls)
    pygame.display.update()
            
