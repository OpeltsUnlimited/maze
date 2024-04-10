from cell import Cell
import time

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()
        self._break_entrance_and_exit()
        
    def _create_cells(self):
        for ix in range(0, self.num_cols):
            column = []
            for iy in range(0, self.num_rows):
                column.append(Cell(self.win))
            self._cells.append(column)
        for ix in range(0, self.num_cols):
            for iy in range(0, self.num_rows):
                self._draw_cell(ix, iy)
            

    def _draw_cell(self, i, j):
        if not self.win:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if not self.win:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrancecell = self._cells[0][0]
        entrancecell.has_top_wall = False
        self._draw_cell(0, 0)
        self._animate()
        exitCell = self._cells[self.num_cols - 1][self.num_rows - 1]
        exitCell.has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
        self._animate()