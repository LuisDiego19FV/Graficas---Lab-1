#SR3.py
#Por Luis Diego Fernandez
#v-1.20.20objMaker

import sys
import math
import struct
import bmp_maker

# image attributes
width = 800
height = 800
x_to_paint = 1
y_to_paint = 1
bits_per_pixel = 32

print("BMP image maker V-2.21.19\n")

# image settings
newBmpImage = bmp_maker.bmpImage()
newBmpImage.glCreateWindow(width, height)
newBmpImage.glViewPort(x_to_paint,y_to_paint,200,200)
newBmpImage.glClearColor(0.2,0.2,0.5)
newBmpImage.glClear()

# pollies
pol1 = [[165,380],[185,360],[180,330],[207,345],[233,330],[230,360],[250,380],[220,385],[205,410],[193,383]]
pol2 = [[321,335],[288,286],[339,251],[374,302]]
pol3 = [[377,249],[411,197],[436,249]]
pol4 = [[413, 177], [448, 159], [502, 88], [553, 53], [535, 36], [676, 37], [660, 52], [750, 145], [761, 179], [672, 192], [659, 214], [615, 214], [632, 230], [580, 230], [597, 215], [552, 214], [517, 144], [466, 180]]
pol5 = [[682, 175], [708, 120], [735, 148], [739, 170]]

# paint them
newBmpImage.glColor(0.5,1,0.5)
newBmpImage.glPolyFiller(pol1)
newBmpImage.glPolyFiller(pol2)
newBmpImage.glPolyFiller(pol3)
newBmpImage.glColor(0.3,1,0.3)
newBmpImage.glPolyFiller(pol4)
newBmpImage.glColor(0.2,0.2,0.5)
newBmpImage.glPolyFiller(pol5)

# finnish
newBmpImage.glFinish()

print("Done")
