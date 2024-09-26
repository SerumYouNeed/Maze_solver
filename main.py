from screen import Window, Point, Line
from cell import Cell


def main():
    screen = Window("500x500", "First window in class")
    
    # line = Line(Point(50,50), Point(400, 400))
    # screen.draw_line(line=line, fill_color="green")

    c1 = Cell(screen)
    c1.draw(150, 150, 200, 200)
    c2 = Cell(screen)
    c2.draw(300, 150, 350, 200)
    c1.draw_move(c2, False)

    screen.wait_for_close()
    



main()