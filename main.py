import time
#from menu import Menu
from character import Character
from bullet import Bullet
from keyboard import Keyboard
from enemy import EnemyT1
from interaction import *
from obstacles import Obstacle
from healthpack import HealthPack
from vector import Vector
from menu import Menu

enemy1_a = simplegui.load_image('https://s3.us-east-2.amazonaws.com/ascensiongamedev/filehost/b28a06ac5850e6556ec12c44f65b3e14.png')
enemy1_b = simplegui.load_image('https://s3.us-east-2.amazonaws.com/ascensiongamedev/filehost/55942801df7a044914b713a281c53c7d.png')
enemy1_c = simplegui.load_image('https://s3.us-east-2.amazonaws.com/ascensiongamedev/filehost/16eeaa1a8b6b77bb7fbbd21284a820eb.png')
bck = simplegui.load_image('https://raw.githubusercontent.com/Seancable/Python-game-project/main/Level1_01.png')


class Main:
    def __init__(self, obs, character, background, clock, kbd, hp, inter, gun, bullet, enemyList, btime):
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
        self.btime = 0
        self.x = 0

    def runGame(self, canvas):
        global gun,btime,invtime,enemy_counter
        clock.tick()
        inter.update()
        sheet.update()
        background.draw(canvas)
        sheet.draw(canvas)
        for enemy in enemies:
            enemy.obstacle()
            hit=enemy.attack(sheet)
            # this tracks if the player hits the enemy and if they are dead
            #or the player is invincible
            if hit==True:
                if sheet.inv==False:
                    sheet.hit()
            if enemy.life==False:
                enemy_counter+=1
                enemy.life=True
            enemy.draw(canvas)
        bullet.draw(canvas)
        hp.draw(canvas)
        if enemy_counter==len(enemies):
            print("all enemies arte dead")
        for obstacle in self.obs:
            obstacle.draw(canvas)
        btime+=1
        if clock.transistion(10)==True:
            for enemy in enemies:
                enemy.next_frame()
            sheet.next_frame()
        if sheet.inv==True:
            invtime+=1
            if invtime%50==0:
                sheet.inv=False
        # this checks to see if the bullet is fready to be fired and will allow
        #the bullets position to chnge to interact with the enviroment
        if kbd.fire and bullet.is_fired():
            bullet.pos=Vector(sheet.pos.get_p()[0],sheet.pos.get_p()[1])
            bullet.draw(canvas)
            gun=True
            btime=0

        if gun==True:
            bullet.update()
            for enemy in enemies:
                if enemy.hit(bullet, sheet) == True:
                    gun = False
                    bullet.pos = Vector(0,0)
            if bullet.pos.x > WIDTH or bullet.pos.x<0:
                gun=False
                bullet.pos=Vector(0,0)

def firstLevel():
    obs = [Obstacle(100, 600, 400, 600, 20, "Orange",),
        Obstacle(500, 500, 650, 500, 50, "Orange"),
        Obstacle(300, 400, 600, 400, 20, "Orange"),
        Obstacle(50, 375, 300, 375, 50, "Orange"),
        Obstacle(55, 200, 280, 200, 20, "Orange")]
    return obs

sheet=Character(Vector(WIDTH/2,HEIGHT-100), firstLevel())
background = Background(bck, WIDTH, HEIGHT)
clock=Clock()
kbd=Keyboard()
hp=HealthPack(Vector(100,600))
gun=False
bullet=Bullet(sheet)
enemyt1list = [enemy1_a, enemy1_b, enemy1_c]
y1 = 350
y2 = 250
y3 = 150
y4 = 50
enemies=[(EnemyT1(enemyt1list[random.randint(0,2)], Vector(400, y1 - 45), 100, 400)), (EnemyT1(enemyt1list[random.randint(0,2)], Vector(550, y2 - 50), 200, 550)), (EnemyT1(enemyt1list[random.randint(0,2)], Vector(300, y3 - 50), 50, 300))]
btime=0
invtime=0
inter=Interaction(sheet,kbd,hp, firstLevel(), enemies, bullet)
enemy_counter=0
main = Main(firstLevel(), sheet, background, clock, kbd, hp, inter, gun, bullet, enemies, btime)

def draw(canvas):
    main.runGame(canvas)

def playGame():
    frame.set_draw_handler(draw)
    frame.set_keydown_handler(kbd.keyDown)
    frame.set_keyup_handler(kbd.keyUp)

def start(canvas):
    frame.set_canvas_background('Grey')
    mn = Menu(WIDTH, HEIGHT)
    choice = mn.mainmenu(canvas)

def click(pos):
    # Start Game
    print(pos)
    x = pos[0]
    y = pos[1]

    if (195 < x < 555) and (197 < y < 240):
        print("Start Game")
        playGame()
    if (195 < x < 555) and (355 < y < 385):
        print("Settings")
        quit()
    if (245 < x < 505) and (415 < y < 440):
        print("Quit")
        quit()

frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_draw_handler(start)
frame.set_mouseclick_handler(click)
frame.start()
