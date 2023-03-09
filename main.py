import time
from menu import Menu
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

def start(canvas):
    frame.set_canvas_background('Grey')
    mn = Menu(WIDTH, HEIGHT)
    mn.mainmenu(canvas)

def cont(canvas):
    frame.set_canvas_background('Grey')
    mn = Menu(WIDTH, HEIGHT)
    mn.pausemenu(canvas)


# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame(" War of The Worlds ", WIDTH, HEIGHT)
if startType == 0:
    frame.set_draw_handler(start)
else:
    frame.set_draw_handler(cont)
# Start the frame animation
frame.start()
