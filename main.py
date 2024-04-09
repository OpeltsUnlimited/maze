from window import Window
from line import Line
from point import Point
from cell import Cell

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

    cu = Cell(win)
    cu.has_bottom_wall = False
    cu.draw(120,100,140,120)
    cr = Cell(win)
    cr.has_left_wall = False
    cr.draw(140,120,160,140)
    cd = Cell(win)
    cd.has_top_wall = False
    cd.draw(120,140,140,160)
    cl = Cell(win)
    cl.has_right_wall = False
    cl.draw(100,120,120,140)
    cm = Cell(win)
    cm.has_bottom_wall = False
    cm.has_left_wall = False
    cm.has_right_wall = False
    cm.has_right_wall = False
    cm.draw(120,140,120,140)

    win.wait_for_close()