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
    file_name = os.path.basename(path)
    img = Image.open(path)
    img_array = np.array(Image.open(path))
    gray_img = img.convert('L')
    gray_img_array = np.array(gray_img)

    # 入力画像を読み込み
    hist = cv2.imread(path)

    b, g, r = hist[:,:,0], hist[:,:,1], hist[:,:,2]

    # 方法1(NumPyでヒストグラムの算出)
    hist_r, bins = np.histogram(r.ravel(),256,[0,256])
    hist_g, bins = np.histogram(g.ravel(),256,[0,256])
    hist_b, bins = np.histogram(b.ravel(),256,[0,256])
    """
    hist_r, bins = np.histogram(r.ravel(),256,[0,256])
    hist_g, bins = np.histogram(g.ravel(),256,[0,256])
    hist_b, bins = np.histogram(b.ravel(),256,[0,256])
    """
    # 方法2(OpenCVでヒストグラムの算出)
    #hist_r = cv2.calcHist([r],[0],None,[256],[0,256])
    #hist_g = cv2.calcHist([g],[0],None,[256],[0,256])
    #hist_b = cv2.calcHist([b],[0],None,[256],[0,256])

    # グラフの作成
    plt.figure()
    plt.xlim(180, 255)
    plt.ylim(0, 20)
    #plt.bar(hist_r)
    plt.plot(hist_r, "-r", label="Red")
    plt.plot(hist_g, "-g", label="Green")
    plt.plot(hist_b, "-b", label="Blue")
    plt.xlabel("Pixel value", fontsize=20)
    plt.ylabel("Number of pixels", fontsize=20)
    plt.legend()
    plt.grid()
    #plt.show()
    #plt.savefig('./hist/' + file_name)


    # グレースケール変換
    gray = cv2.cvtColor(hist, cv2.COLOR_RGB2GRAY)

    # 方法1(NumPyでヒストグラムの算出)
    hist, bins = np.histogram(gray.ravel(),256,[0,256])

    # 方法2(OpenCVでヒストグラムの算出)
    #hist = cv2.calcHist([img],[0],None,[256],[0,256])


    # グラフの作成
    plt.figure()
    plt.xlim(180, 255)
    plt.ylim(0, 20)
    plt.plot(hist)
    plt.xlabel("Pixel value", fontsize=20)
    plt.ylabel("Number of pixels", fontsize=20)
    plt.grid()
    #plt.show()
    #plt.savefig('./hist_gray/' + file_name)


    img_lists =[]
    gray_img_lists = []

    for array in img_array:
        for i in array:
            for n in i:
                if n<180:
                    n=0
                    img_lists.append(n)
                else:
                    img_lists.append(n)

    img_lists = np.array(img_lists)
    img_lists = np.reshape(img_lists, (64,64,3))
    img = Image.fromarray(img_lists.astype(np.uint8))
    img.save('./c_noise/ep41/' + file_name)
    """
    for gray_array in gray_img_array:
        for i in gray_array:
            if i<180:
                i=0
                gray_img_lists.append(i)
            else:
                gray_img_lists.append(i)

    gray_img_lists = np.array(gray_img_lists)
    gray_img_lists = np.reshape(gray_img_lists, (128,128))
    gray_img = Image.fromarray(gray_img_lists.astype(np.uint8))
    gray_img.save('./c_noise_gray/' + file_name)

    k+=1
    """