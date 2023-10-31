import numpy as np
from PIL import Image

class Canvas:
    def __init__(self, height: int, width: int, color: list) -> None:
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((height, width, 3), dtype=np.uint8)
        self.data[:] = color

    def export_png(self, filename: str) -> None:
        img = Image.fromarray(self.data, "RGB")
        img.save(filename+".png")
