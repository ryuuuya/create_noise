import cv2
import matplotlib.pyplot as plt
import numpy as np
from natsort import natsorted
import glob
import os
from PIL import Image

path_list = natsorted(glob.glob("./img_path/*.png"))

for path in path_list:
    file_name = os.path.basename(path)
    img = Image.open(path)
    noise_img = Image.open("./noise_path/test_3_7.png")
    #print(img)
    #print(noise_img)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #noise_img = cv2.cvtColor(noise_img, cv2.COLOR_BGR2RGB)
    #x_offset=0
    #y_offset=0
    #img[y_offset:y_offset+noise_img.shape[0], x_offset:x_offset+noise_img.shape[1]] = noise_img
    #result = Image.alpha_composite(img,noise_img)
    #result.save("./syn/" + file_name)
    img.paste(noise_img, (0,0), noise_img)
    img.save("./syn/" + file_name)
    #cv2.imwrite("./syn/" + file_name,img)
