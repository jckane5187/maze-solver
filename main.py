from tkinter import Tk, BOTH, Canvas
from window import Window
from point import Point
from line import Line

def main():
    win = Window(800, 600)
    point1 = Point(20, 100 )
    point2 = Point(100, 200)
    line1 = Line(point1, point2)
    win.draw_line(line1, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
