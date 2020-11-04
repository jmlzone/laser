#!/usr/bin/python3
import svgwrite
from svgwrite.data.types import SVGAttribute
from svgwrite.extensions import Inkscape

from libShapes import *

dwg = svgwrite.Drawing('oledbezel.svg', profile='full', size=('150mm','115mm'), viewBox="0 0 150 115")
ink=Inkscape(dwg)

def myBox(dwg, ox,oy) :
    p=dwg.path( d="M%d,%d l200,0 l0,50 a50,50 0 0,1 -50,50 l-150,0 l0,-100" % (ox,oy),
    stroke="black",
    fill="none", stroke_width=0.1)
    return(p)

def outsideBox(dwg,ox,oy) :
    outlineBBox(dwg, ox,oy, 37,49)

def mountingHoles(dwg,ox,oy) :
    r=7
    d=6
    hole(dwg,ox+r,oy+d,2)
    r=37-7
    d=6
    hole(dwg,ox+r,oy+d,2)
    r=7
    d=49-6
    hole(dwg,ox+r,oy+d,2)
    r=37-7
    d=49-6
    hole(dwg,ox+r,oy+d,2)
    
def bezelBack(dwg,ox,oy) :
    outsideBox(dwg,ox,oy)
    r=(37.0-18.0)/2.0
    d=(49.0-32.0)-6.0
    outlineBBox(dwg, ox+r,oy+d, 18.0,6.0)
    r=(37.0-13.0)/2.0
    d=(49.0-32.0)
    outlineBBox(dwg, ox+r,oy+d, 13.0,6.0)
    mountingHoles(dwg,ox,oy)

def bezelMiddle(dwg,ox,oy) :
    outsideBox(dwg,ox,oy)
    r=(37.0-25.0)/2.0
    d=(49.0-32.0)-13.0
    outlineBBox(dwg, ox+r,oy+d, 25,13)
    r=(37.0-29.0)/2.0
    d=(49.0-32.0)
    outlineBBox(dwg, ox+r,oy+d, 29,28)

def bezelFront(dwg,ox,oy) :
    outsideBox(dwg,ox,oy)
    r=(37.0-27.0)/2.0
    d=(49.0-32.0)+5.0
    outlineBBox(dwg, ox+r,oy+d, 27,15)
    r=(37.0-0.0)/2.0
    d=(49.0-32.0)-8.0
    hole(dwg,ox+r,oy+d,3)
    r=(37.0/2.0) + 5.08
    hole(dwg,ox+r,oy+d,3)
    r=(37.0/2.0) - 5.08
    hole(dwg,ox+r,oy+d,3)
def bezelFront2(dwg,ox,oy) :
    outsideBox(dwg,ox,oy)
    r=(37.0-27.0)/2.0
    d=(49.0-32.0)+5.0
    outlineBBox(dwg, ox+r,oy+d, 27,15)
    r=(37.0-0.0)/2.0
    d=(49.0-32.0)-8.0
    hole(dwg,ox+r,oy+d,3.5)
    r=(37.0/2.0) + 5.08
    hole(dwg,ox+r,oy+d,3.5)
    r=(37.0/2.0) - 5.08
    hole(dwg,ox+r,oy+d,3.5)

bezelBack(dwg,5,60)
#bezelMiddle(dwg,5+40,60)
#bezelFront(dwg,5+40+40,60)
bezelBack(dwg,5,5)
bezelMiddle(dwg,5+40,5)
bezelFront2(dwg,5+40+40,5)

dwg.save(pretty=True)
