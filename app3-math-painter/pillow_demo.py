from PIL import Image
import numpy as np

data = np.zeros((50,40,3), dtype=np.uint8)
data[:] = [255,255,0]

data[10:30, 20:40] = [255,0,255]

img = Image.fromarray(data, "RGB")
img.save("demo_pillow.png")
