import cv2

try:
    img = cv2.imread('./tmp/lena.jpg')

    if img is None:
        print('ファイルを読み込めません')
        import sys
        sys.exit()

    height = img.shape[0]
    width = img.shape[1]
    center = (int(width/2),int(height/2))
    
    # 回転の計算＝2×3の2次元回転のアフィン変換行列 
    # 原点の中心座標・回転角度・スケーリング値
    affin_trans = cv2.getRotationMatrix2D(center, 33.0, 1.0)
    # アフィンの計算(上記)を変換する
    # 画像、2×3の変換行列、出力画像
    dst = cv2.warpAffine(img, affin_trans, (width, height))

    cv2.imwrite('./tmp4/rotate_033.jpg', dst)

except:
    import sys
    print("Error", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))