from p5 import *

class Rbane:
    def __init__(self):
        pass


    def forward(self, ):
        pass

    def turn(self, angle):
        rotate(angle)

    def drawHex(self):
        pass

    def polygon(self, x, y, radius, npoints):
        angle = TWO_PI / npoints;
        a = 0
        while(a < TWO_PI):
            sx = x + cos(a) * radius
            sy = y + sin(a) * radius
            add_vertex(sx, sy)
            i += angle

    def polygon(self, x, y, radius, np):
        circle((x,y),radius)



def setup():
    size(600,600)
    background(51)


def draw():
    background(51)
    translate(width/2,height/2)

    circle((0,0),40)
    circle((0,40),40)
    circle((0,80),40)

    translate(0,80)
    rotate(PI/3)

    circle((0,40),40)
    translate(0,40)
    rotate(PI/3)
    circle((0,40),40)
    translate(0,40)
    rotate(PI/3)
    circle((0,40),40)
    translate(0,40)
    rotate(PI/3)
    circle((0,40),40)
    5

if __name__=="__main__":
    run()
