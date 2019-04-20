#рисовали линии, длиные
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

LENGTH = 128

def drow_x():
    for x in range(LENGTH):
        mc.setBlock(x,0,0,block.WOOL)

def drow_y():
    for y in range(LENGTH):
        mc.setBlock(0,y,0,block.DIAMOND_BLOCK)

def drow_z():
    for z in range(LENGTH):
        mc.setBlock(0,0,z,block.GOLD_BLOCK)

def drow_axis():
    drow_x()
    drow_y()
    drow_z()

drow_axis()