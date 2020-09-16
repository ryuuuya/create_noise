import cv2
import csv
from PIL import Image
import numpy as np
import glob
import os
from natsort import natsorted
from matplotlib import pyplot as plt

path_list = natsorted(glob.glob("./inputs/ep41/*.png"))

k=1

for path in path_list:
    #読み込み、rgb配列,gray配列
    file_name = os.path.basename(path)
    img = Image.open(path)
    img_array = np.array(Image.open(path))
    gray_img = img.convert('L')
    gray_img_array = np.array(gray_img)

    img_lists =[]
    gray_img_lists = []

    #閾値を以下の値のみ配列に格納（一次元配列）
    for array in img_array:
        for i in array:
            for n in i:
                if n<180:
                    n=0
                    img_lists.append(n)
                else:
                    img_lists.append(n)

    #二次元配列に戻す（画像の形にreshape）
    img_lists = np.array(img_lists)
    img_lists = np.reshape(img_lists, (64,64,3))
    img = Image.fromarray(img_lists.astype(np.uint8))
    img.save('./c_noise/ep41/' + file_name)

    #グレイスケール変換した画像で上と同じ処理を行う
    for gray_array in gray_img_array:
        for i in gray_array:
            if i<180:
                i=0
                gray_img_lists.append(i)
            else:
                gray_img_lists.append(i)

    gray_img_lists = np.array(gray_img_lists)
    gray_img_lists = np.reshape(gray_img_lists, (64,64))
    gray_img = Image.fromarray(gray_img_lists.astype(np.uint8))
    gray_img.save('./c_noise/ep41_gray/' + file_name)