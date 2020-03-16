#!/usr/bin/python3
import svgwrite
import math
from svgwrite.data.types import SVGAttribute
from svgwrite.extensions import Inkscape
from libShapes import *

def pss40(dwg,cx,cy) :
    lx = 57.0
    ly = 101.5
    ox = (lx/2)
    oy = (ly/2)
    circleCl(dwg,(cx+ox),(cy+oy),3.5)
    circleCl(dwg,(cx+ox),(cy-oy),3.5)
    circleCl(dwg,(cx-ox),(cy+oy),3.5)
    circleCl(dwg,(cx-ox),(cy-oy),3.5)
    lx = 63.0
    ly = 108.0
    ox = cx - (lx/2)
    oy = cy - (ly/2)
    centeredBox(dwg, cx,cy, lx, ly)
    return()

def analogSupply(dwg,cx,cy) :
    lx = 76.0
    ly = 76.0
    ox = (lx/2)
    oy = (ly/2)
    circleCl(dwg,(cx+ox),(cy+oy),3.5)
    circleCl(dwg,(cx+ox),(cy-oy),3.5)
    circleCl(dwg,(cx-ox),(cy+oy),3.5)
    circleCl(dwg,(cx-ox),(cy-oy),3.5)
    lx = 84.0
    ly = 84.0
    ox = cx - (lx/2)
    oy = cy - (ly/2)
    centeredBox(dwg, cx,cy, lx, ly)
    return()

def xformer101864(dwg,cx,cy) :
    centeredBox(dwg, cx,cy, 28, 68)
    centeredBox(dwg, cx,cy, 28, 91)
    centeredBox(dwg, cx,cy, 55, 45)
    lx = 0
    ly = 78
    ox = (lx/2)
    oy = (ly/2)
    circleCl(dwg,(cx+ox),(cy+oy),3.5)
    circleCl(dwg,(cx-ox),(cy-oy),3.5)
    return()

if (__name__ == "__main__") :
    print("Running as PowerSupplyBox")
    dwg = svgwrite.Drawing('front.svg', profile='full', size=('300mm','155mm'), viewBox="0 0 300 155")
    ink=Inkscape(dwg)
    outlineBBox(dwg,5,5,232,96)
    #VA meter for analog supply
    centeredBox(dwg,50,25,46,27)
    #amp limit control
    circleCl(dwg,30,50,7.5)
    #Voltage Control
    circleCl(dwg,70,50,7.5)
    bindingPostPair(dwg,50,70)
    #jacks for analog power
    oblongHole(dwg,85,15,7.5,6.5)
    oblongHole(dwg,85,35,7.5,6.5)
    #VA meter for digital supply
    centeredBox(dwg,167,25,46,27)
    #voltage select switch
    circleCl(dwg,167,50,7.5)
    # +5 connections
    bindingPostPair(dwg,120,60)
    oblongHole(dwg,150,60,7.5,6.5)
    # +3.3 connections
    bindingPostPair(dwg,190,60)
    oblongHole(dwg,220,60,7.5,6.5)
    # -12 connections
    bindingPostPair(dwg,120,80)
    oblongHole(dwg,150,80,7.5,6.5)
    dwg.save(pretty=True)

    dwg = svgwrite.Drawing('back.svg', profile='full', size=('300mm','155mm'), viewBox="0 0 300 155")
    ink=Inkscape(dwg)
    outlineBBox(dwg,5,5,232,96)
    powerInletModule(dwg, 205, 70)
    oblongHole(dwg,145,20,7.5,6.5)
    oblongHole(dwg,85,20,7.5,6.5)
    oblongHole(dwg,25,20,7.5,6.5)
    dwg.save(pretty=True)

    dwg = svgwrite.Drawing('bottom.svg', profile='full', size=('300mm','170mm'), viewBox="0 0 300 170")
    ink=Inkscape(dwg)
    outlineBBox(dwg,5,5,232,160)
    pss40(dwg,(232 - (2 + (63/2))),(160-(8+(108/2))))
    analogSupply(dwg,(5+5+(84/2)),(160-(8+(84/2))))
    xformer101864(dwg,128,55)
    dwg.save(pretty=True)

    
