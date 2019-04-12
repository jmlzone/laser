#!/usr/bin/python3
import svgwrite
from svgwrite.data.types import SVGAttribute
from svgwrite.extensions import Inkscape

dwg = svgwrite.Drawing('svgwrite-example.svg', profile='full', size=('300mm','400mm'), viewBox="0 0 300 400")
ink=Inkscape(dwg)

def myBox(dwg, ox,oy) :
    p=dwg.path( d="M%d,%d l200,0 l0,50 a50,50 0 0,1 -50,50 l-150,0 l0,-100" % (ox,oy),
    stroke="black",
    fill="none", stroke_width=0.1)
    return(p)

def mySwitchBracket(dwg, ox,oy) :
    p=dwg.path( d="M%d,%d m0,5 a5,5 0 0,1 10,0 l10,0 l0,20 l-10,0 a5,6 0 0,1 -10,0 l0,-20" % (ox,oy),
    stroke="black",
    fill="none", stroke_width=0.1)
    dwg.add(p)
    c=dwg.circle(center=(ox+5,oy+5), r=2, stroke="black", fill="none", stroke_width=0.1)
    dwg.add(c)
    c=dwg.circle(center=(ox+5,oy+25), r=2, stroke="black", fill="none", stroke_width=0.1)
    dwg.add(c)

    return()

def ravFront(dwg, ox,oy) :
    p=dwg.path( d="M%d,%d l0,60 l100,0 l0,-45 a15,15 0 0,0 -15,-15 l-85,0" % (ox,oy),
    stroke="black", fill="none", stroke_width=0.1)
    dwg.add(p)
    return()

def ravBottom(dwg, ox,oy) :
    p=dwg.path( d="M%d,%d l0,62 l44,0 a25,20 0 0,0 25,-20 l3,-42 l-72,0" % (ox,oy),
    stroke="black", fill="none", stroke_width=0.1)
    dwg.add(p)
    return()

def ravTop(dwg, ox,oy) :
    p=dwg.path( d="M%d,%d l0,80 l75,0 a25,80 0 0,0 25,-80  l-100,0" % (ox,oy),
    stroke="black", fill="none", stroke_width=0.1)
    dwg.add(p)
    return()

def ravSide(dwg, ox,oy) :
    p=dwg.path( d="M%d,%d l8,76 l64,0 a16,47 0 0,1 -16,-47  l-56,-29" % (ox,oy),
    stroke="black", fill="none", stroke_width=0.1)
    dwg.add(p)
    return()

#extra_att={'sodipodi:namedview': SVGAttribute('sodipodi:namedview', anim=False, types=[], const=frozenset(['string'])) }
#dwg.validator.attributes.update(extra_att)
#svg_att=set(dwg.elements['svg'].valid_attributes)

#dwg.add(myBox(dwg,10,10))
#dwg.add(myBox(dwg,10,120))
ravTop(dwg,5,5)
ravSide(dwg,90,5)
ravFront(dwg,5,90)
ravBottom(dwg,115,88)

mySwitchBracket(dwg,220,10)

dwg.save(pretty=True)
