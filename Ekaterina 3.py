import mcpi.minecraft as minecraft
import mcpi.block as block
import random
mc = minecraft.Minecraft.create()

def drow_flat_gorizontal(x,y,z,lx,lz,bt=block.GRASS):
    for xc in range(lx):
        for zc in range(lz):
            mc.setBlock(x + xc,y,z + zc,bt)
            
def drow_flat_vertikal(x,y,z,lx,ly,bt=block.GRASS):
    for xc in range(lx):
        for yc in range(ly):
            mc.setBlock(x + xc,y + yc,z,bt)
            
def drow_flat_vertikal2(x,y,z,ly,lz,bt=block.GRASS):
    for zc in range(lz):
        for yc in range(ly):
            mc.setBlock(x,y + yc,z + zc,bt)

def drow_kr_l(x,y,z,lx):
    for zc in range(20):
        for xc in range(lx):
        mc.setBlock(x+xc,y+xc,30,block.BEDROCK) 
    
drow_flat_gorizontal(10,10,10,20,20,block.DIAMOND_BLOCK)
drow_flat_vertikal(10,10,10,20,20,block.DIAMOND_BLOCK)
drow_flat_vertikal(10,10,30,20,20,block.DIAMOND_BLOCK)
drow_flat_vertikal2(10,10,10,20,20,block.DIAMOND_BLOCK)
drow_flat_vertikal2(30,10,10,20,20,block.DIAMOND_BLOCK)
drow_kr_l(10,30,10,10)