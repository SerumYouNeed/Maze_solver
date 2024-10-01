from cell import Cell
from screen import Point

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win,
                 ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        c = Cell(self.win)
        for i in range(0, self.num_rows):
            row = []
            for j in range(0, self.num_cols):
                row.append(c)
            self._cells.append(row)
        for i in self._cells:
            for j in i:
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # start_point = Point(self.x, self.y)
        # end_point = Point(self.x * self.)
        # self.cell_size_x = i
        # self.cell_size_y = j
        x1 = self.x1 + j * self.cell_size_x
        x2 = self.x1 + (j + 1) * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        y2 = self.y1 + (i + 1) * self.cell_size_y
        cell = Cell(self.win)
        cell.draw(x1, y1, x2, y2)
        self._animate()

    