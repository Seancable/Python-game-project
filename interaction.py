from vector import Vector
from character import *
from healthpack import HealthPack
from keyboard import Keyboard
from bullet import Bullet
from obstacles import Obstacle
from enemy import EnemyT1
import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


enemy1_a = simplegui.load_image('https://s3.us-east-2.amazonaws.com/ascensiongamedev/filehost/b28a06ac5850e6556ec12c44f65b3e14.png')
enemy1_b = simplegui.load_image('https://s3.us-east-2.amazonaws.com/ascensiongamedev/filehost/55942801df7a044914b713a281c53c7d.png')
enemy1_c = simplegui.load_image('https://s3.us-east-2.amazonaws.com/ascensiongamedev/filehost/16eeaa1a8b6b77bb7fbbd21284a820eb.png')

    
class Clock:
    def __init__(self):
        self.time=0
    def tick(self):
        self.time+=1
    def transistion(self,frame_duration):
        if self.time % frame_duration==0:
            return True
        else:
            return False

class Interaction:
    def __init__(self, sheet, keyboard,hp, obstacle):
        self.sheet = sheet
        self.keyboard = keyboard
        self.hp=hp
        self.obstacle = obstacle
    def update(self):
        if self.keyboard.right:
            self.keyRight()

        if self.keyboard.left:
            self.keyLeft()
            
        if self.keyboard.up:
            self.keyUp()


        if not (self.keyboard.right or self.keyboard.left or self.keyboard.up):
            self.sheet.rows=(self.sheet.height/self.sheet.row)/2
            self.sheet.width=IMAGE.get_width()
        if self.sheet.pos.get_p()[0]<=self.hp.pos.get_p()[0]+50 or self.sheet.pos.get_p()[0]<=self.hp.pos.get_p()[0]-50:
            if self.hp.used==False and self.sheet.health!=10:
                self.sheet.health+=2.5
                self.hp.used=True
                print(self.sheet.health)
        #print(self.sheet.pos.get_p(), self.obstacle.getStart())

        
    def keyRight(self):
        self.sheet.vel.add(Vector(1, 0))
        self.sheet.rows=(self.sheet.height/self.sheet.row/2)*3
        self.sheet.width=(IMAGE.get_width()/self.sheet.col)*6

    def keyLeft(self):
        self.sheet.vel.add(Vector(-1,0))
        self.sheet.rows=(self.sheet.height/self.sheet.row/2)*3
        self.sheet.width=(IMAGE.get_width()/self.sheet.col)*6
        
    def keyUp(self):
        if self.sheet.on_ground():
            self.sheet.width=(IMAGE.get_width()/self.sheet.col)*3
        if self.sheet.cols>=self.sheet.width:
            self.sheet.cols=(IMAGE.get_width()/self.sheet.col)/2
            self.sheet.vel.add(Vector(0,-40))
            self.sheet.rows=(self.sheet.height/self.sheet.row/2)*7
        else:
            self.keyboard.up = False

    def keyDown(self):
        pass
y1 = 350
y2 = 250
y3 = 150
y4 = 50
obs = [Obstacle(100, y1, 400, y1, 20, "Orange"),
       Obstacle(200, y2, 550, y2, 20, "Orange"),
       Obstacle(50, y3, 150, y3, 20, "Orange"),
       Obstacle(280, y4, 55, y4, 20, "red")]      
sheet=Character(Vector(WIDTH/2,HEIGHT-100), obs) 
clock=Clock()
kbd=Keyboard()
hp=HealthPack()
inter=Interaction(sheet,kbd,hp, obs)
gun=False
bullet=Bullet(sheet)
enemyt1list = [enemy1_a, enemy1_b, enemy1_c]
i = random.randint(0,2)
enemyt1=EnemyT1(enemyt1list[i], (Vector(450, 400)))
btime=0     
def draw(canvas):
    global gun,btime
    sheet.draw(canvas)
    clock.tick()
    inter.update()
    sheet.update()
    enemyt1.draw(canvas)
    bullet.draw(canvas)
    hp.draw(canvas)
    for obstacle in obs:
        obstacle.draw(canvas)
    btime+=1
    if clock.transistion(10)==True:
        sheet.next_frame()
    if kbd.fire and bullet.is_fired():
        bullet.pos=Vector(sheet.pos.get_p()[0],sheet.pos.get_p()[1])
        bullet.draw(canvas)
        gun=True
        btime=0
    if gun==True:
        bullet.update()
        if btime==50:
            gun=False
            bullet.pos=Vector(0,0)
        
        
frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
