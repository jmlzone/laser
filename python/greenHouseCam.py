#!/usr/bin/python3
import svgwrite
from svgwrite.data.types import SVGAttribute
from svgwrite.extensions import Inkscape
import math

dwg = svgwrite.Drawing('greenHouseCam.svg', profile='full', size=('215mm','50mm'), viewBox="0 0 215 50")
ink=Inkscape(dwg)

def greenHouseCamBlank(dwg, ox,oy, camOD=35.0, camID=10.0, mhd=3.5,mho=5.5) :
    cx=ox+(camOD/2.0)
    cy=oy+(camOD/2.0)
    # inner cicle
    c=dwg.add(dwg.circle(center=(cx,cy), r=(camID/2.0), stroke="black", fill="none", stroke_width=0.1))
    # mounting holes
    c=dwg.add(dwg.circle(center=(cx+mho,cy+mho), r=(mhd/2.0), stroke="black", fill="none", stroke_width=0.1))
    c=dwg.add(dwg.circle(center=(cx+mho,cy-mho), r=(mhd/2.0), stroke="black", fill="none", stroke_width=0.1))
    c=dwg.add(dwg.circle(center=(cx-mho,cy+mho), r=(mhd/2.0), stroke="black", fill="none", stroke_width=0.1))
    c=dwg.add(dwg.circle(center=(cx-mho,cy-mho), r=(mhd/2.0), stroke="black", fill="none", stroke_width=0.1))
    # outer circle conver to path when cam shape is figured out
    c=dwg.add(dwg.circle(center=(cx,cy), r=(camOD/2.0), stroke="black", fill="none", stroke_width=0.1))
    #p=dwg.path( d="M%d,%d m0,10 a10,10 0 0,1 20,0 l15,0 l0,20 l-15,0 a10,10 0 0,1 -20,0 l0,-20" % (ox,oy),
    #stroke="black", fill="none", stroke_width=0.1)
    #dwg.add(p)
    return()

def greenHouseCamCalc(dwg, ox,oy, camOD=35.0, camID=10.0, mhd=3.5,mho=5.5,offDisp=13,onDisp=17.5,dwell=0.75,riseTime=0.5) :
    cx=ox+(camOD/2.0)
    cy=oy+(camOD/2.0)
    # inner cicle
    c=dwg.add(dwg.circle(center=(cx,cy), r=(camID/2.0), stroke="black", fill="none", stroke_width=0.1))
    # mounting holes
    c=dwg.add(dwg.circle(center=(cx+mho,cy+mho), r=(mhd/2.0), stroke="black", fill="none", stroke_width=0.1))
    c=dwg.add(dwg.circle(center=(cx+mho,cy-mho), r=(mhd/2.0), stroke="black", fill="none", stroke_width=0.1))
    c=dwg.add(dwg.circle(center=(cx-mho,cy+mho), r=(mhd/2.0), stroke="black", fill="none", stroke_width=0.1))
    c=dwg.add(dwg.circle(center=(cx-mho,cy-mho), r=(mhd/2.0), stroke="black", fill="none", stroke_width=0.1))
    # outer circle conver to path when cam shape is figured out
    # c=dwg.add(dwg.circle(center=(cx,cy), r=(camOD/2.0), stroke="black", fill="none", stroke_width=0.1))
    #p=dwg.path( d="M%d,%d m0,10 a10,10 0 0,1 20,0 l15,0 l0,20 l-15,0 a10,10 0 0,1 -20,0 l0,-20" % (ox,oy),
    #stroke="black", fill="none", stroke_width=0.1)
    #dwg.add(p)
    rpm=10
    degPerSec=360*rpm/60
    dwellAngle=dwell*degPerSec
    dlaf = (dwellAngle>180)
    riseAngle=riseTime*degPerSec
    riseRad = math.radians(riseAngle)
    remAngle = 360.0 - (dwellAngle + (2.0 * riseAngle))
    rlaf = (remAngle>180)
    if(rlaf<0) :
        print("error remining angle less than zero")
    print("remaining angle =%f" %remAngle)
    rise=onDisp-offDisp
    dwellRad = math.radians(dwellAngle/2.0)
    yOff=offDisp * math.sin(dwellRad)
    xOff=offDisp * math.cos(dwellRad)
    print("dwell agle = %f, %f, dlaf=%d" %(dwellAngle,dwellRad,dlaf))
    print("offset X,Y %f,%f" %(xOff, yOff))
    remRad = math.radians(remAngle/2.0)
    ryOff=onDisp * math.sin(remRad)
    rxOff=onDisp * math.cos(remRad)
    cpx = (xOff-rxOff)/2.0
    cpy = (yOff+ryOff)/2.0
    cpy = ryOff
    print("Control point %f,%f" % (cpx,cpy)) 
    # move to start
    pathText = "M%f,%f\n" % ((cx+xOff),(cy-yOff))
    #dwell off arc
    pathText = pathText+ "A%f,%f 0 %d 1 %f,%f\n" %(offDisp,offDisp,dlaf,(cx+xOff),(cy+yOff))
    # temp move to start of rem
    #pathText = pathText+ "L%f,%f\n" % ((cx-rxOff),(cy+ryOff))
    pathText = pathText+ "Q%f,%f %f,%f\n" % ((cx+cpx),(cy+cpy), (cx-rxOff),(cy+ryOff))
    #remain on arc
    pathText = pathText+ "A%f,%f 0 %d 1 %f,%f\n" %(onDisp,onDisp,rlaf,(cx-rxOff),(cy-ryOff))
    #final transition
    pathText = pathText+ "Q%f,%f %f,%f\n" % ((cx+cpx),(cy-cpy), (cx+xOff),(cy-yOff))

    #p=dwg.path(d="M%f,%f A%f,%f 0 %d 1 %f,%f"  %((cx+xOff),(cy-yOff),offDisp,offDisp,dlaf,(cx+xOff),(cy+yOff)),
    p=dwg.path(d="%s" %pathText,
    stroke="black", fill="none", stroke_width=0.1)
    dwg.add(p)
    return()

#greenHouseCamBlank(dwg,5,5)
#
#greenHouseCamCalc(dwg,5,5)
#greenHouseCamCalc(dwg,45,5)
greenHouseCamCalc(dwg,78,5)
greenHouseCamCalc(dwg,111,5)
greenHouseCamCalc(dwg,144,5)
greenHouseCamCalc(dwg,177,5)
dwg.save(pretty=True)
# -------------------> +X
# arc
# A rx ry x-axis-rotatation large-arc-flag sweep-flag x y
# rx, rx, radius
# large arc flag if greater than 180 degrees
# sweep flag move in positive or negative direction
# Quadratic
# Q cx,cy x,y
# cx, cy control point
# x, y endpoint
