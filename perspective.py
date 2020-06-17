"""
透視投影(perspective)とは、3次元の物体を見たとおりに2次元平面に描画するための図法である
"""
import cv2
import numpy as np

try:
    # 画像の読み込み
    img = cv2.imread('./tmp/lena.jpg')

    if img is None:
        print('読み込みできませんでした')
        import sys
        sys.exit()

    # 画像から座標を入力(y,x)
    init_y, init_x = img.shape[:2]
    x0 = init_x/4
    x1 = (init_x*3)/4
    y0 = init_y/4
    y1 = (init_y*3)/4

    # 座標から初期の形をセット
    init_form = np.float32([[x0,y0],[x1,y0],[x1,y1],[x1,y0]])
    # 座標を変更して変更後の形をセット
    # pattern0
    x_margin = init_x/10
    y_margin = init_y/10
    second_form = np.float32([[x0+x_margin,y0+y_margin], init_form[1], init_form[2],[x1-x_margin,y0+y_margin]]) 
    # 透視投影=初期と変更後の形を比較
    perspective_compere = cv2.getPerspectiveTransform(init_form, second_form)
    # 実際に投影し元の形で出力(init_x,init_y)
    dst = cv2.warpPerspective(img, perspective_compere,(init_x,init_y))
    # 保存
    cv2.imwrite('./tmp5/dst0.jpg',dst)

except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))

