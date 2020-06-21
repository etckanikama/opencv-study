import cv2
import numpy as np

def matchImg(img0,img1):
    img1 = cv2.resize(img0, img1.shape[1::-1])
    x = cv2.imwrite('./tmp11/resize.jpg',img1)
    return x

def alfablend(img0,img1):
    matchImg(img0,img1)
    # 合成=cv2.addWeighted(src1, alpha, src2, beta, gamma[])
    dst = cv2.addWeighted(img0,0.5,img1,0.5,0)
    y = cv2.imwrite('./tmp11/add_weighted.jpg',dst)
    return y





try:
    # 画像の読み込み
    img0 = cv2.imread('./tmp/lena.jpg')
    img1 = cv2.imread('./tmp/sky.jpg')

    if img0 is None and img1 is None:
        print('読み込みできませんでした')
        import sys
        sys.exit()

    
    
    matchImg(img0,img1)
 
    # alfablend(img0,img1)
    


except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))