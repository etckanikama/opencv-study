# 輝度平滑化
# 引き延ばすことで、暗い部分がより暗くなったり、明るいところがより明るくなる。

import cv2


try:
    # グレースケールで画像の読み込み
    img = cv2.imread('./tmp/lena.jpg',cv2.IMREAD_GRAYSCALE)

    if img is None:
        print('読み込みできませんでした')
        import sys
        sys.exit()

    # グレースケールを対象にしているの。
    # cv2.equalizeHist関数の挙動を確認....
    dst = cv2.equalizeHist(img)
    cv2.imwrite('./tmp7/equalize.jpg',dst)


except:
    import sys
    print("Erro:",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
