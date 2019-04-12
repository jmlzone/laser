#!/usr/bin/python3
import svgwrite
from svgwrite.extensions import Inkscape

def invertY(yin) :
#    return(0-yin)
    return(yin)

def insideCircle(centerX,centerY,r,x,y) :
    rx=(x-centerX)
    ry=(y-centerY)
    rx2=rx**2
    ry2=ry**2
    r2=r**2
    tf=(rx2+ry2) <=r2;
    print("rx=%d rx2=%d ry=%d ry2=%d, r2=%d:: %s" %(rx,rx2,ry,ry2,r2,str(tf)))
    return(tf)
def frontPlate(dwg,llx,lly) :
    border = dwg.polyline(points=(((60+llx),(90+lly)),((60+llx),(0+lly)),((0+llx),(0+lly)),((0+llx),(100+lly)),((45+llx),(100+lly))), stroke=stroke)
    border.fill(color='none')
    border.stroke(color='black',width=0.1,opacity=1,linejoin='round',miterlimit=4)
    arcstr = "M%d,%d A12,12 0 0,1 %d,%d" % ((60+llx),(90+lly),(45+llx),(100+lly))
    arc=dwg.path(d=arcstr)
    arc.fill(color='none')
    arc.stroke(color='black',width=0.1,opacity=1,linejoin='round',miterlimit=4)
    dwg.add(arc)
    return(border)
dwg = svgwrite.Drawing('circles.svg', profile='full', size=('200mm','150mm'), viewBox=('0 0 200 150'))
dwg.set_desc(title='circle example',desc='my first example')
#view_attributes= {
#    'sodipodi:namedview'
ink=Inkscape(dwg)
#layer=ink.layer(label="top LAYER1", locked=True)
#dwg.add(layer)
xoff=10
yoff=10
step=8
offset=step/2
d=6
r=d/2
cx=25
cy=25
stroke='black'
for x in range(0,50,step) :
    if(int(x/step) & 1) :
        coff = offset
    else :
        coff = 0
    for y in range(0,50,step) :
        nx=(x+xoff)
        ny=invertY(y+yoff+coff)
        if(insideCircle(cx,cy,25,nx,invertY(ny))) :
           c=dwg.add(dwg.circle(center=(nx,ny),r=r,stroke=stroke))
           c.fill(color='none')
           c.stroke(color='black',width=0.1,opacity=1,linejoin='round',miterlimit=4)
           #layer.add(c)
dwg.add(frontPlate(dwg, 10,10))
dwg.save(pretty=True)
