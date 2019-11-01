from random import *

class Node(object):
    
    LIFE = 800
    
    def __init__(self, x, y):
        self.velocity = PVector()
        self.x = x
        self.y = y
        self.life = Node.LIFE
        self.node = createShape()
        self.node.beginShape(POINTS)
        self.node.vertex(x, y)
        self.node.stroke(255)
        self.node.endShape()
        
    def getShape(self):
        return self.node
    
    def getLoc(self):
        return self.x, self.y
    
    def update(self):
        F = 0.0002
        vx = - (self.x * F) ** 2 + ((width - self.x) * F) ** 2 + uniform(-1, 1)/10
        vy = - (self.y * F) ** 2 + ((height - self.y) * F) ** 2 + uniform(-1, 1)/10
        self.velocity.add(PVector(vx, vy))
        self.node.translate(self.velocity.x, self.velocity.y)
        self.x += self.velocity.x
        self.y += self.velocity.y
        self.life -= 1
