import cv2
import matplotlib.pyplot as plt
import numpy as np
from natsort import natsorted
import glob
import os


path_list = natsorted(glob.glob("./inputs/*.png"))

for path in path_list:
    file_name = os.path.basename(path)
    img = cv2.imread(path)
    #noise_img = cv2.imread("./noise_path/test_3_7.png")
    noise_img = cv2.imread("./touka_test/test.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    noise_img = cv2.cvtColor(noise_img, cv2.COLOR_BGR2RGB)
    x_offset=0
    y_offset=0
    img[y_offset:y_offset+noise_img.shape[0], x_offset:x_offset+noise_img.shape[1]] = noise_img
    cv2.imwrite("./test_noise_img/" + file_name , img)
