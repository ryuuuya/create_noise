import cv2


im = cv2.imread("./noi.png")

img = im[64:128,0:64]

cv2.imwrite("./new.png",img)
