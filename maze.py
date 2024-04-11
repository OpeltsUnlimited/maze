from cell import Cell
import time
import random

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
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        
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

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            posible_next_visits = []
            # check which directions we might continue
            if i > 0 and not self._cells[i - 1][j].visited:
                posible_next_visits.append((i - 1, j))
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                posible_next_visits.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                posible_next_visits.append((i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                posible_next_visits.append((i, j + 1))

            if not posible_next_visits:
                self._draw_cell(i, j)
                return
            
            # choose a direction at random
            direction_index = random.randrange(len(posible_next_visits))
            next_index = posible_next_visits[direction_index]

            # remove wall depending on direction
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            
            self._draw_cell(i, j)
            self._draw_cell(next_index[0], next_index[1])

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited=False
