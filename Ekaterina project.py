#проект
import mcpi.minecraft as minecraft
import mcpi.block as block
from minecraftstuff import MinecraftDrawing
from time import sleep
from random import randint
from mcpi.minecraft import Vec3
mc = minecraft.Minecraft.create()
mcDrawing = MinecraftDrawing(mc)

def drow_flat(startx, startz, m):
    for x in range(50):
        for z in range(50):
            mc.setBlock(x + startx,0,z + startz, m)
            
def drow_portal(portalx, portaly, portalz):
    t = [Vec3(23 + portalx, 0 + portaly, 25 + portalz),
         Vec3(27 + portalx, 0 + portaly, 25 + portalz),
         Vec3(27 + portalx, 5 + portaly, 25 + portalz),
         Vec3(23 + portalx, 5 + portaly, 25 + portalz)]
    mcDrawing.drawFace(t, False, block.OBSIDIAN)
    
def drow_floor(fx, fz):
    for x in range(5):
        for z in range(1):
            mc.setBlock(x + fx,1,z + fz,block.DIAMOND_BLOCK)
    
def player():
    return mc.player.getTilePos()
          
drow_flat(0,0, block.GOLD_BLOCK)
drow_flat(100,100, block.GOLD_ORE)
drow_portal(0,1,0)
drow_portal(100,1,100)
drow_floor(23,24)
drow_floor(123,124)
while True:
    p = player()
    if p.x >= 23 and p.x <= 26:
        if p.z == 25:
            mc.player.setPos(p.x + 100, p.y, 127)
    if p.x >= 123 and p.x <= 126:
        if p.z == 125:
            mc.player.setPos(p.x - 100, p.y, 27)
            p.x = p.x - 100
            p.z = 25