import cv2
import csv
from PIL import Image
import numpy as np
import glob
import os
from natsort import natsorted
from matplotlib import pyplot as plt

path_list = natsorted(glob.glob("./c_noise/ep41_gray/*.png"))

for path in path_list:
    file_name = os.path.basename(path)
    img = Image.open(path)
    img_array = np.array(Image.open(path))
