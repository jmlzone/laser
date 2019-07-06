#!/usr/bin/python3
import svgwrite
from svgwrite.data.types import SVGAttribute
from svgwrite.extensions import Inkscape

dwg = svgwrite.Drawing('endStopBrackets.svg', profile='full', size=('155mm','50mm'), viewBox="0 0 155 50")
ink=Inkscape(dwg)


# switches 2mm more left
# increase outer radius by 5mm  MOved everthting down 5mm and left 5mm
def mySwitchBracket(dwg, ox,oy) :
    p=dwg.path( d="M%d,%d m0,10 a10,10 0 0,1 20,0 l15,0 l0,20 l-15,0 a10,10 0 0,1 -20,0 l0,-20" % (ox,oy),
    stroke="black", fill="none", stroke_width=0.1)
    dwg.add(p)
    c=dwg.circle(center=(ox+10,oy+10), r=2, stroke="black", fill="none", stroke_width=0.1)
    dwg.add(c)
    c=dwg.circle(center=(ox+10,oy+30), r=2, stroke="black", fill="none", stroke_width=0.1)
    dwg.add(c)
    c=dwg.add(dwg.circle(center=((ox+27),(oy+15)),r=0.75,stroke='black',fill="none", stroke_width=0.1))
    c=dwg.add(dwg.circle(center=((ox+27),(oy+25)),r=0.75,stroke='black',fill="none", stroke_width=0.1))
    return()

mySwitchBracket(dwg,5,5)
mySwitchBracket(dwg,42,5)
mySwitchBracket(dwg,79,5)
mySwitchBracket(dwg,116,5)

dwg.save(pretty=True)
