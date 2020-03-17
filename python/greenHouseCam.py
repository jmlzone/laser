#!/usr/bin/python3
import svgwrite
from svgwrite.data.types import SVGAttribute
from svgwrite.extensions import Inkscape
import math

dwg = svgwrite.Drawing('bushing.svg', profile='full', size=('100mm','50mm'), viewBox="0 0 100 50")
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
    #print("remaining angle =%f" %remAngle)
    rise=onDisp-offDisp
    dwellRad = math.radians(dwellAngle/2.0)
    yOff=offDisp * math.sin(dwellRad)
    xOff=offDisp * math.cos(dwellRad)
    #print("dwell agle = %f, %f, dlaf=%d" %(dwellAngle,dwellRad,dlaf))
    #print("offset X,Y %f,%f" %(xOff, yOff))
    remRad = math.radians(remAngle/2.0)
    ryOff=onDisp * math.sin(remRad)
    rxOff=onDisp * math.cos(remRad)
    cpx = (xOff-rxOff)/2.0
    cpy = (yOff+ryOff)/2.0
    cpy = ryOff
    #print("Control point %f,%f" % (cpx,cpy)) 
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

def greenHouseSpacer(dwg, ox,oy, spacerOD=26.0, camID=10.0, mhd=3.5,mho=5.5,notch=4) :
    cx=ox+(spacerOD/2.0)
    cy=oy+(spacerOD/2.0)
    nw=notch/2.0
    r1=camID/2.0
    r2=spacerOD/2.0
    th1=math.asin(nw/r1)
    th2=math.asin(nw/r2)
    x1=math.cos(th1) * r1
    x2=math.cos(th2) * r2
    #print("R1=%f x1=%f" %(r1, x1))
    #print("R2=%f x2=%f" %(r2, x2))
    # inner cicle
    #c=dwg.add(dwg.circle(center=(cx,cy), r=(camID/2.0), stroke="black", fill="none", stroke_width=0.1))
    # mounting holes top only
#    c=dwg.add(dwg.circle(center=(cx+mho,cy+mho), r=(mhd/2.0), stroke="black", fill="none", stroke_width=0.1))
    c=dwg.add(dwg.circle(center=(cx+mho,cy-mho), r=(mhd/2.0), stroke="black", fill="none", stroke_width=0.1))
#    c=dwg.add(dwg.circle(center=(cx-mho,cy+mho), r=(mhd/2.0), stroke="black", fill="none", stroke_width=0.1))
    c=dwg.add(dwg.circle(center=(cx-mho,cy-mho), r=(mhd/2.0), stroke="black", fill="none", stroke_width=0.1))
    # outer circle conver to path when cam shape is figured out
    #c=dwg.add(dwg.circle(center=(cx,cy), r=(spacerOD/2.0), stroke="black", fill="none", stroke_width=0.1))
    # move to start
    pathText = "M%f,%f\n" % ((cx+x1),(cy-nw))
    #ID half arc
    pathText = pathText+ "A%f,%f 0 0 0 %f,%f\n" %(r1,r1,(cx-x1),(cy-nw))
    pathText = pathText+ "L%f,%f\n" %((cx-x2),(cy-nw))
    pathText = pathText+ "A%f,%f 0 %d 1 %f,%f\n" %(r2,r2,0,(cx+x2),(cy-nw))
    pathText = pathText+ "L%f,%f\n" %((cx+x1),(cy-nw))
    p=dwg.path(d="%s" %pathText,
    stroke="black", fill="none", stroke_width=0.1)
    dwg.add(p)
    return()
def greenHouseBushing(dwg, ox,oy, OD=7.0, ID=3.5) :
    cx=ox+(OD/2.0)
    cy=oy+(OD/2.0)
    c=dwg.add(dwg.circle(center=(cx,cy), r=(ID/2.0), stroke="black", fill="none", stroke_width=0.1))
    c=dwg.add(dwg.circle(center=(cx,cy), r=(OD/2.0), stroke="black", fill="none", stroke_width=0.1))
    return()
def circleCl(dwg,cx,cy,d) :
    r=d/2.0
    c=dwg.add(dwg.circle(center=(cx,cy), r=r, stroke="black", fill="none", stroke_width=0.1))
    l=dwg.add(dwg.line(start=(cx-r,cy), end=(cx+r,cy), stroke="black", fill="none", stroke_width=0.1))
    l=dwg.add(dwg.line(start=(cx,cy-r), end=(cx,cy+r), stroke="black", fill="none", stroke_width=0.1))
    return()
def servoArm(dwg,ox,oy, camOD=35.0, camID=10.0, mhd=3.5,mho=5.5, mha=30, endD=20.0, ar1=145.0, ar2=160.0) :
    cx=ox+(camOD/2.0)
    cy=oy+(camOD/2.0)
    br=camOD/2.0
    lr=endD/2.0
    mhr=mho/math.sin(math.radians(45))
    mhRad1 = math.radians(45+(mha/2.0))
    so=mhr * math.sin(mhRad1)
    co=mhr * math.cos(mhRad1)
    mhRad2 = math.radians(45-(mha/2.0))
    se=mhr * math.sin(mhRad2)
    ce=mhr * math.cos(mhRad2)
    # inner cicle
    circleCl(dwg,cx,cy,camID)
    # mounting holes
    #circleCl(dwg,cx+mho,cy+mho,(mhd))
    circleCl(dwg,cx+co,cy+so,(mhd))
    circleCl(dwg,cx+ce,cy+se,(mhd))
    #circleCl(dwg,cx+mho,cy-mho,(mhd))
    circleCl(dwg,cx+co,cy-so,(mhd))
    circleCl(dwg,cx+ce,cy-se,(mhd))
    #circleCl(dwg,cx-mho,cy+mho,(mhd))
    circleCl(dwg,cx-so,cy+co,(mhd))
    circleCl(dwg,cx-se,cy+ce,(mhd))
    #circleCl(dwg,cx-mho,cy-mho,(mhd))
    circleCl(dwg,cx-co,cy-so,(mhd))
    circleCl(dwg,cx-ce,cy-se,(mhd))
    # servo arm holes
    circleCl(dwg,cx+ar1,cy,(mhd))
    circleCl(dwg,cx+ar2,cy,(mhd))
    # outside path
    # move to start
    pathText = "M%f,%f\n" % (cx,(cy-br))
    #big arc
    pathText = pathText+ "A%f,%f 0 %d 0 %f,%f\n" %(br,br,0,cx,(cy+br))
    #move to start of small arc
    pathText = pathText+ "L%f,%f\n" % ((cx+ar2),(cy+lr))
    #small arc
    pathText = pathText+ "A%f,%f 0 %d 0 %f,%f\n" %(lr,lr,0,(cx+ar2),(cy-lr))
    #final line
    pathText = pathText+ "L%f,%f\n" % (cx,(cy-br))
    p=dwg.path(d="%s" %pathText,
    stroke="black", fill="none", stroke_width=0.1)
    dwg.add(p)
    
sx=2
sy=2
#servoArm(dwg,sx,sy)
ox=27
oy=11
#for y in list(range(sy, (7*oy), oy)) :
#    greenHouseSpacer(dwg,sx,y)

sx=2
sy=2
oy=8
ox=8
for y in list(range(sy, (4*oy), oy)) :
    for x in list(range(sx, (2*ox), ox)) :
        greenHouseBushing(dwg,x,y)

#greenHouseSpacer(dwg,5,5)
#greenHouseSpacer(dwg,5,16)
#greenHouseSpacer(dwg,5,27)

#greenHouseSpacer(dwg,32,5)
#greenHouseSpacer(dwg,32,16)
#greenHouseSpacer(dwg,32,27)
#
#greenHouseCamCalc(dwg,5,5)
#greenHouseCamCalc(dwg,45,5)
#greenHouseCamCalc(dwg,78,5)
#greenHouseCamCalc(dwg,111,5)
#greenHouseCamCalc(dwg,144,5)
#greenHouseCamCalc(dwg,177,5)
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
