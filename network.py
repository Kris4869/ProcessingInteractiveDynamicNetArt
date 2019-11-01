from node import Node
from random import *

class Network(object):
    
    def __init__(self):
        #self.nodesShape = createShape(GROUP)
        self.networkShape = createShape(GROUP)
        self.nodes = []
        
    def create(self, x, y):
        n = Node(x, y)
        self.nodes.append(n)
        #self.nodesShape.addChild(n.getShape())
        
    def update(self):
        for n in self.nodes:
            n.update()
            if n.life <= 0:
                self.nodes.remove(n)
                #remove from nodesShape
        self.networkShape = createShape(GROUP)
        for n in self.nodes:
            for m in self.nodes:
                if not (m is n):
                    x, y = n.getLoc()
                    a, b = m.getLoc()
                    col = sqrt(m.life * n.life) / Node.LIFE * 255 
                    link = createShape()
                    link.beginShape(LINES)
                    link.stroke(col, col, col)
                    link.vertex(x, y)
                    link.vertex(a, b)
                    link.endShape()
                    self.networkShape.addChild(link)
                    
    def display(self):
        shape(self.networkShape)
        #shape(self.nodesShape)
