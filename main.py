from tkinter import Tk, BOTH, Canvas
import graphics
from cell import Cell
from maze import Maze

def main():
    win = graphics.Window(1280, 800)
    maze = Maze(10, 10, 10, 10, 50, 50, win)
    maze.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
