# Quick script that removes images 220x220 images

import os
from PIL import Image

img_dir = "/Users/mo/upscale/20kGuitars"
for filename in os.listdir(img_dir):
    filepath = os.path.join(img_dir, filename)
    with Image.open(filepath) as im:
        x, y = im.size
    totalsize = x*y
    if totalsize < 50000:
        os.remove(filepath)
