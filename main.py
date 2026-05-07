from tkinter import Tk, BOTH, Canvas
from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    test_cell = Cell(win)
    test_cell2 = Cell(win)
    test_cell.draw(10, 20, 10, 20)
    test_cell2.draw(20, 30, 10, 20)
    test_cell.draw_move(test_cell2)
    test_cell3 = Cell(win)
    test_cell3.draw(20, 30, 20, 30)
    test_cell2.draw_move(test_cell3)
    win.wait_for_close()


if __name__ == "__main__":
    main()
