running = True

maxEntities = 1000
entities = []

deltaTime = 0
getTicksLastFrame = 0

state = "menu"
player = None

def checkCollision(obja, objb):
    if (obja.pos[0]+obja.size[0] > objb.pos[0] and obja.pos[0] < objb.pos[0]+objb.size[0] and obja.pos[1]+obja.size[1] > objb.pos[1] and obja.pos[1] < objb.pos[1]+objb.size[1]):
        return True
    else:
        return False
    pass
