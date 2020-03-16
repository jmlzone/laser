#!/usr/bin/python3
import svgwrite
import math
from svgwrite.data.types import SVGAttribute
from svgwrite.extensions import Inkscape
def speakerGrill(dwg, cx,cy, diameter=50, holes=6, inlinegap=2, altrowgap=2, mountspace=42, mounthole=3) :
    # start with a hole in the center and work out?
    stroke='black'
    hr=holes/2
    sr=(diameter/2)-hr
    mr=mounthole/2
    mo=mountspace/2
    ox=0
    oy=0
    nx=cx+ox
    ny=cy+oy
    baseRow = True
    while(insideCircle(cx,cy,sr,nx,ny)) :
        while(insideCircle(cx,cy,sr,nx,ny)) :
            c=dwg.add(dwg.circle(center=((cx+ox),(cy+oy)),r=hr,stroke=stroke))
            c.fill(color='none')
            c.stroke(color='black',width=0.1,opacity=1,linejoin='round',miterlimit=4)
            if(oy) :
                c=dwg.add(dwg.circle(center=((cx+ox),(cy-oy)),r=hr,stroke=stroke))
                c.fill(color='none')
                c.stroke(color='black',width=0.1,opacity=1,linejoin='round',miterlimit=4)
            if(ox) :
                c=dwg.add(dwg.circle(center=((cx-ox),(cy+oy)),r=hr,stroke=stroke))
                c.fill(color='none')
                c.stroke(color='black',width=0.1,opacity=1,linejoin='round',miterlimit=4)
                if(oy) :
                    c=dwg.add(dwg.circle(center=((cx-ox),(cy-oy)),r=hr,stroke=stroke))
                    c.fill(color='none')
                    c.stroke(color='black',width=0.1,opacity=1,linejoin='round',miterlimit=4)
            oy=oy+hr+hr+inlinegap
            ny=cy+oy
        ox = ox + hr + hr + altrowgap
        baseRow = not(baseRow)
        if(baseRow) :
            oy=0
        else :
            oy = (hr+hr+inlinegap)/2
        nx=cx+ox
        ny=cy+oy
        if(mo) :
            c=dwg.add(dwg.circle(center=((cx+mo),(cy+mo)),r=mr,stroke='black',fill="none", stroke_width=0.1))
            c=dwg.add(dwg.circle(center=((cx+mo),(cy-mo)),r=mr,stroke='black',fill="none", stroke_width=0.1))
            c=dwg.add(dwg.circle(center=((cx-mo),(cy+mo)),r=mr,stroke='black',fill="none", stroke_width=0.1))
            c=dwg.add(dwg.circle(center=((cx-mo),(cy-mo)),r=mr,stroke='black',fill="none", stroke_width=0.1))
    return()

def insideCircle(centerX,centerY,r,x,y) :
    rx=(x-centerX)
    ry=(y-centerY)
    rx2=rx**2
    ry2=ry**2
    r2=r**2
    tf=(rx2+ry2) <=r2;
    #print("rx=%d rx2=%d ry=%d ry2=%d, r2=%d:: %s" %(rx,rx2,ry,ry2,r2,str(tf)))
    return(tf)

def outlineBBox(dwg, ox,oy,lx,ly) :
    p=dwg.path(d="M%d,%d l%d,0 l0,%d l-%d,0 l0,-%d" % (ox,oy,lx,ly,lx,ly),
    stroke="black",
    fill="none", stroke_width=0.1)
    dwg.add(p)
    return()

def centerLine(dwg,cx,cy,d) :
    r=d/2.0
    #print("Center line at %f,%f length %f" % (cx,cy,d))
    #c=dwg.add(dwg.circle(center=(cx,cy), r=r, stroke="black", fill="none", stroke_width=0.1))
    l=dwg.add(dwg.line(start=(cx-r,cy), end=(cx+r,cy), stroke="black", fill="none", stroke_width=0.1))
    l=dwg.add(dwg.line(start=(cx,cy-r), end=(cx,cy+r), stroke="black", fill="none", stroke_width=0.1))
    return()
def circleCl(dwg,cx,cy,d) :
    r=d/2.0
    c=dwg.add(dwg.circle(center=(cx,cy), r=r, stroke="black", fill="none", stroke_width=0.1))
    centerLine(dwg,cx,cy,d)
    return()

def oblongHole(dwg, cx,cy, od,id):
    rod=od/2.0
    rid=id/2.0
    a=math.acos(rid/rod)
    op = math.sin(a) * rod
    op2 = op*2.0
    centerLine(dwg, cx,cy,id)
    ox=cx-rid
    #print("ox = %f, cx = %f, rid = %f" %(ox,cx,rid))
    oy=cy-op
    pathText = "M%f,%f a%f,%f  0 0,1 %f,0 l0,%f " % (ox,oy, rod,rod,id,op2)
    pathText = pathText+ "a %f,%f  0 0,1 -%f,0 " % (rod,rod,id)
    pathText = pathText+ "l0,-%f " % (op2)
    p=dwg.path(d="%s" %pathText,
    stroke="black",fill="none", stroke_width=0.1)
    dwg.add(p)
    return()
def powerInletModule(dwg, cx,cy):
    circleCl(dwg,(cx-20),(cy-0),2.0)
    circleCl(dwg,(cx+20),(cy+0),2.0)
    ox = cx- 27.0/2.0
    oy = cy - 47.0/2.0
    pathText = "M%f,%f l27,0" % (ox,oy)
    pathText = pathText+ "l0,41 l-6,6 l-15,0 l-6,-6 l0,-41" 
    p=dwg.path(d="%s" %pathText,
    stroke="black",fill="none", stroke_width=0.1)
    dwg.add(p)
    return()

def bindingPostPair(dwg, cx,cy):
    circleCl(dwg,(cx-(19.0/2.0)),(cy-0),7.5)
    circleCl(dwg,(cx+(19.0/2.0)),(cy+0),7.5)
    return()

def centeredBox(dwg, cx,cy, lx,ly):
    ox = cx- lx/2.0
    oy = cy - ly/2.0
    pathText = "M%f,%f " % (ox,oy)
    pathText = pathText+ "l%f,0 " % lx
    pathText = pathText+ "l0,%f " % ly
    pathText = pathText+ "l-%f,0 " % lx
    pathText = pathText+ "l0,-%f " % ly
    p=dwg.path(d="%s" %pathText,
    stroke="black",fill="none", stroke_width=0.1)
    dwg.add(p)
    return()

if (__name__ == "__main__") :
    print("Running as main")
    dwg = svgwrite.Drawing('main.svg', profile='full', size=('300mm','155mm'), viewBox="0 0 300 155")
    ink=Inkscape(dwg)
    outlineBBox(dwg,5,5,232,96)
    oblongHole(dwg,20,20,7.5,6.5)
    powerInletModule(dwg, 50, 50)
    dwg.save(pretty=True)


