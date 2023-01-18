import random
try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

def randCol ():
    r = random.randrange (0, 256)
    g = random.randrange (0, 256)
    b = random.randrange (0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

# Constants are written in capital letters
WIDTH = 600
HEIGHT = 400
size = 0.01
colour = randCol()

# Handler to draw on canvas :
# this function is called 60 times per second
def draw(canvas):
    global size, colour
    if size < WIDTH/2:
        size += 1
    else:
        frame.set_canvas_background(colour)
        colour = randCol()
        size = 0.01

    canvas.draw_circle([WIDTH /2, HEIGHT /2], size, size*2 , colour)
    
    

# Create a frame and assign the callback to the event handler
frame = simplegui.create_frame("Points", WIDTH , HEIGHT )
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
