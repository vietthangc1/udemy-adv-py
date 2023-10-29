from random import randint
import turtle

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle) -> bool:
        return (rectangle.point1.x - self.x)*(rectangle.point2.x-self.x) < 0 \
            and (rectangle.point1.y - self.y)*(rectangle.point2.y-self.y) < 0
    
    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)

class Rectangle:
    def __init__(self, point1: Point, point2: Point) -> None:
        self.point1 = point1
        self.point2 = point2
        self.dim1 = (point2.x - point1.x)
        self.dim2 = (point2.y - point1.y)
        self.area = abs(self.dim1 * self.dim2)

    def __str__(self) -> str:
        output = "Rectangle point: {} & {}".format(self.point1, self.point2)
        return output

class GUIPoint(Point):
    def draw(self, canvas: turtle.Turtle, size = 5, color = "red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

class GUIRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()

        canvas.forward(self.dim1)
        canvas.left(90)
        canvas.forward(self.dim2)
        canvas.left(90)
        canvas.forward(self.dim1)
        canvas.left(90)
        canvas.forward(self.dim2)

point1 = Point(randint(0,300), randint(0,300))
point2 = Point(randint(0,300), randint(0,300))
rec1 = GUIRectangle(point1, point2)
print(rec1)

point3 = GUIPoint(int(input("Guess x: ")), int(input("Guess y: ")))
my_turtle = turtle.Turtle()
rec1.draw(my_turtle)
point3.draw(my_turtle)
turtle.done()

