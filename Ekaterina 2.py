#ставили снег, убирали снег, спрашивали пользователя
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
mc = minecraft.Minecraft.create()

LENGTH = 40
SNOW = 78
COUNT = int(input('Сколько кубиков снега ставить?'))

def drow_flat():
    for x in range(LENGTH):
        for z in range(LENGTH):
            mc.setBlock(x,0,z,block.GRASS)

def drow_snow(count):
   for c in range(count):
       rx = random.randint(0,LENGTH-1)
       rz = random.randint(0,LENGTH-1)
       mc.setBlock(rx,0,rz,block.SNOW)

def cleanup():
    for x in range(LENGTH):
        for z in range(LENGTH):
            b = mc.getBlock(x,0,z)
            if b == SNOW:
                mc.setBlock(x,0,z,block.GOLD_BLOCK)
            else:
                mc.setBlock(x,0,z,block.DIAMOND_BLOCK)

mc.postToChat(' ')   
drow_flat()
drow_snow(COUNT)
cleanup()
mc.postToChat('Done')