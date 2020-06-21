import cv2
import numpy as np

def retain_noise_cansel(img,kernel):
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    x = cv2.imwrite('./tmp10/noise_cansel.jpg',opening)
    return x 



try:
    # 画像の読み込み
    img = cv2.imread('./tmp/j.png')
    if img is None:
        print('読み込みできませんでした')
        import sys
        sys.exit()

    # 5×5サイズのカーネルを作成
    kernel = np.ones((5,5), np.uint8)
    # 縮小＝(全画素のうち白（１）,黒（０）)
    erosion = cv2.erode(img,kernel,iterations=1)
    cv2.imwrite('./tmp10/erosion_j.jpg',erosion)

    # 膨張 = 全画素のうち1(白)の部分をふやす
    # 普通は縮小後に膨張させるノイズの除去方法で使われる
    dilation = cv2.dilate(img, kernel, iterations=1)
    cv2.imwrite('./tmp10/dilation_j.jpg',dilation)

    #  縮小した画像を膨張させてみてどうなるのか検証しました
    test_dilation = cv2.dilate(erosion, kernel, iterations=1)
    cv2.imwrite('./tmp10/test_noise_j.jpg',test_dilation)

    
    # retain_noise_cansel(img,kernel)

    img1 = cv2.imread('./tmp/opening.png')


    height, width = img1.shape[:2]
    print(height,width)
    # img1の画像の切り出し
    # img1[top:bottom, left:right]
    cut_img1 = img1[0:150,0:112]
    cv2.imwrite('./tmp10/cut_img1.jpg',cut_img1)

    # 画像のノイズキャンセルする関数呼び出し
    retain_noise_cansel(cut_img1,kernel)






except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))