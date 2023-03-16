import random

try:
    import simplegui
except ImportError :
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Menu:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def mainmenu(self, canvas):
        canvas.draw_polygon([[self.width/2 - 200, self.height/2 - 150], [self.width/2 + 200, self.height/2 - 150],
        [self.width/2 + 200, self.height/2 +  150], [self.width/2 - 200, self.height/2 + 150]], 12, 'Black', 'ForestGreen')
        #canvas.draw_polygon([[],[],[],[], 5, 'Silver', 'Silver']) # Start Game Button
        #canvas.draw_polygon([[],[],[],[], 5, 'Silver', 'Silver']) # Load Game Button ** If time allows**
        #canvas.draw_polygon([[],[],[],[], 5, 'Silver', 'Silver']) # Settings Button
        #canvas.draw_polygon([[],[],[],[], 5, 'Silver', 'Silver']) # Exit Button

        menChoice = "start"

        return menChoice

    def pausemenu(self, canvas):
        canvas.draw_polygon([[self.width/2 - 200, self.height/2 - 150], [self.width/2 + 200, self.height/2 - 150],
        [self.width/2 + 200, self.height/2 +  150], [self.width/2 - 200, self.height/2 + 150]], 12, 'Black', 'ForestGreen')
        #canvas.draw_polygon([[],[],[],[], 5, 'Silver', 'Silver']) # Continue Button
        #canvas.draw_polygon([[],[],[],[], 5, 'Silver', 'Silver']) # Load Game Button ** If time allows**
        #canvas.draw_polygon([[],[],[],[], 5, 'Silver', 'Silver']) # Settings Button
        #canvas.draw_polygon([[],[],[],[], 5, 'Silver', 'Silver']) # Exit Button
