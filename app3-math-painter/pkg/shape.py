from .drawing import Canvas


class Rectange:
    def __init__(self, x: int, y: int, height: int, width: int, color: list) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas: Canvas) -> None:
        canvas.data[self.x:self.x+self.height, self.y: self.y + self.width] = self.color


class Square:
    def __init__(self, x: int, y: int, size: int, color: list) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, canvas: Canvas) -> None:
        canvas.data[self.x:self.x+self.size, self.y : self.y + self.size] = self.color
