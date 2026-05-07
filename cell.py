from line import Line
from point import Point
from tkinter import Tk, BOTH, Canvas

class Cell():
    def __init__(self, window):
        self.__has_left_wall = True
        self.__has_right_wall = True
        self.__has_top_wall = True
        self.__has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    #calls window class's draw method, not the line method
    def draw(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        upleft = Point(x1, y1)
        upright = Point(x2, y1)
        botleft = Point(x1, y2)
        botright = Point(x2, y2)
        if self.__has_left_wall:
            left = Line(upleft, botleft)
            self.__win.draw_line(left, "black")
        if self.__has_top_wall:
            top = Line(upleft, upright)
            self.__win.draw_line(top, "black")
        if self.__has_right_wall:
            right = Line(upright, botright)
            self.__win.draw_line(right, "black")
        if self.__has_bottom_wall:
            bottom = Line(botleft, botright)
            self.__win.draw_line(bottom, "black")
        
    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"
        centerx = (self.__x1 + self.__x2) / 2
        centery = (self.__y1 + self.__y2) / 2
        to_cell_centerx = (to_cell.__x1 + to_cell.__x2) / 2
        to_cell_centery = (to_cell.__y1 + to_cell.__y2) / 2
        center = Point(centerx, centery)
        to_cell_center = Point(to_cell_centerx, to_cell_centery)
        line = Line(center, to_cell_center)
        self.__win.draw_line(line, line_color)