import graphics

class Cell():
    def __init__(self, window=None):
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
        upleft = graphics.Point(x1, y1)
        upright = graphics.Point(x2, y1)
        botleft = graphics.Point(x1, y2)
        botright = graphics.Point(x2, y2)
        left = graphics.Line(upleft, botleft)
        top = graphics.Line(upleft, upright)
        right = graphics.Line(upright, botright)
        bottom = graphics.Line(botleft, botright)
        if self.__win == None:
            return
        if self.__has_left_wall:
            self.__win.draw_line(left, "black")
        else:
            self.__win.draw_line(left, "white")

        if self.__has_top_wall:
            self.__win.draw_line(top, "black")
        else:
            self.__win.draw_line(top, "white")

        if self.__has_right_wall:
            self.__win.draw_line(right, "black")
        else:
            self.__win.draw_line(right, "white")
            
        if self.__has_bottom_wall:
            self.__win.draw_line(bottom, "black")
        else:
            self.__win.draw_line(bottom, "white")
        
    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"
        centerx = (self.__x1 + self.__x2) / 2
        centery = (self.__y1 + self.__y2) / 2
        to_cell_centerx = (to_cell.__x1 + to_cell.__x2) / 2
        to_cell_centery = (to_cell.__y1 + to_cell.__y2) / 2
        center = graphics.Point(centerx, centery)
        to_cell_center = graphics.Point(to_cell_centerx, to_cell_centery)
        line = graphics.Line(center, to_cell_center)
        if self.__win == None:
            return
        self.__win.draw_line(line, line_color)