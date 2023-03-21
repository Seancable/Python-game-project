import random
from menuCont import MenuCont

try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 750
HEIGHT = 750

class Menu:

    def __init__(self, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT

    def mainmenu(self, canvas):
        canvas.draw_polygon([[self.width/2 - 300, self.height/2 - 250], [self.width/2 + 300, self.height/2 - 250],
        [self.width/2 + 300, self.height/2 +  250], [self.width/2 - 300, self.height/2 + 250]], 12, 'Black', 'ForestGreen')

        # New Game button
        canvas.draw_polygon([[self.width/4, self.height/4], [3/4*(self.width), self.height/4],
                             [3/4*(self.width), self.height/4 + 60], [self.width/4, self.height/4 + 60]], 12, 'Grey', 'Silver')
        canvas.draw_text('Start Game', [self.width/4 + 80, self.height/4 + 45], 45, 'Red')
        # Save Game button ** if time allows **
        #canvas.draw_polygon([[self.width/4, self.height/4 + 80], [3/4*(self.width), self.height/4 + 80],
                             #[3/4*(self.width), self.height/4 + 140], [self.width/4, self.height/4 + 140]], 12, 'Silver', 'Silver')
        #canvas.draw_text('Start Game', [self.width/4 + 30, self.height/4 + 45], 45, 'Red')
        # Settings Button
        canvas.draw_polygon([[self.width/4, self.height/4 + 160], [3/4*(self.width), self.height/4 + 160],
                             [3/4*(self.width), self.height/4 + 200], [self.width/4, self.height/4 + 200]], 12, 'Grey', 'Silver')
        canvas.draw_text('Settings', [self.width/4, self.height/4 + 180], 30, 'Red')
        # Quit Button
        canvas.draw_polygon([[self.width/4 + 50, self.height/4 + 260], [3/4*(self.width) - 50, self.height/4 + 260],
                             [3/4*(self.width) - 50, self.height/4 + 220], [self.width/4 + 50, self.height/4 + 220]], 12, 'Grey', 'Silver')
        canvas.draw_text('Quit', [self.width/4 + 100, self.height/4 + 250], 25, 'Red')

        menChoice = "start"

        return menChoice

    def pausemenu(self, canvas):
        canvas.draw_polygon([[self.width/2 - 200, self.height/2 - 150], [self.width/2 + 200, self.height/2 - 150],
        [self.width/2 + 200, self.height/2 +  150], [self.width/2 - 200, self.height/2 + 150]], 12, 'Black', 'ForestGreen')
        #canvas.draw_polygon([[],[],[],[], 5, 'Silver', 'Silver']) # Continue Button
        #canvas.draw_polygon([[],[],[],[], 5, 'Silver', 'Silver']) # Load Game Button ** If time allows**
        #canvas.draw_polygon([[],[],[],[], 5, 'Silver', 'Silver']) # Settings Button
        #canvas.draw_polygon([[],[],[],[], 5, 'Silver', 'Silver']) # Exit Button

def start(canvas):
    frame.set_canvas_background('Grey')
    mn = Menu(WIDTH, HEIGHT)
    choice = mn.mainmenu(canvas)

def cont(canvas):
    pass



startType = 0

frame = simplegui.create_frame(" The War of The Worlds ", WIDTH, HEIGHT)
if startType == 0:
    print("No one would have believed ... ")
    #playsound('Introduction.wav')
    frame.set_draw_handler(start)
else:
    frame.set_draw_handler(cont)

#frame.set_mouseclick_handler(click)
frame.start()
