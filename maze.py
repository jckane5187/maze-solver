import graphics
import time
from cell import Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()

    def __create_cells(self):
        self.__cells = [[Cell(self.__win) for a in range(self.__num_rows)] for b in range(self.__num_cols)]
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x1 = self.__x1 + (i * self.__cell_size_x)
        x2 = x1 + self.__cell_size_x

        y1 = self.__y1 + (j * self.__cell_size_y)
        y2 = y1 + self.__cell_size_y
        
        self.__cells[i][j].draw(x1, x2, y1, y2)
        self.__animate()

    def __animate(self):
        if self.__win == None:
            return
        self.__win.redraw()
        time.sleep(.05)

    def __break_entrance_and_exit(self):
        last_col = self.__num_cols - 1
        last_row = self.__num_rows - 1
        self.__cells[0][0]._Cell__has_top_wall = False
        self.__draw_cell(0, 0)

        self.__cells[last_col][last_row]._Cell__has_bottom_wall = False
        self.__draw_cell(last_col, last_row)