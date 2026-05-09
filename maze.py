import graphics
import random
import time
from cell import Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
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
        if seed is not None:
            random.seed(seed)
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

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
    
    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:
            to_visit = []

            #left check
            if i > 0 and not self.__cells[i-1][j].visited:
                to_visit.append((i-1, j))
            #right check
            if i < self.__num_cols -1 and not self.__cells[i+1][j].visited:
                to_visit.append((i+1, j))
            #top check
            if j > 0 and not self.__cells[i][j-1].visited:
                to_visit.append((i, j-1))
            #bottom check
            if j < self.__num_rows -1 and not self.__cells[i][j+1].visited:
                to_visit.append((i, j+1))
            
            #no unvisited adjacent cells
            if not to_visit:
                return

            cell_to_visit = random.choice(to_visit)

            ni, nj = cell_to_visit[0], cell_to_visit[1]

            #left move
            if ni == i - 1:
                self.__cells[i][j]._Cell__has_left_wall = False
                self.__cells[ni][nj]._Cell__has_right_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(ni, nj)
            #right move
            if ni == i + 1:
                self.__cells[i][j]._Cell__has_right_wall = False
                self.__cells[ni][nj]._Cell__has_left_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(ni, nj)
            #top move
            if nj == j - 1:
                self.__cells[i][j]._Cell__has_top_wall = False
                self.__cells[ni][nj]._Cell__has_bottom_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(ni, nj)
            #bottom move
            if nj == j + 1:
                self.__cells[i][j]._Cell__has_bottom_wall = False
                self.__cells[ni][nj]._Cell__has_top_wall = False
                self.__draw_cell(i, j)
                self.__draw_cell(ni, nj)
            
            self.__break_walls_r(ni, nj)
    
    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False