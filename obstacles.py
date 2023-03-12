class Obstacle:
    def __init__(self, x, y, endX, endY, thickness, colour):
        self.x = x
        self.y = y
        self.start = (self.x, self.y)
        self.endX = endX
        self.endY = endY
        self.end = (self.endX, self.endY)
        self.thickness = thickness
        self.colour = colour

    def draw(self, canvas):
        canvas.draw_line(self.start, (self.endX, self.endY), self.thickness, self.colour)
        
    def getStartX(self):
        return self.x

    def getEndX(self):
        return self.endX

    def getY(self):
        return self.y

    def collisions(self, character):
        #detects collisions between obstacles and character
        #could also be used for enemy if needed
        if self.x < character.pos.get_p()[0] < self.endX:
            if round(character.pos.get_p()[1]) + 35 < self.y < round(character.pos.get_p()[1]) + 50:
                return True
            #elif round(character.pos.get_p()[1]) < self.y < round(character.pos.get_p()[1]) + 15: #added the 15 bcs not always detecting collisions, program not running often enough
             #   return True
        return False
