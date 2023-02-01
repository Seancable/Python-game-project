from vector import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 500
HEIGHT = 500
IMG = simplegui.load_image('http://www.cs.rhul.ac.uk/courses/CS1830/sprites/coach_wheel-512.png')
IMG_CENTRE = (256, 256)
IMG_DIMS = (512, 512)
IMG_DEST_DIM=(40,40)
STEP=0.5
                
class Wheel:
    def __init__(self, pos, radius):
        self.pos = pos
        self.vel = Vector()
        self.radius = (80,80)
        self.colour = 'White'
        self.img_rot = 0.5

    def draw(self, canvas):
        canvas.draw_image(IMG,IMG_CENTRE, IMG_DIMS, self.pos.get_p(), self.radius, self.img_rot)
        
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)
        if self.pos.get_p()[0]<0:
            self.pos.add(Vector(WIDTH,0))
        if self.pos.get_p()[0]>WIDTH:
            self.pos.subtract(Vector(WIDTH,0))
        if self.pos.get_p()[1]<HEIGHT-40:
            self.pos.add(Vector(0,1))
            val=int(self.pos.get_p()[1])
            val=float(val)
            if val==HEIGHT-40:
                self.pos.subtract(Vector(0,self.pos.get_p()[1]))
                self.pos.add(Vector(0,val))
                
    def on_ground(self):
        if self.pos.get_p()[1]==HEIGHT-40:
            return True
        else:
            return False
    

    
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up=False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['up']:
            self.up = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False

class Interaction:
    def __init__(self, wheel, keyboard):
        self.wheel = wheel
        self.keyboard = keyboard

    def update(self):
        if self.wheel.on_ground()==True:
            if self.keyboard.right:
                self.wheel.vel.add(Vector(1, 0))
                self.wheel.img_rot=self.wheel.img_rot+0.1

            if self.keyboard.left:
                self.wheel.vel.add(Vector(-1,0))
                self.wheel.img_rot=self.wheel.img_rot-0.1

            if self.keyboard.up:
                self.wheel.vel.add(Vector(0,-10))

kbd = Keyboard()
wheel = Wheel(Vector(WIDTH/2, HEIGHT-40), 40)
inter = Interaction(wheel, kbd)

def draw(canvas):
    inter.update()
    wheel.update()
    wheel.draw(canvas)

frame = simplegui.create_frame('Interactions', WIDTH, HEIGHT)
frame.set_canvas_background('#2C6A6A')
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)

frame.start()
