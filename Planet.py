
import pygame
import sys
import math
import time
pygame.init()
screen = pygame.display.set_mode((1600, 1000))

wario=pygame.image.load('png-clipart-wario-land-super-mario-land-3-luigi-mario-wario-wario-world-mario-heroes-hand-thumbnail.png')
wario=pygame.transform.scale(wario,(30,30) )
class Planet:
    def __init__(self,name,mass,velocity,position,a):
        self.name=name
        self.mass=mass
        self.velocity=velocity
        self.position=position
        self.a=a

        
WHITE=(255,255,255)
objects=[]
Earth=Planet("Earth",50000,(0,0),(800,470),[0.0,0.0])
mars=Planet("Mars",100,(15,6),(400,350),[0.0,0.0])
Venus=Planet("Venus",450,(-30,0),(1400,650),[0.0,0.0])
objects.append(Earth)
objects.append(mars)
objects.append(Venus)
e=pygame.Rect(800,470,30,30)
m=pygame.Rect(400,350,15,15)
v=pygame.Rect(1400,650,25,25)
rects=[]
rects.append(e)
rects.append(m)
rects.append(v)
E=pygame.Surface((30,30))
M=pygame.Surface((15,15))
V=pygame.Surface((25,25))
E.fill(WHITE)
M.fill(WHITE)
V.fill(WHITE)
distances=[]
for i in range (3):
    distances.append([1,1,1])

def distance(pos1,pos2):
    d=math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)
    return d
g=10
tc=0.01
while True:
    originalpos=v.center
    #time.sleep(0.1)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #d1=distance(Earth.x,Earth.y,mars.x,mars.y)
    #d2=distance(Earth.x,Earth.y,Venus.x,Venus.y)
    #d3=distance(Venus.x,Venus.y,mars.x,mars.y)
    for i in range(3):
        objects[i].a=[0,0]
        for j in range(3):
            if i!=j:
                dx=(objects[j].position[0]-objects[i].position[0])
                dy=(objects[j].position[1]-objects[i].position[1])
                distances[i][j] = distance(objects[i].position, objects[j].position)
                #print(i,j,distances[i][j])
                objects[i].a[0]+=g*((objects[j].mass)*dx/(distances[i][j]*distances[i][j]))
                objects[i].a[1]+=g*(objects[j].mass)*dy/(distances[i][j]*distances[i][j])
            elif i==j:
                pass
        objects[i].velocity=((objects[i].velocity[0]+(tc*objects[i].a[0]))),(objects[i].velocity[1]+(tc*objects[i].a[1]))
        objects[i].position=(objects[i].position[0]+tc*objects[i].velocity[0],objects[i].position[1]+tc*objects[i].velocity[1])
        rects[i].topleft=(objects[i].position)
    pygame.draw.line(screen,(255,255,255),(originalpos),v.center)
    screen.fill((0,0,0))
    screen.blit(E,e)
    screen.blit(M,m)
    screen.blit(V,v)
    E.blit(wario,e.topleft)
    #print (e.topleft)
    pygame.display.update()
