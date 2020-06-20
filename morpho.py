import cv2
import numpy as np




try:
    # 画像の読み込み
    img = cv2.imread('./tmp/j.png')

    if img is None:
        print('読み込みできませんでした')
        import sys
        sys.exit()

    # 5×5サイズのカーネルを作成
    kernel = np.ones((5,5), np.uint8)
    # 縮小
    erosion = cv2.erode(img,kernel,iterations=1)
    cv2.imwrite('./tmp10/erosion_j.jpg',erosion)




except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))