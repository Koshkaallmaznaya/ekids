#рисовали сферы, линии, круги с помощью библиотек
import mcpi.minecraft as minecraft
import mcpi.block as block
from mcpi.minecraft import Vec3
from minecraftstuff import MinecraftDrawing

mc = minecraft.Minecraft.create()
mcDrawing = MinecraftDrawing(mc)

def simple():
    mcDrawing.drawLine(-9, -10, -10, 10, 10, 9, block.DIAMOND_BLOCK)
    mcDrawing.drawLine(-10, -10, -10, 10, 10, 10, block.DIAMOND_BLOCK)
    mcDrawing.drawLine(-11, -10, -10, 10, 10, 11, block.DIAMOND_BLOCK)
    mcDrawing.drawLine(-10, -9, -10, 10, 10, 9, block.DIAMOND_BLOCK)
    mcDrawing.drawLine(-10, -10, -10, 10, 10, 10, block.DIAMOND_BLOCK)
    mcDrawing.drawLine(-10, -11, -10, 10, 10, 11, block.DIAMOND_BLOCK)
    mcDrawing.drawSphere(10, 10, 10, 10, block.DIAMOND_BLOCK)
    mcDrawing.drawSphere(-10, -10, -10, 10, block.DIAMOND_BLOCK)
    
def T():
    t = [Vec3(-10, -10, 0),
         Vec3(-10, 10, 0),
         Vec3(10, 0, 0)]
    mcDrawing.drawFace(t, False, block.DIAMOND_BLOCK)

class Tri():
    def __init__(self):
        self.t = [Vec3(-10, -10, 0),
                  Vec3(-10, 10, 0),
                  Vec3(10, 0, 0)]
    def show(self):
        for v in self.t:
            mc.setBlock(v.x, v.y, v.z, block.BEDROCK)
    def draw (self):
        mcDrawing.drawFace(self.t, True, block.DIAMOND_BLOCK)
    def scale(self, scale):
        for v in self.t:
            v.x = v.x * scale
            v.y = v.y * scale
            v.z = v.z * scale
    def move(self, x, y, z):
        for v in self.t:
            v.x = -v.x
            v.y = v.y + y
            v.z = v.z + z
        
t = Tri()
t.scale(15)
t.draw()
        
        
               