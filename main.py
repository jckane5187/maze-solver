from tkinter import Tk, BOTH, Canvas
from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    test_cell = Cell(win)
    test_cell.draw(10, 200, 10, 200)
    win.wait_for_close()


if __name__ == "__main__":
    main()
