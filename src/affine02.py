# スケーリング拡大・縮小
import cv2
import numpy as np

# angleに角度を指定して画像を回転させる関数
def RotateToAngle(rows,cols,angle):
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst



try:
		# 画像の読み込み
		img = cv2.imread('./tmp/lena.jpg')

		if img is None:
				print('読み込みできませんでした')
				import sys
				sys.exit()
		
		rows, cols = img.shape[:2]
		rotate_x = RotateToAngle(rows,cols,60)
		cv2.imwrite('./tmp8/function.jpg',rotate_x)


except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
  





# rows,cols = img.shape[:2]
# # 初期の座標をセットx,y,移動量？(一応行列変換？)
# M = np.float32([[1,0,100],[0,1,50]])
#  # 画像、2×3の変換行列、出力画像(width,heigth)
# dst = cv2.warpAffine(img,M,(cols,rows))

# cv2.imwrite('./tmp8/warpAffine.jpg',dst)



# # resizeの引数cv2.inter_cubicは拡大を荒らす
# res = cv2.resize(img, None,fx=2,fy=2, interpolation=cv2.INTER_CUBIC)

# height, width = img.shape[:2]
# print(height, width)


# # cv2.imwrite('./tmp8/scheeeel.jpg',res)

# height1,width1 = res.shape[:2]
# print(height1,width1)


