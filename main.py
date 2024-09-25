from screen import Window, Point, Line, Cell


def main():
    screen = Window("500x500", "First window in class")
    
    # line = Line(Point(50,50), Point(400, 400))
    # screen.draw_line(line=line, fill_color="green")

    c1 = Cell(True, True, True, True, 50, 50, 200, 200, screen)
    c1.draw()

    screen.wait_for_close()
    



main()