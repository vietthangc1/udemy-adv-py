from pkg.shape import Rectange, Square
from pkg.drawing import Canvas

if __name__ == "__main__":
    canvas_height = 50
    canvas_width = 40
    canvas_color = [255,255,0]

    rectangle_x = 10
    rectangle_y = 10
    rectangle_width = 5
    rectangle_height = 10
    rectangle_color = [255,0,0]

    square_x = 30
    square_y = 25
    square_size = 10
    square_color = [255,0,255]

    rec = Rectange(rectangle_x, rectangle_y, rectangle_height, rectangle_width, rectangle_color)
    sq = Square(square_x, square_y, square_size, square_color)
    canvas = Canvas(canvas_height, canvas_width, canvas_color)

    rec.draw(canvas)
    sq.draw(canvas)
    canvas.export_png("canvas_output")
