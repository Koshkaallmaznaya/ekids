#рисовали динамиты, взрывали, получали ответ о действиях игрока
import mcpi.minecraft as minecraft
import mcpi.block as block
from minecraftstuff import MinecraftDrawing
from time import sleep
from random import randint
from mcpi.minecraft import Vec3
mc = minecraft.Minecraft.create()
mcDrawing = MinecraftDrawing(mc)

class Tnt():
    def __init__(self, x, z):
        self.x = x
        self.z = z
        self.y = mc.getHeight(x, z) + 1
        mc.setBlock(self.x, self.y, self.z, block.TNT)
    
    def boom(self):
        mcDrawing.drawSphere(self.x, self.y, self.z, 5, block.AIR)
        
    def pos(self):
        return Vec3(self.x, self. y, self.z)
        
def prepare(size):
    mc.setBlocks(-size, -5, -size, size, 0, size, block.DIAMOND_ORE)
    
prepare(10)
    
COUNT = 50
tnts = []
for t in range(COUNT):
    tnts.append(Tnt(randint(-10, 10), randint(-10, 10)))

while True:
    ev = mc.events.pollBlockHits()
    if ev:
        hit = ev[0]
        for t in tnts:
            if hit.pos == t.pos():
                t.boom()
