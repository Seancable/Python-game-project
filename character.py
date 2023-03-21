from vector import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH=750
HEIGHT=750
IMAGE=simplegui.load_image('https://opengameart.org/sites/default/files/hero_spritesheet_0.png')
IMAGE2=simplegui.load_image('hero_spritesheet_walking.png')

class Character:
    def __init__(self,pos, obs):
        self.row=5
        self.col=8
        self.pos=pos
        self.vel=Vector(0,0)
        self.width=IMAGE.get_width()
        self.height=IMAGE.get_height()
        self.rows=(self.height/self.row)/2
        self.cols=(self.width/self.col)/2
        self.health=10
        self.length=(WIDTH/20)*self.health
        self.obstacle = obs
        self.inv=False
        self.height = 500

    def setHeight(self, newHeight):
        self.height = newHeight
        
    def draw(self,canvas):
        canvas.draw_image(IMAGE, (self.cols, self.rows), (IMAGE.get_width()/self.col, IMAGE.get_height()/self.row), self.pos.get_p(), (100,100))
        canvas.draw_line((0,0),(self.length,0),20,'Red')
        
    def next_frame(self):
        self.cols+=IMAGE.get_width()/self.col
        if self.cols>=self.width:
            self.cols=(IMAGE.get_width()/self.col)/2
            #self.rows+=self.height/self.row
            #if self.rows>=self.height:
                #self.rows=(self.height/self.row)/2
    def update(self):
        temp = self.vel
        #if self.obstacle.collisions(self) and self.pos.get_p()[1] < self.obstacle.getY():
        #    self.vel = Vector(0, 1)
        #else:
        #    self.vel = temp
        self.pos.add(self.vel)
        self.length=(WIDTH/20)*self.health
        self.vel.multiply(0.85)
        if self.pos.get_p()[0]<0:
            self.pos.add(Vector(WIDTH,0))
        if self.pos.get_p()[0]>WIDTH:
            self.pos.subtract(Vector(WIDTH,0))
        if self.pos.get_p()[1]<HEIGHT-100:
            flip = False
            for obstacles in self.obstacle:
                if obstacles.collisions(self): #only makes character move downwards if not colliding with an obstacle
                    flip = True
            if not flip:
                self.pos.add(Vector(0,5))
            val=int(self.pos.get_p()[1])
            val=float(val)
            if val==HEIGHT-100:
                self.pos.subtract(Vector(0,self.pos.get_p()[1]))
                self.pos.add(Vector(0,val))
    def hit(self):
        self.health-=2.5
        self.inv = True
    def on_ground(self):
        #allows character to jump when on the defined ground
        if round(self.pos.get_p()[1],-1)==HEIGHT-100:
            return True
        for obstacles in self.obstacle:
            if obstacles.collisions(self):
                return True
        return False
