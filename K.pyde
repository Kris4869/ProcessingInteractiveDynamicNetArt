# @Kris Chen
# 10.29.2019

from network import Network
    
flag = 0    

def setup():
    print("Loading...")
    global system
    size(800, 600, P2D)
    background(0)
    system = Network()
    print("Loaded")

def mouseReleased():
    global flag
    flag = 0

def draw():
    global flag
    background(0)
    if mousePressed and flag == 0:
        x, y = mouseX, mouseY
        system.create(x, y)
        flag = 1
    system.update()
    system.display()
    
    #print(frameRate)
