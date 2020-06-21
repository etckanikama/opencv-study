import numpy as np
import cv2

img = np.zeros((400,400,3), np.uint8)
# すべてのpxに対して[:,:]色指定
img[:,:] = [255,0,0]

cv2.imwrite("./tmp1/blueImage.jpg",img)
# cv2.imshow('img1',img) conect to x serverの元　(linuxではめんどい？)

img[:,:]=[0,255,0]
cv2.imwrite('./tmp1/greenImage.jpg',img)


img[:,:] = [0,0,255]
cv2.imwrite('./tmp1/redImage.jpg',img)
