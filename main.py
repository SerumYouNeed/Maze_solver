from screen import Window, Point, Line
from cell import Cell
from maze import Maze


def main():
    # screen = Window("500x500", "First window in class")
    
    # line = Line(Point(50,50), Point(400, 400))
    # screen.draw_line(line=line, fill_color="green")

    # c1 = Cell(screen)
    # c1.draw(150, 150, 200, 200)
    # c2 = Cell(screen)
    # c2.draw(300, 150, 350, 200)
    # c1.draw_move(c2, False)

    # m = Maze(100, 100, 5, 5, 35, 25, screen)
    # m._break_entrance_and_exit()
    num_rows = 10
    num_cols = 10
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window("800x600", "Maze")

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()
    # screen.wait_for_close()
    



main()