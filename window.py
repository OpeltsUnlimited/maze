from tkinter import Tk, BOTH, Canvas
from line import Line
from cell import Cell

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "maze"
        self.__canvas = Canvas(self.__root,width=width, height=height)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def draw_line(self, line: Line, color="black"):
        line.draw(self.__canvas, color)

    def draw_cell(self, cell: Cell):
        cell.draw(self.__canvas)

    def close(self):
        self.__running = False