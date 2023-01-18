import random
try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Constants are written in capital letters
WIDTH = 600
HEIGHT = 400
counter = 0

def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

# Handler to draw on canvas :
# this function is called 60 times per second
def draw(canvas):
    global counter, colour, colourOne, colourTwo
    if counter == 60:
        colourOne, colourTwo = randCol(), randCol()
        counter = 0
    else:
        counter += 1
    canvas.draw_circle([WIDTH - 60, HEIGHT /2], 40, 20 , colourOne)
    canvas.draw_circle([WIDTH - 60, HEIGHT /2], 40, 10 , colourTwo)

# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame("Points", WIDTH , HEIGHT )
frame.set_draw_handler(draw)

# Start the frame animation
colourOne = randCol()
colourTwo = randCol()
frame.start()
