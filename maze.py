from cell import Cell

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
                _draw_cells(i, j)

    
        
