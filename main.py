from window import Window
from line import Line
from point import Point

if __name__ == "__main__":
    win = Window(800, 600)

    p1 = Point(10,10)
    p2 = Point(110,10)
    p3 = Point(60,110)

    l1 = Line(p1,p2)
    l2 = Line(p2,p3)
    l3 = Line(p3,p1)

    win.draw_line(l1, "black")
    win.draw_line(l2, "black")
    win.draw_line(l3, "black")
    win.wait_for_close()