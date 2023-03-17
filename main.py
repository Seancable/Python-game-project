import time
from menu import Menu
from character import Character
from bullet import Bullet
from keyboard import Keyboard
from enemy import EnemyT1
from interaction import *
from obstacles import Obstacle
from healthpack import HealthPack
from vector import Vector

enemy1_a = simplegui.load_image('https://s3.us-east-2.amazonaws.com/ascensiongamedev/filehost/b28a06ac5850e6556ec12c44f65b3e14.png')
enemy1_b = simplegui.load_image('https://s3.us-east-2.amazonaws.com/ascensiongamedev/filehost/55942801df7a044914b713a281c53c7d.png')
enemy1_c = simplegui.load_image('https://s3.us-east-2.amazonaws.com/ascensiongamedev/filehost/16eeaa1a8b6b77bb7fbbd21284a820eb.png')
bck = simplegui.load_image('https://raw.githubusercontent.com/Seancable/Python-game-project/main/Level1_01.png')

class Main:
    def __init__(self, obs, character, background, clock, kbd, hp, inter, gun, bullet, enemyList, enemy, btime):
        self.obs = obs
        self.character = character
        self.background = background
        self.clock = clock
        self.kbd = kbd
        self.hp = hp
        self.inter = inter
        self.gun = False
        self.bullet = bullet
        self.enemyList = enemyList
        self.enemy = enemy
        self.btime = 0
        self.x = 0

    def runGame(self, canvas):
        self.clock.tick()
        self.inter.update()
        self.character.update()
        self.background.draw(canvas)
        self.character.draw(canvas)
        self.enemy.draw(canvas)
        self.bullet.draw(canvas)
        self.hp.draw(canvas)
        for obs in self.obs:
            obs.draw(canvas)
        self.btime+=1
        if self.clock.transistion(10)==True:
            self.character.next_frame()
        if self.kbd.fire and self.bullet.is_fired():
            self.bullet.pos=Vector(self.character.pos.get_p()[0], self.character.pos.get_p()[1])
            self.bullet.draw(canvas)
            self.gun=True
            self.btime=0
        if self.gun==True:
            self.bullet.update()
            if self.btime==50:
                self.gun=False
                self.bullet.pos=Vector(0,0)

kbd=Keyboard()
check = False
y1 = 350
y2 = 250
y3 = 150
y4 = 50
obs = [Obstacle(100, y1, 400, y1, 20, "Orange"),
        Obstacle(200, y2, 550, y2, 20, "Orange"),
        Obstacle(50, y3, 300, y3, 20, "Orange"),
        Obstacle(55, y4, 280, y4, 20, "red")]      
sheet=Character(Vector(WIDTH/2,HEIGHT-100), obs)
background = Background(bck, WIDTH, HEIGHT)
clock=Clock()
hp=HealthPack()
inter=Interaction(sheet,kbd,hp, obs)
gun=False
bullet=Bullet(sheet)
enemyList = [enemy1_a, enemy1_b, enemy1_c]
i = random.randint(0,2)
enemy=EnemyT1(enemyList[i], (Vector(450, 400)))
btime=0
main = Main(obs, sheet, background, clock, kbd, hp, inter, gun, bullet, enemyList, enemy, btime)

def draw(canvas):
    global main
    main.runGame(canvas)

frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()


                

