# 円を描くプログラム
import numpy as np
import cv2

# 画像の生成
img = np.zeros((400,400,3), np.uint8)
# 対象画像,中心座標=(200,200),色=(b,g,r),太さ
cv2.circle(img,(200,200),50,(255,0,0),1)

cv2.imwrite('./tmp2/circle1.jpg',img)


img = np.zeros((400,400,3), np.uint8)
# 半径100,緑,太さ3
cv2.circle(img,(200,200),100,(0,255,0),3)

cv2.imwrite('./tmp2/circle2.jpg',img)


img = np.zeros((400,400,3), np.uint8)
# 半径150,赤,塗りつぶし
cv2.circle(img,(200,200),150,(0,0,255),-1)

cv2.imwrite('./tmp2/circle3.jpg',img)


