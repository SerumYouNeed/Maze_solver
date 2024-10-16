from cell import Cell
import random
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            cells_to_visit = []
            # right:
            if i < self._num_cols - 1 and self._cells[i+1][j].visited == False:
                cells_to_visit.append((i + 1, j))
            # down:
            if j < self._num_rows - 1 and self._cells[i][j+1].visited == False:
                cells_to_visit.append((i, j + 1))
            # left:
            if i > 0 and self._cells[i-1][j].visited == False:
                cells_to_visit.append((i - 1, j))
            # up:
            if j > 0 and self._cells[i][j - 1].visited == False:
                cells_to_visit.append((i, j - 1))
            # no way to go:
            if len(cells_to_visit) == 0:
                self._draw_cell(i,j)
                return
            
            dir = cells_to_visit[random.randrange(len(cells_to_visit))]
            # up:
            if dir[1] == j - 1:
                self._cells[i][j-1].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False
            # down:
            if dir[1] == j + 1:
                self._cells[i][j+1].has_top_wall = False
                self._cells[i][j].has_bottom_wall = False
            # right:
            if dir[0] == i + 1:
                self._cells[i+1][j].has_left_wall = False
                self._cells[i][j].has_left_wall = False
            #left:
            if dir[0] == i - 1:
                self._cells[i-1][j].has_right_wall = False
                self._cells[i][j].has_left_wall = False
                
            self._break_walls_r(dir[0], dir[1])

    def _reset_cells_visited(self):
        for col in range(len(self._cells)):
            for row in range(len(self._cells[col])):
                self._cells[col][row].visited = False
                                
