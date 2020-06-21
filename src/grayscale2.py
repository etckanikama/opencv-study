# グレイスケールの方法2
# あとから変換する方法
import cv2


try:
    # 画像の読み込み
    img = cv2.imread('./tmp/lena.jpg')

    if img is None:
        print('読み込みできませんでした')
        import sys
        sys.exit()

    # cv2.cvtColor関数で引数にcv2.COLOR_BAYER_GB2GRAYを指定
    dst = cv2.cvtColor(img, cv2.COLOR_BAYER_GB2GRAY)
    cv2.imwrite('./tmp7/grayscale.jpg',img)


except:
    import sys
    print("Erro:",sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))
