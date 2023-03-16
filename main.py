import time
from menu import Menu
from character import Character
from bullet import Bullet
from keyboard import Keyboard
from enemy import EnemyT1
from interaction import *
from obstacle import Obstacle
from healthpack import HealthPack
from vector import Vector

try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Main:

    def __init__(self):
        pass

    def begin(t):
        print("Game start at", time.ctime(t))
        return 0

WIDTH = 500
HEIGHT = 500


ma = Main
tm = time.time()
startType = ma.begin(tm)

global gun,btime, kbd
y1 = 350
y2 = 250
y3 = 150
y4 = 50
obs = [Obstacle(100, y1, 400, y1, 20, "Orange"),
       Obstacle(200, y2, 550, y2, 20, "Orange"),
       Obstacle(50, y3, 150, y3, 20, "Orange"),
       Obstacle(280, y4, 55, y4, 20, "red")]
sheet=Character(Vector(WIDTH/2,HEIGHT-100), obs)
background = Background(bck, WIDTH, HEIGHT)
clock=Clock()
kbd=Keyboard()
hp=HealthPack()
inter=Interaction(sheet,kbd,hp, obs)
bullet=Bullet(sheet)
enemyt1list = [enemy1_a, enemy1_b, enemy1_c]
i = random.randint(0,2)
enemyt1=EnemyT1(enemyt1list[i], (Vector(450, 400)))



def draw(canvas):
    btime=0
    gun=False
    background.draw(canvas)
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

def start(canvas):
    frame.set_canvas_background('Grey')
    mn = Menu(WIDTH, HEIGHT)
    choice = mn.mainmenu(canvas)

    if choice == "start":
        print("No one would have believed ... ")

        draw(canvas)

    else:
        draw(canvas)


def cont(canvas):
    frame.set_canvas_background('Grey')
    mn = Menu(WIDTH, HEIGHT)
    mn.pausemenu(canvas)


# Create a frame and assign the callback to the event handler
kbd=Keyboard()
frame = simplegui.create_frame(" The War of The Worlds ", WIDTH, HEIGHT)
if startType == 0:

    frame.set_draw_handler(start)
else:
    frame.set_draw_handler(cont)

frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
# Start the frame animation
frame.start()
