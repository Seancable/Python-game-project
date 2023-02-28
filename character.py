from vector import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH=500
HEIGHT=500
IMAGE=simplegui.load_image('https://opengameart.org/sites/default/files/hero_spritesheet_0.png')
IMAGE2=simplegui.load_image('hero_spritesheet_walking.png')

class Character:
    def __init__(self,pos):
        self.row=5
        self.col=8
        self.pos=pos
        self.vel=Vector(0,0)
        self.width=IMAGE.get_width()
        self.height=IMAGE.get_height()
        self.rows=(self.height/self.row)/2
        self.cols=(self.width/self.row)/2
        self.health=10
        self.length=(WIDTH/20)*self.health
        
    def draw(self,canvas):
        canvas.draw_image(IMAGE, (self.cols, self.rows), (IMAGE.get_width()/self.col, IMAGE.get_height()/self.row), self.pos.get_p(), (100,100))
        canvas.draw_line((0,0),(self.length,0),30,'Red')
    def next_frame(self):
        self.cols+=IMAGE.get_width()/self.col
        if self.cols>=self.width:
            self.cols=(IMAGE.get_width()/self.col)/2
            #self.rows+=self.height/self.row
            #if self.rows>=self.height:
                #self.rows=(self.height/self.row)/2
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)
        if self.pos.get_p()[0]<0:
            self.pos.add(Vector(WIDTH,0))
        if self.pos.get_p()[0]>WIDTH:
            self.pos.subtract(Vector(WIDTH,0))
        if self.pos.get_p()[1]<HEIGHT-100:
            self.pos.add(Vector(0,5))
            val=int(self.pos.get_p()[1])
            val=float(val)
            if val==HEIGHT-100:
                self.pos.subtract(Vector(0,self.pos.get_p()[1]))
                self.pos.add(Vector(0,val))

    def on_ground(self):
        if round(self.pos.get_p()[1],-1)==HEIGHT-100:
            return True
        else:
            return False
                
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
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up=False
        self.fire=False

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        #if key == simplegui.KEY_MAP['space']:
         #   self.up = True
        if key == simplegui.KEY_MAP['F']:
            self.fire =  True
            
 
    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['space']:
            self.up = True
        if key == simplegui.KEY_MAP['F']:
            self.fire = True
            

class Interaction:
    def __init__(self, sheet, keyboard):
        self.sheet = sheet
        self.keyboard = keyboard

    def update(self):
        if self.keyboard.right:
            self.sheet.vel.add(Vector(1, 0))
            self.sheet.rows=(self.sheet.height/self.sheet.row/2)*3
            self.sheet.width=(IMAGE.get_width()/self.sheet.col)*6

        if self.keyboard.left:
            self.sheet.vel.add(Vector(-1,0))
            self.sheet.rows=(self.sheet.height/self.sheet.row/2)*3
            self.sheet.width=(IMAGE.get_width()/self.sheet.col)*6
        if self.keyboard.up:
            if self.sheet.on_ground()==True:
                self.sheet.width=(IMAGE.get_width()/self.sheet.col)*3
                if self.sheet.cols>=self.sheet.width:
                    self.sheet.cols=(IMAGE.get_width()/self.sheet.col)/2
                self.sheet.vel.add(Vector(0,-10))
                self.sheet.rows=(self.sheet.height/self.sheet.row/2)*7
                self.sheet.width=(IMAGE.get_width()/self.sheet.col)*3
            else:
                self.keyboard.up = False

        if not (self.keyboard.right or self.keyboard.left or self.keyboard.up):
            self.sheet.rows=(self.sheet.height/self.sheet.row)/2
            self.sheet.width=IMAGE.get_width()
                               
sheet=Character(Vector(WIDTH/2,HEIGHT-100)) 
clock=Clock()
kbd=Keyboard()
inter=Interaction(sheet,kbd)
def draw(canvas):
    sheet.draw(canvas)
    clock.tick()
    inter.update()
    sheet.update()
    if clock.transistion(10)==True:
        sheet.next_frame()
frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()
