import numpy as np
import cv2

image=np.zeros((128, 128, 3))

k = 0

image_list = []

for img in image:
    for im in img:
        for i in im:
            k += 1
            if 7999 <=k<= 8007 or 8767<=k<=8769 or 8773<= k<=8775:
                i = 152
                image_list.append(i)
            elif 8383<=k<=8385 or 8392<=k<=8394 or 8770<=k<=8772:
                i = 186
                image_list.append(i)
            elif 8386<=k<=8391:
                i = 230
                image_list.append(i)
            else:
                image_list.append(i)
            

image_list = np.array(image_list)
image_list = np.reshape(image_list,(128,128,3))

cv2.imwrite(".test//test.png",image_list)


