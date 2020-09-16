import cv2
import csv
from PIL import Image
import numpy as np
import glob
import os
from natsort import natsorted

path_list = natsorted(glob.glob("./test/*.png"))

def select_color(color):
    mean = np.array(color).mean(axis=0)
    return (0,0,0,0) if mean <= 50 else color

def to_touka(img):
    w , h = img.size
    touka_img = Image.new('RGBA', (w,h))
    np.array([[touka_img.putpixel((x,y),select_color(img.getpixel((x,y)))) for x in range(w)]for y in range(h)])
    return touka_img


for path in path_list:
    file_name = os.path.basename(path)
    #noise_gray = path.replace("c_noise","c_noise_gray")
    original_img = Image.open(path).convert("RGB")
    to_touka(original_img).save("./touka_test/" + file_name)
    color_img = to_touka(original_img)
    #original_gray = color_img.convert("L")
    #original_gray.save("./touka_gray/" + file_name)
    #original_gray = Image.open(noise_gray).convert("L")
    #to_touka(original_gray).save("./touka_gray/" + file_name)