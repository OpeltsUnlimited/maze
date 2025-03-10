from point import Point
from line import Line
class Cell():
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1: float, y1: float, x2: float, y2: float):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line, "black" if self.has_left_wall else "white")
        
        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line, "black" if self.has_top_wall else "white")
        
        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line, "black" if self.has_right_wall else "white")
        
        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line, "black" if self.has_bottom_wall else "white")

    def draw_move(self, to_cell, undo=False):
        xm1 = (self._x1 + self._x2)/2
        ym1 = (self._y1 + self._y2)/2
        xm2 = (to_cell._x1 + to_cell._x2)/2
        ym2 = (to_cell._y1 + to_cell._y2)/2
        line = Line(Point(xm1, ym1), Point(xm2, ym2))
        self._win.draw_line(line, "gray" if undo else "red")

