import time
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
bck2 = simplegui.load_image('https://raw.githubusercontent.com/Seancable/Python-game-project/main/Level1_02.png')
#bck3 = simplegui.load_image()


class Main:
    def __init__(self, obs, character, background, clock, kbd, hp, inter, gun, bullet, enemyList):
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
        self.enemy_counter = 0
        self.btime = 0
        self.invtime=0
        self.x = 0
        self.level = 1

    def runGame(self, canvas):
        global gun,btime,invtime,enemy_counter
        self.clock.tick()
        self.inter.update()
        self.character.update()
        self.background.draw(canvas)
        self.character.draw(canvas)

        for enemy in self.enemyList:
            enemy.obstacle()
            hit=enemy.attack(sheet)
            # this tracks if the player hits the enemy and if they are dead
            #or the player is invincible
            if hit==True:
                if self.character.inv==False: #player is no longer invincible
                    self.character.hit()
            if enemy.life==False:
                self.enemy_counter+=1
                enemy.life=True
            enemy.draw(canvas)

        self.bullet.draw(canvas)
        self.hp.draw(canvas)
        if self.enemy_counter==len(self.enemyList):
            #print("All enemies are dead")
            #print("Complete level " + str(self.level) + "!")
            self.level += 1
            self.obs = []
            mn = Menu(WIDTH, HEIGHT)
            mn.contmenu(canvas)
            print("all enemies are dead")
            self.enemy_counter=0
            if check==1:
                self.background=secondLevel()[2]
                self.obs=secondLevel()[0]
                self.enemyList=secondLevel()[1]
                self.character=Character(Vector(WIDTH/2,HEIGHT-100), secondLevel()[0])
                self.inter=Interaction(self.character,self.kbd,self.hp, secondLevel()[0],secondLevel()[1],self.bullet)
                check+=1
            else:
                self.background=thirdLevel()[2]
                self.obs=thirdLevel()[0]
                self.enemyList=thirdLevel()[1]
                self.character=Character(Vector(WIDTH/2,HEIGHT-100), thirdLevel()[0])
                self.inter=Interaction(self.character,self.kbd,self.hp, thirdLevel()[0],thirdLevel()[1],self.bullet)
     
        if self.character.health==0:
            print("you are dead")
            self.menu.mainmenu(canvas)
        for obstacle in self.obs:
            obstacle.draw(canvas)
        self.btime+=1
        if self.clock.transistion(10)==True:
            for enemy in self.enemyList:
                enemy.next_frame()
            sheet.next_frame()
        if self.character.inv==True:
            self.invtime+=1
            if self.invtime%50==0:
                self.character.inv=False
        # this checks to see if the bullet is fready to be fired and will allow
        #the bullets position to chnge to interact with the enviroment
        if self.kbd.fire and self.bullet.is_fired():
            self.bullet.pos=Vector(self.character.pos.get_p()[0],self.character.pos.get_p()[1])
            self.bullet.draw(canvas)
            self.gun=True
            self.btime=0

        if self.gun==True:
            self.bullet.update()
            for enemy in self.enemyList:
                if enemy.hit(self.bullet, self.character) == True:
                    self.gun = False
                    self.bullet.pos = Vector(0,0)
            if self.bullet.pos.x > WIDTH or self.bullet.pos.x<0:
                self.gun=False
                self.bullet.pos=Vector(0,0)

def firstLevel():
    background = Background(bck, WIDTH, HEIGHT)
    enemyt1list = [enemy1_a, enemy1_b, enemy1_c]
    enemies = [EnemyT1(enemyt1list[random.randint(0,2)], Vector(600, 500 - 95), 400, 525),
               EnemyT1(enemyt1list[random.randint(0,2)], Vector(280, 100 - 60), 400, 750),
               EnemyT1(enemyt1list[random.randint(0,2)], Vector(400, 600 - 60), 200, 400)]
    obs = [Obstacle(200, 600, 400, 600, 20, "Orange",),
        Obstacle(400, 450, 550, 450, 20, "Orange"),
        Obstacle(400, 100, 750, 100, 20, "Orange"),
        Obstacle(50, 375, 300, 375, 20, "Orange"),
        Obstacle(55, 200, 280, 200, 20, "Orange")]
    return obs, enemies, background

def secondLevel():
    background = Background(bck2, WIDTH, HEIGHT)
    enemyt1list = [enemy1_a, enemy1_b, enemy1_c]
    enemies = [EnemyT1(enemyt1list[random.randint(0,2)], Vector(random.randint(400,690), 83 - 52), 400, 690),
                EnemyT1(enemyt1list[random.randint(0,2)], Vector(random.randint(0,204), 204 - 60), 0, 204),
                EnemyT1(enemyt1list[random.randint(0,2)], Vector(690, 550 - 60), 400, 690),
                EnemyT1(enemyt1list[random.randint(0,2)], Vector(WIDTH/2, HEIGHT - 115), 133, 340),
                EnemyT1(enemyt1list[random.randint(0,2)], Vector(WIDTH/2, 425 - 60), 133, WIDTH/2 - 70)]
    obs = [Obstacle(400, 550, 690, 550, 20, "Orange"),
           Obstacle(133, 425, 340, 425, 20, "Orange"),
           Obstacle(240, 300, 340, 300, 20, "Orange"),
           Obstacle(0, 204, 230, 204, 20, "Orange"),
           Obstacle(400, 83, 690, 83, 20, "Orange")]
    return obs, enemies, background
def thirdLevel():
    background = Background(bck,WIDTH,HEIGHT)
    enemyt1list = [enemy1_a, enemy1_b, enemy1_c]
    enemies = [EnemyT1(enemyt1list[random.randint(0,2)], Vector(600, 500 - 95), 400, 525),
               EnemyT1(enemyt1list[random.randint(0,2)], Vector(280, 100 - 60), 400, 750),
               EnemyT1(enemyt1list[random.randint(0,2)], Vector(400, 600 - 60), 200, 400)]
    obs = [Obstacle(400, 550, 690, 550, 20, "Orange",),
           Obstacle(133, 425, 250, 425, 20, "Orange",),
           Obstacle(270, 390, 320, 390, 20, "Orange",),
           Obstacle(624, 204, 750, 204, 20, "Orange",),
           Obstacle(400, 83, 690, 83, 20, "Orange",)]
    return obs, enemies, background   

check = 1
if check == 1:
    clock=Clock()
    kbd=Keyboard()
    hp=HealthPack(Vector(100,600))
    gun=False
    btime=0
    invtime=0
    enemy_counter=0
    sheet=Character(Vector(WIDTH/2,HEIGHT-100), firstLevel()[0])
    bullet=Bullet(sheet)
    inter=Interaction(sheet,kbd,hp, firstLevel()[0],firstLevel()[1],bullet)
    main = Main(firstLevel()[0], sheet, firstLevel()[2], clock, kbd, hp, inter, gun, bullet, firstLevel()[1])
elif check == 2:
    clock=Clock()
    kbd=Keyboard()
    hp=HealthPack(Vector(100,600))
    gun=False
    btime=0
    invtime=0
    enemy_counter=0
    sheet=Character(Vector(WIDTH/2,HEIGHT-100), secondLevel()[0])
    bullet=Bullet(sheet)
    inter=Interaction(sheet,kbd,hp, secondLevel()[0],secondLevel()[1],bullet)
    main = Main(secondLevel()[0], sheet, secondLevel()[2], clock, kbd, hp, inter, gun, bullet, secondLevel()[1])

def draw(canvas):
    main.runGame(canvas)

def start(canvas):
    frame.set_canvas_background('Grey')
    mn = Menu(WIDTH, HEIGHT)
    choice = mn.mainmenu(canvas)

def pause(canvas):
    mn = Menu(WIDTH, HEIGHT)
    choice = mn.pausemenu(canvas)

# Indicates that the user is viewing the controls
def controls():
    mn = Menu(WIDTH, HEIGHT)
    mn.controlsMenu(canvas)

# Method to recognise a mouse click by the user
def click(pos):
    global frame
    #print(pos)
    x = pos[0]
    y = pos[1]

    if (195 < x < 555) and (197 < y < 240):
        # If the mouse is clicked within these parameters,
        # the game begins by setting a draw_handler and
        # initialising the keyboard
        frame.set_draw_handler(draw)
        frame.set_keydown_handler(kbd.keyDown)
        frame.set_keyup_handler(kbd.keyUp)
    if (195 < x < 555) and (355 < y < 385):
        # If the mouse is clicked within these parameters,
        # a 'controls' menu will appear

        frame.set_draw_handler(controls)
    if (245 < x < 505) and (415 < y < 440):
        # If the mouse is clicked within these parameters,
        # the player will exit the game

        quit()
    if (707 < x < 745) and (5 < y < 45):
        # If the mouse is clicked within these parameters,
        # the game is paused and the game state saved
        # (i.e. enemies and player will remain in the
        # same positions)

        frame.set_draw_handler(pause)
    if (195 < x < 555) and (245 < y < 290):
        # If the mouse is clicked within these parameters,
        # the level check increments by 1 and the next
        # level is displayed
        frame.set_draw_handler(draw)
        
        
# Creating the frame for the game - Used as a default over all of the classes involved
frame = simplegui.create_frame(' The War of The Worlds ', WIDTH, HEIGHT)
# Begins the game by initialising the start() method (calling the Menu class)
frame.set_draw_handler(start)
# Initialises the handler for when the player clicks the mouse
frame.set_mouseclick_handler(click)
# Begin the frame animation
frame.start()
