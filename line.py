from point import Point

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    #feeds the window class's draw method, does not draw on it's own
    def draw(self, canvas, fill_color : str):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)