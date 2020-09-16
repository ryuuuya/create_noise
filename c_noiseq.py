import cv2
import csv
from PIL import Image
import numpy as np

img_array = np.array(Image.open("./test_2_3.png"))

img_lists =[]

for array in img_array:
    for i in array:
        for n in i:
            if n<150:
                n=0
                img_lists.append(n)
            else:
                img_lists.append(n)

img_lists = np.array(img_lists)
img_lists = np.reshape(img_lists, (128,128,3))
img = Image.fromarray(img_lists.astype(np.uint8))
img.save('./noize.png')
