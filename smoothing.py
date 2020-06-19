import cv2
import numpy as np
# from matplotlib import plt

# angleに角度を指定して画像を回転させる関数
def RotateToAngle(rows,cols,angle):
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst

# a×bの画素すべて１？をつくりnumで割って平均をとる関数
def MakeFilterImage(a,b,num):
    kernel = np.ones((a,b),np.float32)/num
    dst_k = cv2.filter2D(img,-1,kernel)
    return dst_k


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

    average_img=MakeFilterImage(5,5,25)
    cv2.imwrite('./tmp9/func_avg.jpg',average_img)


except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))