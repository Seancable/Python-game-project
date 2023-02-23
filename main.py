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


ma = Main
tm = time.time()
ma.begin(tm)

def draw(canvas):
    frame.set_canvas_background('Silver')


# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame(" War of The Worlds ", 1628 , 900)
frame.set_draw_handler(draw)
# Start the frame animation
frame.start()
