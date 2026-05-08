from tkinter import Tk, BOTH, Canvas
import graphics
from cell import Cell
from maze import Maze

def main():
    win = graphics.Window(800, 600)
    maze = Maze(10, 10, 5, 5, 20, 20, win)
    win.wait_for_close()


if __name__ == "__main__":
    main()
