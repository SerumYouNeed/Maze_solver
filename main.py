from screen import Window
from maze import Maze
import sys


def main():
    
    num_rows = 20
    num_cols = 20
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    sys.setrecursionlimit(10000)
    win = Window("800x600", "Maze")

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("Your maze is ready!")
    is_solvable = maze.solve()
    if not is_solvable:
        print("There is no way out!")
    else:
        print("We did it!")

    win.wait_for_close()

main()